<!-- Auto-generated pull requests from the "Add a Paper" and "Add a Resource" issue forms already carry their own checklist; delete this one in that case. This template covers pull requests opened by hand. -->

## Contents of this change

<!-- One or two sentences. If it closes an issue, write "Closes #123". -->

## Checklist

Tick what applies. An unticked box tells the reviewer where to look and does not block the merge.

**For an added or edited paper:**

- [ ] `area` describes the **contribution** of the paper, and not the topic it covers. (Several agents on their own means `scale: [multi-agent]`, not `area: coordination`.)
- [ ] `scale` reflects the scale of the system studied.
- [ ] The paper is absent from the collection under any other title.
- [ ] `id` matches the filename.
- [ ] A record with `status: read` carries `tldr`, `topics` and `about`. Otherwise it is `triaged`, which is a valid end state.
- [ ] `relates_to` is declared in **one direction only** (newer paper points at the older one). The reverse link is computed automatically.

**For a change to `src/data/taxonomy.yml`:**

- [ ] `npm run docs` has been run and the regenerated blocks are committed. The guides and the issue form are generated from that file, and the review needs the change to them in the diff. `docs_sync.yml` also regenerates them on `main` after the merge.
- [ ] A new topic would serve as a filter *today*. A new area has at least one paper to live in it, and an argument from the literature in [TAXONOMY.md](../TAXONOMY.md#bibliographic-basis).

**For every pull request:**

- [ ] `npm run build` passes locally. CI runs it as well, so this step only saves a round trip.
- [ ] For a change under `scripts/`, `npm test` passes and any new behavior has a test. That directory runs unsupervised, and its failures reach contributors as issue comments.

<!-- For a first contribution, say so in the description: reviewers will walk through the points above when requesting changes. -->
