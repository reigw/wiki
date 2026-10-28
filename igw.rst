Structured wiki entities
========================

The local ``igw`` Sphinx domain treats reStructuredText definitions as the
entity database. Define each entity once. Infoboxes, lists, statistics tables,
and backlinks read that definition during the documentation build.

Definitions
-----------

The definition directives are ``igw:weapon``, ``igw:upgrade``,
``igw:file-extension``, ``igw:enemy``, ``igw:level``, ``igw:faction``,
``igw:building``, ``igw:cvar``, and ``igw:entity``. All accept the same options.

Each definition takes a stable, case-sensitive ID containing lowercase ASCII
letters, digits, and single internal hyphens. IDs are unique within their type,
across the entire project. Display names and document paths can change without
changing the ID. A fully qualified target is written ``type:id``.

Cvars use lowercase IDs with underscores replaced by hyphens, and preserve
their console spelling in ``:name:``. For example, ``cg_drawGun`` has the ID
``cg-drawgun``. Its definition and reference syntax are:

.. code-block:: rst

   .. igw:cvar:: cg-drawgun
      :name: cg_drawGun
      :stats:
         flags: CVAR_ARCHIVE

      Documentation of the console variable goes here.

   :igw:cvar:`cg-drawgun`

Cvars participate in infoboxes, references, lists, statistics, and backlinks
like the other entity types. Use ``:type: cvar`` to filter a view to cvars.

The following examples are illustrative authoring syntax, not game data:

.. code-block:: rst

   .. igw:weapon:: example-weapon
      :name: Example weapon
      :summary: A short description.
      :faction: example-faction
      :upgrades: example-upgrade
      :related: enemy:example-enemy, building:example-building
      :stats:
         damage: 25
         fire-rate: 2 shots/s

      Additional prose can contain :igw:upgrade:`example-upgrade` references.

``:name:`` defaults to the ID. ``:summary:`` is optional plain text.
``:stats:`` contains one ``statistic-id: value`` per line, with unique IDs
following the entity ID syntax and nonempty, literal text values. Statistics
are stored only on the definition and reused by views. Units, text, and
explicitly stated ranges are preserved as supplied; the extension does not
infer game-specific constraints, numeric types, or formulas.

``:faction:`` refers to a faction ID. ``:upgrades:`` is a comma-separated list
of upgrade IDs. ``:related:`` takes comma-separated, fully qualified targets.
These relationships must resolve to definitions in the project; definitions
can appear later or in other documents.

Definitions produce an anchored name, an infobox, and their body content.
``:no-infobox:`` suppresses the automatic infobox when a separate presentation
is more useful. It does not remove the entity from the database or search.

References
----------

Each definition directive has a matching semantic role:

.. code-block:: rst

   :igw:weapon:`example-weapon`
   :igw:weapon:`custom link text <example-weapon>`
   :igw:entity:`weapon:example-weapon`

Implicit link text uses the entity's display name. Typed roles only resolve
their own type. The generic ``igw:entity`` role accepts any type, but an
unqualified ID must be unique across types. Use ``entity:some-id`` to target
a generic entity explicitly. Targets are also exported in Sphinx's object
inventory, and standard ``:any:`` references can resolve them.

Presentation
------------

Views query registered definitions without copying their values:

.. code-block:: rst

   .. igw:infobox:: weapon:example-weapon

   .. igw:entity-list::
      :type: weapon
      :faction: example-faction

   .. igw:statistics::
      :type: weapon
      :columns: damage, fire-rate

   .. igw:backlinks:: weapon:example-weapon

``igw:infobox`` and ``igw:backlinks`` require an entity target. Unqualified
targets must be unique across types.

``igw:entity-list`` and ``igw:statistics`` accept optional ``:type:`` and
``:faction:`` filters, combined when both are present. Without filters, they
include every entity. Rows are ordered by display name, then qualified ID.
``:type: entity`` selects generic entities only.

Statistics tables always include a linked name. ``:columns:`` selects and
orders statistic IDs. Without it, the table includes all statistic IDs from
matching entities, in alphabetical order. Missing values display as
``Unknown``; they are not interpreted as zero.

Backlinks list other documents containing semantic references or definition
relationships to the target. Infoboxes and generated lists or tables do not
create backlinks. References through ``:any:`` count when they identify a
unique entity in the ``igw`` registry.

Build behavior
--------------

Definitions, references, and queries belong to their source document. Sphinx
purges removed or changed documents and merges only the documents read by each
parallel worker. Once collection finishes, the domain validates duplicate
definitions and relationships and computes backlinks. Views expand before
Sphinx resolves cross-references, using standard Docutils nodes for output.

When definitions or references change, the extension rewrites documents using
the registry so that existing queries reflect added, edited, or removed
entities. No runtime service or generated source database is needed.

Invalid definitions, duplicate IDs within a type, unresolved relationships,
and unresolved semantic references produce build diagnostics. Use
``sphinx-build -W --keep-going`` to make warnings fail a build.

Further work
------------

@TODO: Define game-specific property schemas and verified formulas before
adding numeric validation or derived statistics.

@TODO: Associate individual properties with sources, methods, game versions,
and verified, measured, documented, estimated, or unknown evidence states.

@TODO: Add sortable tables, categories, navboxes, upgrade trees, damage tables,
galleries, and annotated maps as content requires them.
