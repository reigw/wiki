- while documenting:
  - add @TODO for things that remain undocumented

  - keep things separate, e.g. when documenting map file extension, don't list
    or document specific maps unless you have a really strong reason to

  - separation of concerns !!!

  - for ranges and possible values, don't try to infer them from "observed
    values" from examples - either we know via the actual code or metadata for
    sure the valid ranges OR we don't ; i.e. just because you have examples
    within certain range says nothing about the actual allowed/valid range

  - embed as much data as possible as custom directives and use a custom sphinx
    extension with namespace `igw`

- custom directives:
  - igw:weapon
  - igw:upgrades
  - igw:file-extension
  - igw:enemies
  - igw:levels
  - igw:faction
  - igw:building
  - igw:entity
