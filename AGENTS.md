- while documenting:
  - add @TODO for things that remain undocumented

  - keep things general and separate, e.g. when documenting map file extension,
    don't list or document specific maps unless you have a really strong reason
    to

  - separation of concerns !!!

  - for ranges and possible values, don't try to infer them from "observed
    values" from examples - either we know via the actual code or metadata for
    sure the valid ranges OR we don't ; i.e. just because you have examples
    within certain range says nothing about the actual allowed/valid range ; if
    we don't feel free to add a @TODO if it makes sense

  - there's usually no need to cite where you have information from

  - here are examples NOT to do:
    - `These definitions combine the supplied base/*/* files
      with the Iron Grip: Warlord Game Manual, version 2.4 (2012-03-23),
      transcribed in Iron_Grip_Warlord_Manual.rst.` :: we don't care about where
      the information comes from! we *provide* information ourselves
