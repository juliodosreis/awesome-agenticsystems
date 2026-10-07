import fs from 'node:fs';
import path from 'node:path';
// js-yaml 5 is pure ESM: it no longer exposes a default export.
import { load } from 'js-yaml';

export interface Group {
  label: string;
  blurb: string;
}

export interface Area {
  group: string;
  label: string;
  blurb: string;
}

export interface DomainGroup {
  label: string;
  blurb: string;
  members: string[];
}

export interface ResourceKind {
  label: string;
  blurb: string;
}

export interface Reference {
  key: string;
  cite: string;
  url: string;
  used_for: string;
}

export interface Taxonomy {
  version: number;
  references: Reference[];
  groups: Record<string, Group>;
  areas: Record<string, Area>;
  topics: string[];
  facets: Record<string, string[]>;
  facet_blurbs: Record<string, string>;
  value_blurbs: Record<string, Record<string, string>>;
  domain_groups: Record<string, DomainGroup>;
  resource_kinds: Record<string, ResourceKind>;
  status: string[];
  status_blurbs: Record<string, string>;
  rules: Record<string, number>;
}

const TAXONOMY_PATH = path.join(process.cwd(), 'src/data/taxonomy.yml');

export const taxonomy = load(
  fs.readFileSync(TAXONOMY_PATH, 'utf-8')
) as Taxonomy;

/**
 * The topic vocabulary. It is a flat, global list in the YAML: topics cross
 * areas on purpose, so there is nothing to flatten here.
 */
export const allTopics: string[] = [...new Set(taxonomy.topics ?? [])];

export const areaKeys = Object.keys(taxonomy.areas);

export const resourceKindKeys = Object.keys(taxonomy.resource_kinds ?? {});

/**
 * Areas in group order, with the groups in the order they are written in the
 * YAML. This is the order used by the sidebar and by /areas.
 */
export function areasByGroup(): Array<{
  key: string;
  group: Group;
  areas: Array<{ key: string; area: Area }>;
}> {
  return Object.entries(taxonomy.groups).map(([key, group]) => ({
    key,
    group,
    areas: Object.entries(taxonomy.areas)
      .filter(([, area]) => area.group === key)
      .map(([areaKey, area]) => ({ key: areaKey, area })),
  }));
}

/**
 * The first sentence of a blurb.
 *
 * Area blurbs carry the rule for picking that area, which can run long. The
 * issue form and the compact cards only have room for the opening claim, and
 * every blurb is written so that its first sentence stands on its own.
 */
export function firstSentence(blurb: string): string {
  return blurb.trim().split(/(?<=\.)\s/)[0] ?? blurb.trim();
}

/**
 * Fails loudly when the taxonomy references something that does not exist.
 *
 * Without this a typo makes an area (or a domain, or a description) vanish
 * from the site with no error at all: the page just renders less than it
 * should.
 */
export function assertGroupsResolve(): void {
  const problems: string[] = [];

  const known = new Set(Object.keys(taxonomy.groups));
  for (const [key, area] of Object.entries(taxonomy.areas)) {
    if (!known.has(area.group)) {
      problems.push(`area "${key}" points at a group that does not exist: "${area.group}"`);
    }
  }

  // domain_groups is not its own vocabulary: it only regroups facets.domain.
  // Once they stop matching, /domains shows less than what exists.
  const domains = new Set(taxonomy.facets.domain);
  for (const [key, dg] of Object.entries(taxonomy.domain_groups)) {
    for (const member of dg.members ?? []) {
      if (!domains.has(member)) {
        problems.push(
          `domain_group "${key}" lists "${member}", which is not in facets.domain`
        );
      }
    }
  }

  // The descriptions feed /taxonomy and the issue form. A facet without one
  // renders as an empty paragraph; a description for a facet that no longer
  // exists is dead weight that hides the fact that something was renamed.
  const facetKeys = new Set(Object.keys(taxonomy.facets));
  for (const key of facetKeys) {
    if (!taxonomy.facet_blurbs?.[key]) {
      problems.push(`facet "${key}" has no entry in facet_blurbs`);
    }
  }
  for (const key of Object.keys(taxonomy.facet_blurbs ?? {})) {
    if (!facetKeys.has(key)) {
      problems.push(`facet_blurbs describes "${key}", which is not in facets`);
    }
  }

  // value_blurbs only covers the facets a contributor picks in the issue form,
  // so we do not require it to be complete — but what it does describe has to
  // exist, or the issue form offers an option the validator will reject.
  for (const [facet, values] of Object.entries(taxonomy.value_blurbs ?? {})) {
    const allowed = new Set(taxonomy.facets[facet] ?? []);
    if (!facetKeys.has(facet)) {
      problems.push(`value_blurbs describes facet "${facet}", which does not exist`);
      continue;
    }
    for (const value of Object.keys(values)) {
      if (!allowed.has(value)) {
        problems.push(`value_blurbs.${facet} describes "${value}", which is not a valid value`);
      }
    }
  }

  // A kind without a label renders as an empty sidebar link and an untitled
  // section on /resources.
  for (const [key, kind] of Object.entries(taxonomy.resource_kinds ?? {})) {
    if (!kind?.label) {
      problems.push(`resource_kind "${key}" has no label`);
    }
  }

  if (problems.length) {
    throw new Error(`src/data/taxonomy.yml:\n  - ${problems.join('\n  - ')}`);
  }
}
