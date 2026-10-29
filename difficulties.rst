Difficulties
============

The five difficulty levels are :igw:difficulty:`easy`,
:igw:difficulty:`medium`, :igw:difficulty:`hard`, :igw:difficulty:`brute`,
and :igw:difficulty:`god`. Select a difficulty when starting a game or
creating a server. The selection is controlled by :igw:cvar:`sv-difficulty`;
changes require a map load to take effect.

Difficulty profiles configure enemy health, damage, Power rewards, building
properties, construction times, and upgrade settings. See :doc:`enemies`,
:doc:`buildings`, and the skill reference pages under :doc:`cvars` for the
individual settings.

The base ``skill.cfg`` settings are listed separately from the five
difficulty profiles. They do not represent an additional selectable
difficulty. Configured values do not establish allowed ranges or final
runtime values. A missing assignment leaves the effective value and fallback
behavior unresolved.

.. important::

   Skill settings are not networked and must match on client and server.

@TODO: Verify profile loading order, fallback behavior, and game-version
applicability. Document difficulty effects that are not represented by the
skill settings.

.. _difficulty-file-naming:

File naming scheme
------------------

Difficulty-specific skill configurations and :doc:`wave scripts <scripts/waves>`
append a difficulty suffix to the base name, before the file extension:
``<name><suffix>.<extension>``. Skill configurations use
``skill<suffix>.cfg``. For example, ``skill-e.cfg`` is the Easy skill
configuration, and ``<map>-e.xml`` is an Easy wave definition. Wave filenames
use the map name as their base name: ``<map>.xml`` or
``<map><suffix>.xml``.

``filename-suffix`` includes the separating hyphen. ``selection-value`` is
the value of ``sv_difficulty``.

.. igw:statistics::
   :type: difficulty
   :columns: selection-value, filename-suffix
   :sort-by: selection-value

Unsuffixed wave files, ``<map>.xml``, contain their own values and are
separate definitions. An unsuffixed filename does not establish a difficulty
level or confirm that the file is used as a fallback.

@TODO: Verify how the loader selects difficulty variants, when it uses an
unsuffixed file, and what happens when a requested file is missing.

Definitions
-----------

.. igw:difficulty:: easy
   :name: Easy
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 0
      filename-suffix: -e

.. igw:difficulty:: medium
   :name: Medium
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 1
      filename-suffix: -m

.. igw:difficulty:: hard
   :name: Hard
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 2
      filename-suffix: -h

.. igw:difficulty:: brute
   :name: Brute
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 3
      filename-suffix: -b

.. igw:difficulty:: god
   :name: God
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 4
      filename-suffix: -g

Multiplayer scaling
-------------------

:igw:cvar:`sv-diffmulti` controls a separate player-count difficulty
multiplier. Enemy health increases at spawn for each player, up to four
players. This multiplier does not affect single-player Skirmish games.

@TODO: Document the scaling formula and which settings it affects in
addition to enemy health.
