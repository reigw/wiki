Wave scripts
============

The XML files in ``base/scripts/waves/`` describe map-specific enemy waves,
population limits, AI settings, and skill settings for Iron Grip: Warlord.
Some also contain positions for spawning and placing map objects.

This page describes the XML structure and links skill fields to their cvar
entries. The wave loader's requirements and runtime behavior remain to be
verified where marked ``@TODO``.

Files and difficulty variants
-----------------------------

See :ref:`difficulty-file-naming` for filename patterns, difficulty suffixes,
and unresolved selection rules for wave scripts.

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
inside a wave.

.. list-table:: Population fields
   :header-rows: 1

   * - Element
     - Apparent role
   * - ``CONSCRIPTS``
     - Conscript population limit
   * - ``VEHICLES``
     - Vehicle population limit
   * - ``BOTS``
     - Bot population limit
   * - ``OFFICERS``
     - Officer population limit
   * - ``COMMANDOS``
     - Commando population limit

@TODO: Determine valid values, which actors count toward each cap, how
player-count scaling affects the limits, and whether excess wave members are
delayed or discarded.

WAVESETTINGS: spacing and progression
-------------------------------------

Every definition with settings contains these six fields:

.. list-table:: Wave settings
   :header-rows: 1

   * - Element
     - Apparent role
   * - ``MINWAVEDIST_SMALL``
     - Minimum wave distance for the small category
   * - ``MINWAVEDIST_MEDIUM``
     - Minimum wave distance for the medium category
   * - ``MINWAVEDIST_LARGE``
     - Minimum wave distance for the large category
   * - ``ROAMERINTERVAL``
     - Roamer interval
   * - ``SMALLWAVE_TIME``
     - Small-wave timing or progression threshold
   * - ``MEDIUMWAVE_TIME``
     - Medium-wave timing or progression threshold

The units and scheduling rules remain unverified. In particular, the word
``DIST`` alone does not establish whether a setting measures elapsed time or
spatial separation.

@TODO: Verify valid values, units, the reference point for each timer, and how
these settings interact with :igw:cvar:`sk-wavespawn-delay`,
:igw:cvar:`sk-wavespawn-random`, :igw:cvar:`sk-roamerspawn-delay`, and
:igw:cvar:`sk-roamerspawn-random`.

SKILLSETTINGS: map-specific skill values
----------------------------------------

Each child element uses the corresponding cvar's name as its XML tag and
contains its value as text. For example:

.. code-block:: xml

   <SKILLSETTINGS>
       <sk_morale_max>200</sk_morale_max>
       <sk_officer_respawntime>35000</sk_officer_respawntime>
   </SKILLSETTINGS>

These fields correspond to :igw:cvar:`sk-morale-max` and
:igw:cvar:`sk-officer-respawntime`. The values illustrate the syntax; see the
cvar entries for individual settings and :doc:`../cvars` for the distinction
between skill configuration values, engine defaults, and allowed values.

The following groups list skill fields present in wave scripts. A script can
contain a subset of these fields; an absent field should not be interpreted
as zero.

.. list-table:: Morale cvars
   :header-rows: 1

   * - Group
     - Cvars / XML element names
   * - Unprefixed morale
     - :igw:cvar:`sk-morale-max`, :igw:cvar:`sk-morale-start`
   * - Confederate morale
     - :igw:cvar:`sk-cmorale-max`, :igw:cvar:`sk-cmorale-start`
   * - Atelian morale
     - :igw:cvar:`sk-amorale-max`, :igw:cvar:`sk-amorale-start`
   * - Strongholds
     - :igw:cvar:`sk-deadstronghold-morale`, :igw:cvar:`sk-stronghold-morale`
   * - Officers
     - :igw:cvar:`sk-deadofficer-morale`, :igw:cvar:`sk-officer-morale`
   * - Morale costs
     - :igw:cvar:`sk-player-moralecost`, :igw:cvar:`sk-bot-moralecost`,
       :igw:cvar:`sk-npc-moralecost`, :igw:cvar:`sk-vehicle-moralecost`

The team-specific fields can coexist with the unprefixed fields and have
different values.

@TODO: Determine precedence between unprefixed and team-specific morale fields.

.. list-table:: Spawn and pickup cvars
   :header-rows: 1

   * - Group
     - Cvars / XML element names
   * - Officer spawning
     - :igw:cvar:`sk-officer-respawntime`,
       :igw:cvar:`sk-officer-firstspawntime`
   * - Invulnerability
     - :igw:cvar:`sk-immortal-time`
   * - Wave spawning
     - :igw:cvar:`sk-wavespawn-delay`, :igw:cvar:`sk-wavespawn-random`
   * - Roamer spawning
     - :igw:cvar:`sk-roamerspawn-delay`, :igw:cvar:`sk-roamerspawn-random`
   * - Bombers
     - :igw:cvar:`sk-numbombers`
   * - NPC threshold
     - :igw:cvar:`sk-npc-treshold` (preserve the spelling ``treshold``)
   * - Pickups
     - :igw:cvar:`sk-max-food`, :igw:cvar:`sk-max-jewel`

.. list-table:: Health and damage cvars
   :header-rows: 1

   * - Group
     - Cvars / XML element names
   * - Health
     - :igw:cvar:`sk-health-militia`, :igw:cvar:`sk-health-walker`
   * - Ball of Doom
     - :igw:cvar:`sk-dmg-splash-ballodoom`
   * - Machine-gun turrets
     - :igw:cvar:`sk-dmg-mgturret1`, :igw:cvar:`sk-dmg-mgturret2`,
       :igw:cvar:`sk-dmg-mgturret3`, :igw:cvar:`sk-dmg-mgturret4`
   * - Anti-tank turrets
     - :igw:cvar:`sk-dmg-atturret1`, :igw:cvar:`sk-dmg-atturret2`,
       :igw:cvar:`sk-dmg-atturret3`

@TODO: Verify XML override precedence relative to skill configurations and
player-count scaling, and which additional ``sk_*`` variables the loader accepts.

AI_SETTINGS: AI behavior
------------------------

.. list-table:: AI fields
   :header-rows: 1

   * - Element
     - Apparent role
   * - ``AIM``
     - Aim tuning parameter
   * - ``GANGSIZE``
     - Gang grouping size
   * - ``SQUADSIZE``
     - Squad grouping size
   * - ``REACTIONTIME``
     - Reaction timing parameter
   * - ``WAVEDISTANCE``
     - Wave distance parameter; units and purpose unverified
   * - ``SCALE_LEGIONNAIRE``
     - Legionnaire scaling parameter
   * - ``SCALE_HERRAD``
     - Herrad scaling parameter
   * - ``SCALE_GRENADIER``
     - Grenadier scaling parameter
   * - ``DM_CIVS``
     - Purpose unverified

@TODO: Document valid values, the aim scale, gang versus squad behavior, reaction timer
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
     - Space-separated route IDs, for example ``1 2 3``.
   * - ``size``
     - Numeric wave category.

.. list-table:: Wave children
   :header-rows: 1

   * - Element
     - Apparent role
   * - ``CONSCRIPT``
     - Conscript count
   * - ``TEMPLAR_RATIO``
     - Templar proportion parameter
   * - ``SCARAB``
     - Scarab vehicle count
   * - ``ONTOS``
     - Ontos vehicle count
   * - ``WALKER``
     - Walker vehicle count
   * - ``BOSS_WALKER``
     - Boss walker vehicle count

Repeated vehicle tags occur in the supplied data. A single wave can contain
multiple separate ``<SCARAB>1</SCARAB>`` elements.
Preserve repeated children when reading or editing a definition; converting
children to a dictionary keyed only by tag name would lose data.

@TODO: Verify valid route IDs, sizes, unit counts, and ratios, the numeric
size-to-category mapping, whether waves are selected
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
