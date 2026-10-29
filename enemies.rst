Enemies
=======

Enemy settings vary with the difficulty selected through
:igw:cvar:`sv-difficulty`: :igw:difficulty:`easy`, :igw:difficulty:`medium`,
:igw:difficulty:`hard`, :igw:difficulty:`brute`, or :igw:difficulty:`god`.
Each enemy's difficulty table shows its configured skill settings for all
five difficulties, with the base setting listed separately.

``Unspecified`` means that a profile has no assignment for that setting.
It leaves the effective value and any fallback behavior unresolved.
Configuration values do not establish allowed ranges or final runtime values.

.. important::

   Skill settings are not networked and must match on client and server.

Definitions
-----------

.. igw:enemy:: bomber
   :name: Bomber
   :skill-cvars:
      sk-health-bomber
      sk-power-bomber
      sk-score-bomber
      sk-numbombers

   @TODO: Document the Bomber's armament, attacks, and behavior.

.. igw:enemy:: bosswalker
   :name: Boss Walker
   :skill-cvars:
      sk-health-bosswalker
      sk-power-bosswalker
      sk-score-bosswalker
      sk-speed-bosswalker
      sk-bosswalker-angle-change
      sk-dmg-boss-walker-primary
      sk-dmg-boss-walker-splash
      sk-dmg-bosswalkerbackturret
      sk-blowup-bosswalker-dmg
      sk-blowup-bosswalker-radius
   :stats:
      armament: Cannon and machine gun turrets

   @TODO: Document the Boss Walker's attacks and behavior.

.. igw:enemy:: conscript
   :name: Conscript
   :skill-cvars:
      sk-health-conscript
      sk-power-conscript
      sk-score-conscript
   :stats:
      armament: Weapons include pistols and light machine guns

   @TODO: Document the remaining Conscript weapon variants, attacks, and behavior.

.. igw:enemy:: engineer
   :name: Engineer
   :skill-cvars:
      sk-health-engineer
      sk-power-engineer
      sk-score-engineer
      sk-engineer-spawn-delay

   @TODO: Document the Engineer's armament, attacks, and behavior.

.. igw:enemy:: grenadier
   :name: Grenadier
   :skill-cvars:
      sk-health-grenadier
      sk-power-grenadier
      sk-score-grenadier
   :stats:
      armament: Grenades and a shield

   Throws grenades and carries a shield.

   @TODO: Document the Grenadier's attack timing, shield protection, and behavior.

.. igw:enemy:: herrad
   :name: Herrad
   :skill-cvars:
      sk-health-herrad
      sk-power-herrad
      sk-score-herrad
   :stats:
      armament: Rocket launcher

   @TODO: Document the Herrad's attacks and behavior.

.. igw:enemy:: legionnaire
   :name: Legionnaire
   :skill-cvars:
      sk-health-legionnaire
      sk-power-legionnaire
      sk-score-legionnaire
   :stats:
      armament: Flamethrower

   @TODO: Document the Legionnaire's attacks and behavior.

.. igw:enemy:: officer
   :name: Officer
   :skill-cvars:
      sk-health-officer
      sk-power-officer
      sk-score-officer
      sk-officer-firstspawntime
      sk-officer-respawntime
      sk-officer-morale
      sk-deadofficer-morale
      sk-officer-vistime
      sk-officer-regen-radius
      sk-officer-regen-force
   :stats:
      armament: Minigun

   @TODO: Document the Officer's attacks and behavior.

.. igw:enemy:: ontos
   :name: Ontos
   :skill-cvars:
      sk-health-ontos
      sk-power-ontos
      sk-score-ontos
      sk-speed-ontos
      sk-ontos-angle-change
      sk-dmg-ontos-primary
      sk-dmg-ontos-primarysplash
      sk-blowup-ontos-dmg
      sk-blowup-ontos-radius
   :stats:
      armament: Cannon or rockets, plus machine gun turrets

   @TODO: Document the Ontos weapon variants, attacks, and behavior.

.. igw:enemy:: scarab
   :name: Scarab
   :skill-cvars:
      sk-health-scarab
      sk-power-scarab
      sk-score-scarab
      sk-speed-scarab
      sk-scarab-angle-change
      sk-dmg-scarab
      sk-blowup-scarab-dmg
      sk-blowup-scarab-radius
   :stats:
      armament: Small cannon

   @TODO: Document the Scarab's attacks and behavior.

.. igw:enemy:: spy
   :name: Spy
   :skill-cvars:
      sk-health-spy
      sk-power-spy
      sk-score-spy
      sk-spy-spawn-delay

   @TODO: Document the Spy's armament, attacks, and behavior.

.. igw:enemy:: templar
   :name: Templar
   :skill-cvars:
      sk-health-templar

   @TODO: Document the Templar's armament, attacks, and behavior.

.. igw:enemy:: walker
   :name: Walker
   :skill-cvars:
      sk-health-walker
      sk-power-walker
      sk-score-walker
      sk-speed-walker
      sk-walker-angle-change
      sk-dmg-walker-primary
      sk-blowup-walker-dmg
      sk-blowup-walker-radius
      sk-ball-firerate
      sk-dmg-ball-crush
      sk-dmg-ballodoom
      sk-dmg-splash-ballodoom
      sk-dmg-splash-ballodoom-radius
   :stats:
      armament: Ball of Doom and machine gun turrets

   @TODO: Document the Walker's attacks and behavior.

Shared enemy settings
---------------------

NPC weapon settings are grouped by weapon. Their exact assignment to enemy
variants remains to be verified. Parameter names link to their cvar entries.

NPC weapon damage
~~~~~~~~~~~~~~~~~

.. list-table:: Difficulty settings
   :header-rows: 1

   * - Setting
     - Base
     - Easy
     - Medium
     - Hard
     - Brute
     - God
   * - :igw:cvar:`sk-dmg-npc-cbazooka`
     - 90
     - 70
     - 70
     - 90
     - 110
     - 150
   * - :igw:cvar:`sk-dmg-npc-conflmg`
     - 9
     - 7
     - 8
     - 9
     - 10
     - 15
   * - :igw:cvar:`sk-dmg-npc-dynamite`
     - Unspecified
     - 250
     - 350
     - 400
     - 500
     - 750
   * - :igw:cvar:`sk-dmg-npc-flamer`
     - 10
     - 10
     - 10
     - 10
     - 13
     - 16
   * - :igw:cvar:`sk-dmg-npc-heavyrifle`
     - 5
     - 5
     - 5
     - 5
     - 7
     - 9
   * - :igw:cvar:`sk-dmg-npc-hgrenade`
     - 100
     - 90
     - 90
     - 90
     - 100
     - 130
   * - :igw:cvar:`sk-dmg-npc-lrifle`
     - 10
     - 10
     - 10
     - 10
     - 13
     - 16
   * - :igw:cvar:`sk-dmg-npc-mg`
     - 10
     - 10
     - 10
     - 10
     - 13
     - 15
   * - :igw:cvar:`sk-dmg-npc-minigun`
     - 8
     - 7
     - 10
     - 12
     - 17
     - 20
   * - :igw:cvar:`sk-dmg-npc-molotov`
     - 110
     - 90
     - 90
     - 90
     - 90
     - 90
   * - :igw:cvar:`sk-dmg-npc-pistol`
     - 8
     - 8
     - 8
     - 8
     - 10
     - 13
   * - :igw:cvar:`sk-dmg-npc-suicide`
     - Unspecified
     - 1000
     - 250
     - 280
     - 1450
     - 750
   * - :igw:cvar:`sk-dmg-npc-sword`
     - 8000
     - 8000
     - 8000
     - 8000
     - 8000
     - 8000
   * - :igw:cvar:`sk-dmg-npc-templarmgnade`
     - Unspecified
     - 70
     - 90
     - 120
     - 165
     - 175

NPC splash settings
~~~~~~~~~~~~~~~~~~~

.. list-table:: Difficulty settings
   :header-rows: 1

   * - Setting
     - Base
     - Easy
     - Medium
     - Hard
     - Brute
     - God
   * - :igw:cvar:`sk-npc-dynamite-splash-dmg`
     - Unspecified
     - 300
     - 750
     - 950
     - 500
     - 1200
   * - :igw:cvar:`sk-npc-dynamite-splash-radius`
     - Unspecified
     - 215
     - 225
     - 235
     - 230
     - 235
   * - :igw:cvar:`sk-npc-splash-suicide`
     - Unspecified
     - 150
     - 180
     - 200
     - 270
     - 300

Movement and spawning
~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Difficulty settings
   :header-rows: 1

   * - Setting
     - Base
     - Easy
     - Medium
     - Hard
     - Brute
     - God
   * - :igw:cvar:`g-npcspeed`
     - Unspecified
     - 190
     - 215
     - 235
     - 240
     - 250
   * - :igw:cvar:`sk-tank-maxspeed`
     - 365
     - 365
     - 365
     - 365
     - 365
     - 365
   * - :igw:cvar:`sk-npc-treshold`
     - 20
     - 20
     - 20
     - 20
     - 20
     - 20
   * - :igw:cvar:`sk-wavespawn-delay`
     - 25000
     - 15000
     - 15000
     - 15000
     - 15000
     - 15000
   * - :igw:cvar:`sk-wavespawn-random`
     - 5000
     - 5000
     - 5000
     - 5000
     - 5000
     - 5000
   * - :igw:cvar:`sk-roamerspawn-delay`
     - 30000
     - 10000
     - 10000
     - 10000
     - 10000
     - 10000
   * - :igw:cvar:`sk-roamerspawn-random`
     - 5000
     - 5000
     - 5000
     - 5000
     - 5000
     - 5000

Scaling and morale
~~~~~~~~~~~~~~~~~~

.. list-table:: Difficulty settings
   :header-rows: 1

   * - Setting
     - Base
     - Easy
     - Medium
     - Hard
     - Brute
     - God
   * - :igw:cvar:`sk-dmultiplier`
     - 30
     - 10
     - 25
     - 40
     - 50
     - 75
   * - :igw:cvar:`sk-npc-moralecost`
     - 2
     - 2
     - 1
     - 1
     - 1
     - 1
   * - :igw:cvar:`sk-vehicle-moralecost`
     - 25
     - 35
     - 25
     - 25
     - 25
     - 25
   * - :igw:cvar:`sk-cmorale-start`
     - 200
     - 200
     - 200
     - 200
     - 200
     - 200
   * - :igw:cvar:`sk-cmorale-max`
     - 200
     - 200
     - 200
     - 200
     - 200
     - 200

@TODO: Document the units, formulas, weapon-to-enemy mappings, and fallback
behavior for settings whose runtime meaning remains unverified.

@TODO: Document how difficulty scaling, map overrides, and other runtime
modifiers affect the configured enemy values.
