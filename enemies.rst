Enemies
=======

Enemy settings vary with the difficulty selected through
:igw:cvar:`sv-difficulty`: :igw:difficulty:`easy`, :igw:difficulty:`medium`,
:igw:difficulty:`hard`, :igw:difficulty:`brute`, or :igw:difficulty:`god`.
The health comparison and each enemy's infobox show the configured health
for all five difficulties, with the base setting listed separately.

``Unspecified`` means that a profile has no assignment for that setting.
It leaves the effective value and any fallback behavior unresolved.
Configuration values do not establish allowed ranges or final runtime values.

.. important::

   Skill settings are not networked and must match on client and server.

Health comparison
-----------------

.. igw:statistics::
   :type: enemy
   :columns: base-health, easy-health, medium-health, hard-health, brute-health, god-health

Definitions
-----------

.. igw:enemy:: bomber
   :name: Bomber
   :related: cvar:sk-health-bomber
   :stats:
      base-health: Unspecified
      easy-health: 125
      medium-health: 250
      hard-health: 350
      brute-health: 430
      god-health: 500

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-bomber`
        - Unspecified
        - 8
        - 8
        - 6
        - 6
        - 5
      * - :igw:cvar:`sk-score-bomber`
        - Unspecified
        - 7
        - 7
        - 7
        - 7
        - 7
      * - :igw:cvar:`sk-numbombers`
        - Unspecified
        - 4
        - 5
        - 5
        - 6
        - 6

   @TODO: Document the Bomber's armament, attacks, and behavior.

.. igw:enemy:: bosswalker
   :name: Boss Walker
   :related: cvar:sk-health-bosswalker
   :stats:
      base-health: 5000
      easy-health: 4800
      medium-health: 5800
      hard-health: 6000
      brute-health: 7500
      god-health: 9500
      armament: Cannon and machine gun turrets

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-bosswalker`
        - 350
        - 750
        - 550
        - 500
        - 300
        - 300
      * - :igw:cvar:`sk-score-bosswalker`
        - 300
        - 300
        - 300
        - 300
        - 300
        - 300
      * - :igw:cvar:`sk-speed-bosswalker`
        - 35
        - 35
        - 35
        - 35
        - 35
        - 35
      * - :igw:cvar:`sk-bosswalker-angle-change`
        - 175
        - 175
        - 175
        - 175
        - 175
        - 175
      * - :igw:cvar:`sk-dmg-boss-walker-primary`
        - 130
        - 170
        - 250
        - 450
        - 650
        - 950
      * - :igw:cvar:`sk-dmg-boss-walker-splash`
        - 100
        - 80
        - 100
        - 100
        - 100
        - 100
      * - :igw:cvar:`sk-dmg-bosswalkerbackturret`
        - 30
        - 30
        - 30
        - 30
        - 35
        - 40
      * - :igw:cvar:`sk-blowup-bosswalker-dmg`
        - 400
        - 400
        - 400
        - 400
        - 400
        - 400
      * - :igw:cvar:`sk-blowup-bosswalker-radius`
        - 300
        - 300
        - 300
        - 300
        - 300
        - 300

   @TODO: Document the Boss Walker's attacks and behavior.

.. igw:enemy:: conscript
   :name: Conscript
   :related: cvar:sk-health-conscript
   :stats:
      base-health: 90
      easy-health: 90
      medium-health: 115
      hard-health: 130
      brute-health: 150
      god-health: 175
      armament: Weapons include pistols and light machine guns

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-conscript`
        - 2
        - 2
        - 2
        - 2
        - 1
        - 1
      * - :igw:cvar:`sk-score-conscript`
        - 3
        - 3
        - 3
        - 3
        - 3
        - 3

   @TODO: Document the remaining Conscript weapon variants, attacks, and behavior.

.. igw:enemy:: engineer
   :name: Engineer
   :related: cvar:sk-health-engineer
   :stats:
      base-health: 130
      easy-health: 115
      medium-health: 200
      hard-health: 190
      brute-health: 220
      god-health: 230

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-engineer`
        - Unspecified
        - 100
        - 100
        - 100
        - 100
        - 100
      * - :igw:cvar:`sk-score-engineer`
        - Unspecified
        - 100
        - 100
        - 100
        - 100
        - 100
      * - :igw:cvar:`sk-engineer-spawn-delay`
        - Unspecified
        - 180000
        - 180000
        - 180000
        - 180000
        - 180000

   @TODO: Document the Engineer's armament, attacks, and behavior.

.. igw:enemy:: grenadier
   :name: Grenadier
   :related: cvar:sk-health-grenadier
   :stats:
      base-health: 110
      easy-health: 115
      medium-health: 145
      hard-health: 155
      brute-health: 185
      god-health: 200
      armament: Grenades and a shield

   Throws grenades and carries a shield.

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-grenadier`
        - 3
        - 4
        - 4
        - 3
        - 3
        - 2
      * - :igw:cvar:`sk-score-grenadier`
        - 5
        - 5
        - 5
        - 5
        - 5
        - 5

   @TODO: Document the Grenadier's attack timing, shield protection, and behavior.

.. igw:enemy:: herrad
   :name: Herrad
   :related: cvar:sk-health-herrad
   :stats:
      base-health: 135
      easy-health: 125
      medium-health: 180
      hard-health: 190
      brute-health: 230
      god-health: 250
      armament: Rocket launcher

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-herrad`
        - 4
        - 6
        - 5
        - 4
        - 4
        - 3
      * - :igw:cvar:`sk-score-herrad`
        - 5
        - 5
        - 5
        - 5
        - 5
        - 5

   @TODO: Document the Herrad's attacks and behavior.

.. igw:enemy:: legionnaire
   :name: Legionnaire
   :related: cvar:sk-health-legionnaire
   :stats:
      base-health: 135
      easy-health: 120
      medium-health: 180
      hard-health: 200
      brute-health: 225
      god-health: 250
      armament: Flamethrower

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-legionnaire`
        - 4
        - 5
        - 5
        - 4
        - 4
        - 3
      * - :igw:cvar:`sk-score-legionnaire`
        - 7
        - 7
        - 7
        - 7
        - 7
        - 7

   @TODO: Document the Legionnaire's attacks and behavior.

.. igw:enemy:: officer
   :name: Officer
   :related: cvar:sk-health-officer
   :stats:
      base-health: 650
      easy-health: 670
      medium-health: 900
      hard-health: 1250
      brute-health: 1500
      god-health: 2500
      armament: Minigun

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-officer`
        - 350
        - 550
        - 300
        - 250
        - 200
        - 200
      * - :igw:cvar:`sk-score-officer`
        - 300
        - 300
        - 300
        - 300
        - 300
        - 300
      * - :igw:cvar:`sk-officer-firstspawntime`
        - 200000
        - 200000
        - 200000
        - 200000
        - 200000
        - 200000
      * - :igw:cvar:`sk-officer-respawntime`
        - 27000
        - 27000
        - 27000
        - 27000
        - 27000
        - 27000
      * - :igw:cvar:`sk-officer-morale`
        - 5
        - 5
        - 5
        - 5
        - 5
        - 5
      * - :igw:cvar:`sk-deadofficer-morale`
        - 7
        - 7
        - 7
        - 7
        - 7
        - 7
      * - :igw:cvar:`sk-officer-vistime`
        - 10000
        - 10000
        - 5000
        - 3000
        - 2000
        - 1000
      * - :igw:cvar:`sk-officer-regen-radius`
        - 400
        - 400
        - 400
        - 400
        - 400
        - 400
      * - :igw:cvar:`sk-officer-regen-force`
        - 5
        - 5
        - 5
        - 5
        - 5
        - 5

   @TODO: Document the Officer's attacks and behavior.

.. igw:enemy:: ontos
   :name: Ontos
   :related: cvar:sk-health-ontos
   :stats:
      base-health: 1250
      easy-health: 1275
      medium-health: 1675
      hard-health: 1875
      brute-health: 2000
      god-health: 2500
      armament: Cannon or rockets, plus machine gun turrets

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-ontos`
        - 75
        - 175
        - 150
        - 100
        - 100
        - 100
      * - :igw:cvar:`sk-score-ontos`
        - 150
        - 150
        - 150
        - 150
        - 150
        - 150
      * - :igw:cvar:`sk-speed-ontos`
        - 60
        - 60
        - 70
        - 70
        - 70
        - 70
      * - :igw:cvar:`sk-ontos-angle-change`
        - 100
        - 100
        - 100
        - 100
        - 100
        - 100
      * - :igw:cvar:`sk-dmg-ontos-primary`
        - 230
        - 350
        - 750
        - 2000
        - 2000
        - 2000
      * - :igw:cvar:`sk-dmg-ontos-primarysplash`
        - 150
        - 120
        - 150
        - 150
        - 150
        - 150
      * - :igw:cvar:`sk-blowup-ontos-dmg`
        - 200
        - 200
        - 200
        - 200
        - 200
        - 200
      * - :igw:cvar:`sk-blowup-ontos-radius`
        - 100
        - 100
        - 100
        - 100
        - 100
        - 100

   @TODO: Document the Ontos weapon variants, attacks, and behavior.

.. igw:enemy:: scarab
   :name: Scarab
   :related: cvar:sk-health-scarab
   :stats:
      base-health: 800
      easy-health: 800
      medium-health: 1100
      hard-health: 1200
      brute-health: 1350
      god-health: 1550
      armament: Small cannon

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-scarab`
        - 50
        - 110
        - 90
        - 90
        - 100
        - 90
      * - :igw:cvar:`sk-score-scarab`
        - 100
        - 100
        - 100
        - 100
        - 100
        - 100
      * - :igw:cvar:`sk-speed-scarab`
        - 70
        - 70
        - 80
        - 80
        - 80
        - 80
      * - :igw:cvar:`sk-scarab-angle-change`
        - 150
        - 150
        - 150
        - 150
        - 150
        - 150
      * - :igw:cvar:`sk-dmg-scarab`
        - 35
        - 25
        - 45
        - 60
        - 60
        - 100
      * - :igw:cvar:`sk-blowup-scarab-dmg`
        - 100
        - 100
        - 100
        - 100
        - 100
        - 100
      * - :igw:cvar:`sk-blowup-scarab-radius`
        - 80
        - 80
        - 80
        - 80
        - 80
        - 80

   @TODO: Document the Scarab's attacks and behavior.

.. igw:enemy:: spy
   :name: Spy
   :related: cvar:sk-health-spy
   :stats:
      base-health: 130
      easy-health: 115
      medium-health: 200
      hard-health: 190
      brute-health: 220
      god-health: 230

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-spy`
        - Unspecified
        - 25
        - 25
        - 25
        - 25
        - 25
      * - :igw:cvar:`sk-score-spy`
        - Unspecified
        - 25
        - 25
        - 25
        - 25
        - 25
      * - :igw:cvar:`sk-spy-spawn-delay`
        - Unspecified
        - 120000
        - 120000
        - 120000
        - 120000
        - 120000

   @TODO: Document the Spy's armament, attacks, and behavior.

.. igw:enemy:: templar
   :name: Templar
   :related: cvar:sk-health-templar
   :stats:
      base-health: 50
      easy-health: 125
      medium-health: 180
      hard-health: 190
      brute-health: 230
      god-health: 250

   @TODO: Document the Templar's armament, attacks, and behavior.

.. igw:enemy:: walker
   :name: Walker
   :related: cvar:sk-health-walker
   :stats:
      base-health: 3000
      easy-health: 3050
      medium-health: 4500
      hard-health: 4500
      brute-health: 4500
      god-health: 5000
      armament: Ball of Doom and machine gun turrets

   .. list-table:: Difficulty settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-walker`
        - 130
        - 350
        - 250
        - 200
        - 175
        - 150
      * - :igw:cvar:`sk-score-walker`
        - 200
        - 200
        - 200
        - 200
        - 200
        - 200
      * - :igw:cvar:`sk-speed-walker`
        - 60
        - 60
        - 70
        - 70
        - 70
        - 70
      * - :igw:cvar:`sk-walker-angle-change`
        - 150
        - 150
        - 150
        - 150
        - 150
        - 150
      * - :igw:cvar:`sk-dmg-walker-primary`
        - 35
        - 40
        - 40
        - 50
        - 70
        - 80
      * - :igw:cvar:`sk-blowup-walker-dmg`
        - 250
        - 250
        - 250
        - 250
        - 250
        - 250
      * - :igw:cvar:`sk-blowup-walker-radius`
        - 175
        - 175
        - 175
        - 175
        - 175
        - 175
      * - :igw:cvar:`sk-ball-firerate`
        - 10000
        - 10000
        - 6000
        - 5000
        - 4000
        - 3000
      * - :igw:cvar:`sk-dmg-ball-crush`
        - 100
        - 500
        - 800
        - 900
        - 1300
        - 1700
      * - :igw:cvar:`sk-dmg-ballodoom`
        - 70
        - 70
        - 100
        - 100
        - 200
        - 300
      * - :igw:cvar:`sk-dmg-splash-ballodoom`
        - 800
        - 2500
        - 2500
        - 3300
        - 4000
        - 5000
      * - :igw:cvar:`sk-dmg-splash-ballodoom-radius`
        - 300
        - 315
        - 315
        - 325
        - 325
        - 325

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
