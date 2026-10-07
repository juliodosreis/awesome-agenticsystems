import { defineCollection } from 'astro:content';
// The `z` re-export from astro:content was deprecated in Astro 5+.
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';
import { taxonomy, allTopics, areaKeys, resourceKindKeys, assertGroupsResolve } from './lib/taxonomy';

assertGroupsResolve();

/**
 * Validate a value against a vocabulary from taxonomy.yml.
 *
 * z.enum() needs a literal tuple, so we build the check by hand in order to
 * read the vocabulary from the YAML. The error message names the field and
 * lists the valid values: that is what makes adding a topic cheap and
 * inventing an area impossible.
 */
function vocab(field: string, values: string[]) {
  const allowed = new Set(values);
  // superRefine and not refine(): in Zod 4 the second argument of refine() no
  // longer accepts a function, and the message needs to name the bad value.
  return z.string().superRefine((v, ctx) => {
    if (!allowed.has(v)) {
      ctx.addIssue({
        code: 'custom',
        message:
          `"${v}" is not part of ${field} (src/data/taxonomy.yml). ` +
          `Valid values: ${values.join(', ')}`,
      });
    }
  });
}

const paperCollection = defineCollection({
  // Content Layer API (Astro 5+): replaces the old `type: 'data'`.
  loader: glob({ pattern: '**/*.yml', base: './src/content/papers' }),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    authors: z.array(z.string()),
    year: z.number(),
    // min(1) rather than just optional(): a `venue: ""` passed the schema and
    // rendered a stray separator on the card. No venue means no key.
    venue: z.string().min(1, 'empty venue: omit the key instead of leaving "".').optional(),
    arxiv: z.string().optional(),
    links: z.object({
      // z.url() and not z.string().url(): in Zod 4 formats are top-level.
      paper: z.url(),
      code: z.url().optional()
    }),

    // --- taxonomy: validated against src/data/taxonomy.yml ---
    // Optional in the base schema because a `captured` paper is not classified
    // yet. What each status requires is enforced in the superRefine below.
    area: vocab('areas', areaKeys).optional(),
    topics: z.array(vocab('topics', allTopics)).default([]),
    about: z.array(vocab('facets.about', taxonomy.facets.about)).default([]),
    scale: z.array(vocab('facets.scale', taxonomy.facets.scale)).default([]),
    type: z.array(vocab('facets.type', taxonomy.facets.type)).default([]),
    infra: z.array(vocab('facets.infra', taxonomy.facets.infra)).default([]),
    domain: z.array(vocab('facets.domain', taxonomy.facets.domain)).default([]),

    status: z.enum(['captured', 'triaged', 'read']),
    featured: z.boolean().optional().default(false),
    tldr: z.string().optional(),
    notes: z.string().optional(),
    relates_to: z.array(z.string()).optional().default([]),
    evaluated_on: z.array(z.string()).optional().default([]),

    // YAML hands back a Date when the value is unquoted (`added: 2026-08-21`)
    // and a string when it is quoted (which is how process_issue.py writes it).
    // coerce.date() accepts both and rejects anything else, which is what the
    // previous z.any() let through.
    added: z.coerce.date({ error: 'added must be a YYYY-MM-DD date.' })
  })
  // The three statuses from CONTRIBUTING.md, actually enforced. A paper is
  // never blocked waiting for classification: `captured` requires nothing.
  // What cannot happen is declaring a status and not meeting it.
  .superRefine((paper, ctx) => {
    const require = (field: string, ok: boolean, state: string) => {
      if (!ok) {
        ctx.addIssue({
          code: 'custom',
          path: [field],
          message: `status: ${paper.status} requires "${field}". Drop it back to ${state} if you do not have it yet.`,
        });
      }
    };

    if (paper.status === 'triaged' || paper.status === 'read') {
      require('area', !!paper.area, 'captured');
      require('scale', paper.scale.length > 0, 'captured');
      require('type', paper.type.length > 0, 'captured');
    }

    if (paper.status === 'read') {
      require('tldr', !!paper.tldr, 'triaged');
      require('topics', paper.topics.length > 0, 'triaged');
      require('about', paper.about.length > 0, 'triaged');
    }
  })
});

// Material that is not a paper: protocol specs, books, courses, posts and
// software. Listed on /resources, grouped by `kind`. It has no status cycle:
// a resource is a link with a description, so there is nothing to triage.
const resourceCollection = defineCollection({
  loader: glob({ pattern: '**/*.yml', base: './src/content/resources' }),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    kind: vocab('resource_kinds', resourceKindKeys),
    url: z.url(),
    // A person (a book, a post) or an organization (a protocol, an SDK).
    authors: z.array(z.string()).default([]),
    org: z.string().min(1).optional(),
    year: z.number().optional(),
    // The area the resource relates to. It also lists the resource on that
    // area's page, under the papers.
    area: vocab('areas', areaKeys).optional(),
    description: z.string(),
    added: z.coerce.date({ error: 'added must be a YYYY-MM-DD date.' })
  })
});

export const collections = {
  'papers': paperCollection,
  'resources': resourceCollection
};
