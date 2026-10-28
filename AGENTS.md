- while documenting:
  - add @TODO for things that remain undocumented

  - keep things separate, e.g. when documenting map file extension, don't list
    or document specific maps unless you have a really strong reason to

  - separation of concerns !!!

  - for ranges and possible values, don't try to infer them from "observed
    values" from examples - either we know via the actual code or metadata for
    sure the valid ranges OR we don't ; i.e. just because you have examples
    within certain range says nothing about the actual allowed/valid range

- custom Sphinx extension (`igw` namespace):
  - Treat `.rst` as the structured database: define and validate entities once,
    keeping their data separate from presentation. Generate content at build
    time without a runtime backend or duplicated statistics.
  - Use a Sphinx domain for typed entities, their registry, and semantic
    cross-reference roles; use directives for definitions and presentation.
  - Existing directives: `weapon`, `upgrades`, `file-extension`, `enemies`,
    `levels`, `faction`, `building`, `entity` (all prefixed with `igw:`).
  - Extend as needed, without implementing everything upfront:
    - Entities: weapon, enemy, building, upgrade, map, mechanic, ability, item,
      faction, achievement; nested upgrade levels can define costs and effects.
    - Navigation: related articles, backlinks, categories and category trees,
      filtered entity lists, navboxes.
    - Presentation: infoboxes, sortable statistics and comparison tables,
      upgrade trees, damage tables, galleries, annotated maps. Compute derived
      values from registered data where possible.
    - Research: sources, observations, formulas, version changes, unknowns.
      Associate property evidence with its source, method, and game version;
      distinguish verified, measured, documented, estimated, and unknown data.
  - Prioritize core entities (weapon, enemy, building, upgrade), semantic roles,
    infoboxes, statistics tables, entity lists, backlinks, then observations.
  - Resolve generated content and relationships after all documents have been
    collected; support incremental and parallel builds correctly.
