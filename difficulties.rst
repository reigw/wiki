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

Selection and profiles
----------------------

``selection-value`` is the value of ``sv_difficulty``. ``skill-config`` names
the corresponding difficulty profile.

.. igw:statistics::
   :type: difficulty
   :columns: selection-value, skill-config

Definitions
-----------

.. igw:difficulty:: easy
   :name: Easy
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 0
      skill-config: skill-e.cfg

.. igw:difficulty:: medium
   :name: Medium
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 1
      skill-config: skill-m.cfg

.. igw:difficulty:: hard
   :name: Hard
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 2
      skill-config: skill-h.cfg

.. igw:difficulty:: brute
   :name: Brute
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 3
      skill-config: skill-b.cfg

.. igw:difficulty:: god
   :name: God
   :related: cvar:sv-difficulty
   :stats:
      selection-value: 4
      skill-config: skill-g.cfg

Multiplayer scaling
-------------------

:igw:cvar:`sv-diffmulti` controls a separate player-count difficulty
multiplier. Enemy health increases at spawn for each player, up to four
players. This multiplier does not affect single-player Skirmish games.

@TODO: Document the scaling formula and which settings it affects in
addition to enemy health.
