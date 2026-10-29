``fs_`` Filesystem
==================

See :doc:`../cvars` for flags.

See :doc:`../virtual-filesystem` for directory and PK3 search order. With
the default CVAR values, the game searches one ``base`` directory beneath
:igw:cvar:`fs-basepath` and its PK3s.

.. igw:cvar:: fs-basegame
   :name: fs_basegame
   :stats:
      flags: CVAR_INIT

   Name of an optional base mod directory, searched in addition to ``base``
   and the active mod selected by :igw:cvar:`fs-game`. Defaults to an empty
   string, disabling the extra group. Setting it to ``base`` also adds no
   separate group.

.. igw:cvar:: fs-basepath
   :name: fs_basepath
   :stats:
      flags: CVAR_INIT

   Root directory for installed game files. Defaults to the working directory
   at startup. Game directories such as ``base`` are searched beneath this
   root.

.. igw:cvar:: fs-cdpath
   :name: fs_cdpath
   :stats:
      flags: CVAR_INIT

   Optional CD root directory. Game directories such as ``base`` are searched
   beneath this root. Defaults to an empty string, disabling this root's
   search directories.

.. igw:cvar:: fs-copyfiles
   :name: fs_copyfiles
   :stats:
      flags: CVAR_INIT

   @TODO: Document the behavior, units where applicable, engine default,
   and valid values from registration or consuming code.

.. igw:cvar:: fs-debug
   :name: fs_debug
   :stats:
      flags: None listed

   @TODO: Document the behavior, units where applicable, engine default,
   and valid values from registration or consuming code.

.. igw:cvar:: fs-game
   :name: fs_game
   :stats:
      flags: CVAR_INIT

   Name of the active mod directory, searched in addition to ``base`` and
   the optional base mod selected by :igw:cvar:`fs-basegame`. Defaults to an
   empty string, adding no mod group. Setting it to ``base`` also adds no
   separate group.

.. igw:cvar:: fs-homepath
   :name: fs_homepath
   :stats:
      flags: CVAR_INIT

   Root directory for user files. Defaults to :igw:cvar:`fs-basepath` at
   startup; it is not automatically a separate user-profile directory.
   Game directories such as ``base`` are searched beneath this root.

.. igw:cvar:: fs-restrict
   :name: fs_restrict
   :stats:
      flags: CVAR_INIT

   @TODO: Document the behavior, units where applicable, engine default,
   and valid values from registration or consuming code.
