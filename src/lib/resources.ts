import fs from 'node:fs';
import path from 'node:path';
import { getCollection, type CollectionEntry } from 'astro:content';
import { taxonomy, type ResourceKind } from './taxonomy';

export type Resource = CollectionEntry<'resources'>;

const RESOURCES_DIR = path.join(process.cwd(), 'src/content/resources');

/** Same rule as papers: the `id` field has to equal the filename. */
function assertIdsMatchFilenames(resources: Resource[]): void {
  const onDisk = new Set(
    fs.existsSync(RESOURCES_DIR)
      ? fs.readdirSync(RESOURCES_DIR)
          .filter((f) => f.endsWith('.yml'))
          .map((f) => f.replace(/\.yml$/, ''))
      : []
  );

  const mismatched = resources
    .filter((r) => !onDisk.has(r.data.id))
    .map((r) => `id: "${r.data.id}" matches no file`);
  if (mismatched.length) {
    throw new Error(
      `src/content/resources: the id field must equal the filename. ` +
        mismatched.join('; ')
    );
  }
}

/** Every resource, sorted by title. */
export async function listResources(): Promise<Resource[]> {
  const all = await getCollection('resources');
  assertIdsMatchFilenames(all);
  return all.sort((a, b) => a.data.title.localeCompare(b.data.title));
}

/**
 * Resources grouped by kind, in the order of `resource_kinds` in taxonomy.yml.
 * Kinds with no resources are kept: the sidebar links to every kind, and the
 * anchor has to exist.
 */
export async function resourcesByKind(): Promise<
  Array<{ key: string; kind: ResourceKind; resources: Resource[] }>
> {
  const all = await listResources();
  return Object.entries(taxonomy.resource_kinds).map(([key, kind]) => ({
    key,
    kind,
    resources: all.filter((r) => r.data.kind === key),
  }));
}

/** The "by" line of a card: the authors, the organization, or both. */
export function formatBy(resource: Resource): string {
  const { authors, org, year } = resource.data;
  const who = [authors.join(', '), org].filter(Boolean).join(' · ');
  return [who, year].filter(Boolean).join(', ');
}
