/**
 * Internal links, always relative to the `base` in astro.config.mjs.
 *
 * The site is served under a subpath (/awesome-agenticsystems), so a bare
 * href of "/areas" 404s. That prefix used to be written by hand in ~20 places:
 * a fork, a repo rename or a change to `base` broke every internal link, and
 * the build never noticed, because to Astro they are just strings.
 *
 * BASE_URL may or may not carry a trailing slash depending on config, so we
 * normalize it.
 *
 *   url()                     -> "/awesome-agenticsystems/"
 *   url('/areas')             -> "/awesome-agenticsystems/areas"
 *   url(`/papers/${id}`)      -> "/awesome-agenticsystems/papers/react-2022"
 */
const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

export function url(path = '/'): string {
  return path === '/' ? `${BASE}/` : `${BASE}/${path.replace(/^\//, '')}`;
}

/** The GitHub repo. Used by the nav and by links into the documentation. */
export const REPO_URL = 'https://github.com/juliodosreis/awesome-agenticsystems';
