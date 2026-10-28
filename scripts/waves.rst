Wave scripts
============

The XML files in ``base/scripts/waves/`` describe map-specific enemy waves,
population limits, AI settings, and skill settings for Iron Grip: Warlord.
Some also contain positions for spawning and placing map objects.

This reference describes the XML structure and fields observed in the supplied
files. Descriptions of runtime behavior are inferred from field names, the
companion ``skill*.cfg`` files, and the game manual; the wave loader has not
been verified. Remaining gaps are marked ``@TODO``.

Files and difficulty variants
-----------------------------

Filenames use a map name, optionally followed by a difficulty suffix:
``<map>.xml`` or ``<map>-<difficulty>.xml``. The suffixes correspond to the
companion skill configuration names and the game's difficulty labels:

.. list-table:: Filename conventions
   :header-rows: 1

   * - Suffix
     - Difficulty
     - Example
   * - ``-e``
     - Easy
     - ``<map>-e.xml``
   * - ``-m``
     - Medium
     - ``<map>-m.xml``
   * - ``-h``
     - Hard
     - ``<map>-h.xml``
   * - ``-b``
     - Brute
     - ``<map>-b.xml``
   * - ``-g``
     - God
     - ``<map>-g.xml``
   * - None
     - Unsuffixed definition; selection rules unverified
     - ``<map>.xml``

The unsuffixed files contain their own values and should be treated as separate
definitions.

@TODO: Verify how the loader selects difficulty variants, when it uses an
unsuffixed file, and what happens when a requested file is missing.

Document structure
------------------

All files declare XML version 1.0 and use a lowercase ``definition`` root.
The usual layout contains one of each settings block followed by repeated
``WAVE`` elements. Position records can follow the waves. A second layout is
described under `Nested-route layout`_.

This outline shows the structure; comments stand in for omitted fields and
records, so it is not a complete map configuration:

.. code-block:: xml

   <?xml version="1.0" ?>
   <definition>
       <MAXCOUNTS>
           <!-- Population limits, including CONSCRIPTS and VEHICLES. -->
       </MAXCOUNTS>
       <WAVESETTINGS>
           <!-- Wave spacing and timing settings. -->
       </WAVESETTINGS>
       <SKILLSETTINGS>
           <!-- Map-specific sk_* values. -->
       </SKILLSETTINGS>
       <AI_SETTINGS>
           <!-- Aim, reaction, grouping, and scaling settings. -->
       </AI_SETTINGS>
       <WAVE routes="1 2 3" size="2">
           <CONSCRIPT>30</CONSCRIPT>
           <TEMPLAR_RATIO>0.2</TEMPLAR_RATIO>
           <WALKER>1</WALKER>
       </WAVE>
       <!-- Further WAVE elements and any map-specific position records. -->
   </definition>

Preserve the spelling and capitalization of element names, including lowercase
``sk_*`` fields and position tags. All observed settings are numeric text;
``AIM`` and ``TEMPLAR_RATIO`` use decimal fractions, while the remaining leaf
values use integers. The ``routes`` attribute is a space-separated list.

@TODO: Establish which blocks and fields are required by the loader, the
defaults for omitted fields, and whether element order or case affects loading.

MAXCOUNTS: population limits
----------------------------

The apparent population caps use plural names, unlike the singular unit names
inside a wave. The ranges below describe supplied values, not engine limits.

.. list-table:: Population fields
   :header-rows: 1

   * - Element
     - Apparent role
     - Observed range
   * - ``CONSCRIPTS``
     - Conscript population limit
     - 15 to 100
   * - ``VEHICLES``
     - Vehicle population limit
     - 1 to 5
   * - ``BOTS``
     - Bot population limit
     - 3 to 6
   * - ``OFFICERS``
     - Officer population limit
     - Always 1
   * - ``COMMANDOS``
     - Commando population limit
     - 9 to 30

@TODO: Determine which actors count toward each cap, how player-count scaling
affects the limits, and whether excess wave members are delayed or discarded.

WAVESETTINGS: spacing and progression
-------------------------------------

Every definition with settings contains these six fields:

.. list-table:: Wave settings
   :header-rows: 1

   * - Element
     - Apparent role
     - Observed range
   * - ``MINWAVEDIST_SMALL``
     - Minimum wave distance for the small category
     - 1000 to 14500
   * - ``MINWAVEDIST_MEDIUM``
     - Minimum wave distance for the medium category
     - 500 to 14000
   * - ``MINWAVEDIST_LARGE``
     - Minimum wave distance for the large category
     - 200 to 10000
   * - ``ROAMERINTERVAL``
     - Roamer interval
     - 500 to 13500
   * - ``SMALLWAVE_TIME``
     - Small-wave timing or progression threshold
     - 9000 to 180000
   * - ``MEDIUMWAVE_TIME``
     - Medium-wave timing or progression threshold
     - 120000 to 500000

The time values are consistent with milliseconds, but the assets do not define
their units or scheduling rules. In particular, the word ``DIST`` alone does
not establish whether a setting measures elapsed time or spatial separation.

@TODO: Verify the units, the reference point for each timer, and how these
settings interact with ``sk_wavespawn_*`` and ``sk_roamerspawn_*``.

SKILLSETTINGS: map-specific skill values
----------------------------------------

These elements share names with variables in the companion ``skill*.cfg``
files. Those configurations label a group of values as fallback settings that
can mostly be set per map. The XML files contain different subsets of the
fields below; an absent field should not be interpreted as zero.

Morale
~~~~~~

The manual describes Confederate morale regenerating while an officer is
present, and Atelian morale regenerating while a stronghold is standing.
Officer deaths and stronghold losses reduce the corresponding team's morale.
This provides context for the following field names:

.. list-table:: Morale fields
   :header-rows: 1

   * - Element
     - Apparent role
   * - ``sk_morale_max``, ``sk_morale_start``
     - Unprefixed maximum and starting morale
   * - ``sk_Cmorale_max``, ``sk_Cmorale_start``
     - Confederate maximum and starting morale
   * - ``sk_Amorale_max``, ``sk_Amorale_start``
     - Atelian maximum and starting morale
   * - ``sk_deadstronghold_morale``
     - Morale loss associated with a destroyed stronghold
   * - ``sk_stronghold_morale``
     - Morale regeneration associated with a standing stronghold
   * - ``sk_deadofficer_morale``
     - Morale loss associated with an officer's death
   * - ``sk_officer_morale``
     - Morale regeneration associated with a living officer
   * - ``sk_player_moralecost``
     - Morale cost associated with a player's death
   * - ``sk_bot_moralecost``
     - Morale cost associated with a bot's death
   * - ``sk_npc_moralecost``
     - Morale cost associated with an NPC's death
   * - ``sk_vehicle_moralecost``
     - Morale cost associated with a vehicle's destruction

The team-specific fields can coexist with the unprefixed fields and have
different values.

@TODO: Determine precedence between unprefixed and team-specific morale fields,
which NPC categories incur each cost, and the tick interval for regeneration
or continuing morale loss.

Spawning and pickups
~~~~~~~~~~~~~~~~~~~~

.. list-table:: Spawn and pickup fields
   :header-rows: 1

   * - Element
     - Apparent role
   * - ``sk_officer_respawntime``
     - Officer respawn delay
   * - ``sk_officer_firstspawntime``
     - Delay before the first officer spawn
   * - ``sk_immortal_time``
     - Duration of temporary invulnerability, apparently after spawning
   * - ``sk_wavespawn_delay``, ``sk_wavespawn_random``
     - Base wave spawn delay and random timing component
   * - ``sk_roamerspawn_delay``, ``sk_roamerspawn_random``
     - Base roamer spawn delay and random timing component
   * - ``sk_numbombers``
     - Bomber count setting; observed values range from 0 to 12
   * - ``sk_npc_treshold``
     - NPC threshold setting; preserve the spelling ``treshold``
   * - ``sk_max_food``
     - Maximum food pickup count
   * - ``sk_max_jewel``
     - Maximum jewel pickup count

Timing values such as ``sk_officer_respawntime = 35000`` and
``sk_immortal_time = 4000`` suggest milliseconds. The random components' names
do not establish their distribution or whether they are added to or subtracted
from the base delay.

@TODO: Confirm timer units and randomization, what triggers invulnerability,
the bomber count's scope, pickup replenishment rules, and what
``sk_npc_treshold`` controls.

Health and damage
~~~~~~~~~~~~~~~~~

Some files also include combat variables ordinarily found in skill
configurations:

.. list-table:: Combat fields
   :header-rows: 1

   * - Element
     - Apparent role
   * - ``sk_health_militia``
     - Militia health
   * - ``sk_health_walker``
     - Walker health
   * - ``sk_dmg_splash_ballodoom``
     - Ball of Doom splash damage
   * - ``sk_dmg_mgturret1``, ``sk_dmg_mgturret2``,
       ``sk_dmg_mgturret3``, ``sk_dmg_mgturret4``
     - Machine-gun turret damage by upgrade level
   * - ``sk_dmg_atturret1``, ``sk_dmg_atturret2``, ``sk_dmg_atturret3``
     - Anti-tank turret damage by upgrade level

@TODO: Verify XML override precedence relative to skill configurations and
player-count scaling, and which additional ``sk_*`` variables the loader accepts.

AI_SETTINGS: AI behavior
------------------------

.. list-table:: AI fields
   :header-rows: 1

   * - Element
     - Apparent role
     - Observed values
   * - ``AIM``
     - Aim tuning parameter
     - 0.2 to 0.9
   * - ``GANGSIZE``
     - Gang grouping size
     - 3 to 6
   * - ``SQUADSIZE``
     - Squad grouping size
     - 2 to 5
   * - ``REACTIONTIME``
     - Reaction timing parameter, apparently in milliseconds
     - 200 to 3000
   * - ``WAVEDISTANCE``
     - Wave distance parameter; units and purpose unverified
     - 10 to 100
   * - ``SCALE_LEGIONNAIRE``
     - Legionnaire scaling parameter
     - 1 or 2
   * - ``SCALE_HERRAD``
     - Herrad scaling parameter
     - 1 or 2
   * - ``SCALE_GRENADIER``
     - Grenadier scaling parameter
     - Always 3 when present
   * - ``DM_CIVS``
     - Purpose unverified
     - 10

@TODO: Document the aim scale, gang versus squad behavior, reaction timer
units, wave distance calculation, the ``SCALE_*`` formulas, and ``DM_CIVS``.

WAVE: routes and composition
----------------------------

In the usual layout, each ``WAVE`` has ``routes`` and ``size`` attributes and
contains unit counts directly. For example:

.. code-block:: xml

   <WAVE routes="1 2 3" size="2">
       <CONSCRIPT>10</CONSCRIPT>
       <TEMPLAR_RATIO>0.3</TEMPLAR_RATIO>
       <WALKER>1</WALKER>
       <ONTOS>1</ONTOS>
   </WAVE>

.. list-table:: Wave attributes
   :header-rows: 1

   * - Attribute
     - Observed form
   * - ``routes``
     - Space-separated route IDs. IDs 1 through 4 occur, including lists such
       as ``1 2``, ``1 3``, and ``1 2 3 4``.
   * - ``size``
     - Numeric category: ``0``, ``1``, or ``2``. Files group entries in the
       order ``2``, then ``1``, then ``0``.

.. list-table:: Wave children
   :header-rows: 1

   * - Element
     - Apparent role
     - Observed values
   * - ``CONSCRIPT``
     - Conscript count
     - 7 to 80
   * - ``TEMPLAR_RATIO``
     - Templar proportion parameter
     - 0.05 to 0.8; omitted in many waves
   * - ``SCARAB``
     - Scarab vehicle count
     - 1 per element
   * - ``ONTOS``
     - Ontos vehicle count
     - 1 or 2 per element
   * - ``WALKER``
     - Walker vehicle count
     - 1 per element
   * - ``BOSS_WALKER``
     - Boss walker vehicle count
     - 1 per element

Repeated vehicle tags occur in the supplied data. A single wave can contain
multiple separate ``<SCARAB>1</SCARAB>`` elements.
Preserve repeated children when reading or editing a definition; converting
children to a dictionary keyed only by tag name would lose data.

@TODO: Verify the numeric size-to-category mapping, whether waves are selected
in sequence or from a pool, how route lists distribute units, how route IDs
connect to map entities, how repeated vehicle tags are processed, and how
``TEMPLAR_RATIO`` affects the conscript count and rounding.

Position records
----------------

Position records are direct children of ``definition``, after the ``WAVE``
elements, and each contains lowercase integer fields ``x``, ``y``, ``z``, and
``yaw``. The following example illustrates the field structure:

.. code-block:: xml

   <rocketspot>
       <x>100</x>
       <y>200</y>
       <z>64</z>
       <yaw>90</yaw>
   </rocketspot>

The names suggest map-space coordinates and an orientation angle. Signed
positions and negative yaw values occur in the data.

.. list-table:: Position record types
   :header-rows: 1

   * - Element
     - Apparent role
   * - ``SPAWNPOINT``
     - Spawn position; actor type unverified
   * - ``deathhand``
     - Deathhand placement
   * - ``rocketspot``
     - Rocket pickup placement
   * - ``radiospot``
     - Radio pickup placement

@TODO: Verify coordinate and yaw units, whether records are simultaneous
placements or candidate locations, how duplicate positions are handled, and
which actors use ``SPAWNPOINT``.

Nested-route layout
-------------------

A second observed layout uses ``WAVE`` elements with a ``time`` attribute and
nested ``ROUTE`` elements with an ``id`` attribute. These waves omit the
``routes`` and ``size`` attributes, and the definitions omit the four settings
blocks. For example:

.. code-block:: xml

   <WAVE time="1000000">
       <ROUTE id="1">
           <CONSCRIPT>15</CONSCRIPT>
       </ROUTE>
       <ROUTE id="2">
           <CONSCRIPT>15</CONSCRIPT>
           <GRENADIER>5</GRENADIER>
       </ROUTE>
   </WAVE>

Unit counts belong to each ``ROUTE``. Both ``CONSCRIPT`` and ``GRENADIER``
occur here; ``GRENADIER`` does not occur as a direct child of waves in the
other layout.

@TODO: Determine whether the current game still loads this layout, whether
``time`` is absolute or relative and in what units, and how out-of-range timer
values are handled.
