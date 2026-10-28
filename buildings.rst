Buildings
=========

Buildings include defensive turrets, traps, support stations, and strongholds.
Each definition records the building's game ID, such as ``mgturret``.

Construction and repairs
------------------------

Press ``G`` by default to switch between FPS and Construction mode. In
Construction mode, select a building from the building panel and place it
within the permitted area. Construction mode uses a top-down view and prevents
attacking, so move to a secure position before switching.

Construction, repairs, and turret upgrades cost Power. The
:igw:weapon:`toolkit` repairs damaged structures. Turret upgrades improve
health and attack power.

@TODO: Document placement restrictions, construction and repair mechanics,
and how player upgrades affect building and repair speed.

Difficulty settings
-------------------

Building settings vary with :igw:cvar:`sv-difficulty`: :igw:difficulty:`easy`,
:igw:difficulty:`medium`, :igw:difficulty:`hard`, :igw:difficulty:`brute`, or
:igw:difficulty:`god`. The base setting is listed separately. Health
comparisons and infoboxes use level-one health for turrets.

Tables preserve the raw configured values. Build times, upgrade times,
attack rates, distances, and support settings have no units assigned here
until their interpretation is verified. Configuration values do not establish
allowed ranges or final runtime values. ``Unspecified`` means that a profile
has no assignment; effective values and fallback behavior remain unresolved.

.. important::

   Skill settings are not networked and must match on client and server.

@TODO: Verify time and distance units, attack-rate interpretation, damage
application, and the game versions to which these settings apply.

Health comparison
-----------------

.. igw:statistics::
   :type: building
   :columns: game-id, base-health, easy-health, medium-health, hard-health, brute-health, god-health

Definitions
-----------

.. igw:building:: mgturret
   :name: Machine Gun Turret
   :related: cvar:sk-health-mgturret1
   :stats:
      game-id: mgturret
      base-health: 650
      easy-health: 900
      medium-health: 900
      hard-health: 900
      brute-health: 900
      god-health: 900

   A manned machine gun nest with fast, accurate fire against infantry. It
   cannot damage armored targets such as tanks and walkers. Three upgrades
   provide four levels in total.

   .. list-table:: Construction settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-mgturret`
        - 325
        - 250
        - 250
        - 250
        - 250
        - 250
      * - :igw:cvar:`sk-buildtime-mgturret`
        - 20000
        - 12000
        - 13000
        - 13000
        - 15000
        - 15000

   .. list-table:: Level settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-dmg-mgturret1`
        - 7
        - 7
        - 8
        - 8
        - 7
        - 7
      * - :igw:cvar:`sk-attackrate-mgturret1`
        - 80
        - 75
        - 75
        - 75
        - 75
        - 75
      * - :igw:cvar:`sk-dmg-mgturret2`
        - 9
        - 10
        - 11
        - 11
        - 10
        - 10
      * - :igw:cvar:`sk-attackrate-mgturret2`
        - 70
        - 60
        - 60
        - 60
        - 60
        - 60
      * - :igw:cvar:`sk-dmg-mgturret3`
        - 11
        - 15
        - 18
        - 18
        - 15
        - 15
      * - :igw:cvar:`sk-attackrate-mgturret3`
        - 60
        - 50
        - 50
        - 50
        - 50
        - 50
      * - :igw:cvar:`sk-dmg-mgturret4`
        - 17
        - 30
        - 27
        - 27
        - 25
        - 25
      * - :igw:cvar:`sk-attackrate-mgturret4`
        - 50
        - 40
        - 40
        - 40
        - 40
        - 40
      * - :igw:cvar:`sk-range-mg1`
        - 1200
        - 1500
        - 1500
        - 1500
        - 1500
        - 1500
      * - :igw:cvar:`sk-range-mg2`
        - 1600
        - 1800
        - 1800
        - 1800
        - 1800
        - 1800
      * - :igw:cvar:`sk-range-mg3`
        - 2000
        - 2500
        - 2500
        - 2500
        - 2500
        - 2500
      * - :igw:cvar:`sk-range-mg4`
        - 3000
        - 3900
        - 3900
        - 3900
        - 3900
        - 3900
      * - :igw:cvar:`sk-health-mgturret2`
        - 775
        - 1500
        - 1500
        - 1500
        - 1500
        - 1500
      * - :igw:cvar:`sk-health-mgturret3`
        - 825
        - 2000
        - 2000
        - 1900
        - 1900
        - 2000
      * - :igw:cvar:`sk-health-mgturret4`
        - 950
        - 3500
        - 2500
        - 2500
        - 2500
        - 2500

   .. list-table:: Upgrade settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-mgupgr2`
        - 100
        - 150
        - 150
        - 150
        - 150
        - 150
      * - :igw:cvar:`sk-upgradetime-mgupgr2`
        - 8000
        - 8000
        - 10000
        - 10000
        - 13000
        - 15000
      * - :igw:cvar:`sk-cost-mgupgr3`
        - 175
        - 250
        - 250
        - 250
        - 250
        - 250
      * - :igw:cvar:`sk-upgradetime-mgupgr3`
        - 13000
        - 15000
        - 20000
        - 20000
        - 25000
        - 28000
      * - :igw:cvar:`sk-cost-mgupgr4`
        - 200
        - 350
        - 350
        - 350
        - 350
        - 350
      * - :igw:cvar:`sk-upgradetime-mgupgr4`
        - 15000
        - 17000
        - 25000
        - 25000
        - 30000
        - 35000
      * - :igw:cvar:`sk-score-turretupgradepercent`
        - 10
        - 10
        - 10
        - 10
        - 10
        - 10

   @TODO: Document targeting, operation of the gun, and how the turret-upgrade
   score percentage is applied.

.. igw:building:: atturret
   :name: Anti-Tank Turret
   :related: cvar:sk-health-atturret1
   :stats:
      game-id: atturret
      base-health: 1000
      easy-health: 1500
      medium-health: 1500
      hard-health: 1500
      brute-health: 1500
      god-health: 1500

   Fires explosive shells that damage infantry and vehicles, making it an
   effective counter to tanks and walkers. Its slow rate of fire leaves it
   vulnerable to groups of enemies.

   .. list-table:: Construction settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-atturret`
        - 450
        - 450
        - 450
        - 450
        - 450
        - 450
      * - :igw:cvar:`sk-buildtime-atturret`
        - 20000
        - 14500
        - 16500
        - 16500
        - 18500
        - 18500

   .. list-table:: Level settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-dmg-atturret1`
        - 700
        - 700
        - 800
        - 800
        - 700
        - 700
      * - :igw:cvar:`sk-attackrate-atturret1`
        - 4000
        - 5000
        - 5000
        - 5000
        - 5000
        - 5000
      * - :igw:cvar:`sk-dmg-atturret2`
        - 825
        - 1200
        - 1300
        - 1300
        - 1100
        - 1100
      * - :igw:cvar:`sk-attackrate-atturret2`
        - 3500
        - 4000
        - 4000
        - 4000
        - 4000
        - 4000
      * - :igw:cvar:`sk-dmg-atturret3`
        - 1150
        - 1500
        - 1500
        - 1500
        - 1400
        - 1400
      * - :igw:cvar:`sk-attackrate-atturret3`
        - 3000
        - 3000
        - 3000
        - 3000
        - 3000
        - 3000
      * - :igw:cvar:`sk-range-at1`
        - 3000
        - 3000
        - 3000
        - 3000
        - 3000
        - 3000
      * - :igw:cvar:`sk-range-at2`
        - 4000
        - 5000
        - 5000
        - 5000
        - 5000
        - 5000
      * - :igw:cvar:`sk-range-at3`
        - 7000
        - 9000
        - 9000
        - 9000
        - 9000
        - 9000
      * - :igw:cvar:`sk-dmgradius-at1`
        - 30
        - 30
        - 30
        - 30
        - 30
        - 30
      * - :igw:cvar:`sk-dmgradius-at2`
        - 50
        - 50
        - 50
        - 50
        - 50
        - 50
      * - :igw:cvar:`sk-dmgradius-at3`
        - 70
        - 70
        - 70
        - 70
        - 70
        - 70
      * - :igw:cvar:`sk-dmgradius-at4`
        - 80
        - 80
        - 80
        - 80
        - 80
        - 80
      * - :igw:cvar:`sk-health-atturret2`
        - 1375
        - 2500
        - 2500
        - 2300
        - 2300
        - 2500
      * - :igw:cvar:`sk-health-atturret3`
        - 1750
        - 4000
        - 3500
        - 3500
        - 3500
        - 3500

   .. list-table:: Upgrade settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-atupgr2`
        - 150
        - 250
        - 250
        - 250
        - 250
        - 250
      * - :igw:cvar:`sk-upgradetime-atupgr2`
        - 10000
        - 12000
        - 20000
        - 20000
        - 25000
        - 27000
      * - :igw:cvar:`sk-cost-atupgr3`
        - 175
        - 300
        - 300
        - 300
        - 300
        - 300
      * - :igw:cvar:`sk-upgradetime-atupgr3`
        - 15000
        - 18000
        - 30000
        - 30000
        - 35000
        - 38000
      * - :igw:cvar:`sk-score-turretupgradepercent`
        - 10
        - 10
        - 10
        - 10
        - 10
        - 10

   Level-four health, damage, attack rate, range, cost, and upgrade-time
   assignments are commented out. The active ``sk_dmgradius_at4`` setting alone
   does not establish an available fourth level.

   @TODO: Verify the available upgrade levels, targeting behavior, splash-damage
   mechanics, and how the turret-upgrade score percentage is applied.

.. igw:building:: fuelbomb
   :name: Fuel Bomb
   :related: cvar:sk-health-fuelbomb1
   :stats:
      game-id: fuelbomb
      base-health: 400
      easy-health: 400
      medium-health: 400
      hard-health: 400
      brute-health: 400
      god-health: 400

   A structure made from fuel barrels and explosives, triggered by shooting
   it. Once triggered, it explodes when enough damage has been dealt or five
   seconds have passed, whichever comes first. A small initial blast disperses
   the fuel into a mist; a second, larger explosion ignites it seconds later.

   .. list-table:: Construction settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-fuelbomb`
        - 30
        - 75
        - 75
        - 75
        - 75
        - 75
      * - :igw:cvar:`sk-buildtime-fuelbomb`
        - 5000
        - 5000
        - 5000
        - 5000
        - 5000
        - 5000

   .. list-table:: Explosion settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-dmg-fuelbomb1`
        - 1000
        - 1000
        - 1000
        - 1000
        - 1000
        - 1000
      * - :igw:cvar:`sk-dmgradius-fuelbomb`
        - 170
        - 170
        - 170
        - 170
        - 170
        - 170
      * - :igw:cvar:`sk-dmg-fuelbombgas`
        - 2000
        - 2000
        - 2000
        - 2000
        - 2000
        - 2000
      * - :igw:cvar:`sk-dmgradius-fuelbombgas`
        - 350
        - 350
        - 350
        - 350
        - 350
        - 350

   @TODO: Document the damage threshold for detonation, the delay between
   explosions, and whether upgrades are available.

.. igw:building:: poison
   :name: Poison Trap
   :related: cvar:sk-health-poison
   :stats:
      game-id: poison
      base-health: 10000
      easy-health: 10000
      medium-health: 10000
      hard-health: 10000
      brute-health: 10000
      god-health: 10000

   A canister concealed by netting and triggered by infantry pressure. It
   releases a green cloud that chokes and can kill infantry passing through
   it. The poison also slows affected targets; damage and slowdown linger
   after exposure.

   .. list-table:: Construction settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-poison`
        - 50
        - 100
        - 100
        - 100
        - 100
        - 100
      * - :igw:cvar:`sk-buildtime-poison`
        - 5000
        - 5000
        - 5000
        - 5000
        - 5000
        - 5000

   .. list-table:: Poison settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-dmg-poison1`
        - 30
        - 30
        - 30
        - 30
        - 30
        - 30
      * - :igw:cvar:`sk-dmg-poison-time`
        - 4000
        - 4000
        - 4000
        - 4000
        - 4000
        - 4000
      * - :igw:cvar:`sk-poison-speed-penalty`
        - 0.50
        - 0.50
        - 0.50
        - 0.50
        - 0.50
        - 0.50
      * - :igw:cvar:`sk-poison-life`
        - 90000
        - 90000
        - 90000
        - 90000
        - 90000
        - 90000
      * - :igw:cvar:`sk-poison-range`
        - 65
        - 65
        - 65
        - 65
        - 65
        - 65

   @TODO: Establish the damage interval, speed-penalty formula, and what the
   poison lifetime and range settings measure.

.. igw:building:: tripmine
   :name: Trip Mine
   :related: cvar:sk-health-tripmine
   :stats:
      game-id: tripmine
      base-health: 25
      easy-health: 25
      medium-health: 25
      hard-health: 25
      brute-health: 25
      god-health: 25

   An explosive bundle connected to a taut tripwire. Enemy infantry touching
   and disturbing the wire trigger an explosion that can kill or seriously
   injure nearby targets.

   .. list-table:: Construction settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-tripmine`
        - 18
        - 85
        - 85
        - 85
        - 85
        - 85
      * - :igw:cvar:`sk-buildtime-tripmine`
        - 3000
        - 3000
        - 3000
        - 3000
        - 3000
        - 3000

   .. list-table:: Explosion settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-dmg-tripmine1`
        - 750
        - 750
        - 650
        - 750
        - 750
        - 750
      * - :igw:cvar:`sk-dmg-splash-tripmine`
        - 350
        - 300
        - 300
        - 300
        - 300
        - 300

   @TODO: Document tripwire placement, trigger restrictions, and blast falloff.

.. igw:building:: supportstation
   :name: Support Station
   :related: cvar:sk-health-supportstation
   :stats:
      game-id: supportstation
      base-health: 400
      easy-health: 1500
      medium-health: 1500
      hard-health: 1500
      brute-health: 1500
      god-health: 1500

   A stockpile of ammunition and med kits. Players and allies receive
   ammunition and healing automatically while standing nearby.

   .. list-table:: Construction settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-supportstation`
        - 100
        - 150
        - 150
        - 150
        - 150
        - 150
      * - :igw:cvar:`sk-buildtime-supportstation`
        - 8000
        - 6000
        - 6000
        - 6000
        - 6000
        - 6000

   .. list-table:: Resupply settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-support-ammoadd`
        - 0.6
        - 0.6
        - 0.6
        - 0.5
        - 0.5
        - 0.5
      * - :igw:cvar:`sk-support-healthperc`
        - 0.6
        - 0.6
        - 0.4
        - 0.5
        - 0.5
        - 0.5

   @TODO: Document the resupply radius, update interval, affected ammunition,
   and how the ammunition and health settings determine the amounts supplied.

.. igw:building:: stronghold
   :name: Stronghold
   :related: cvar:sk-health-stronghold
   :stats:
      game-id: stronghold
      base-health: 2500
      easy-health: 3000
      medium-health: 3000
      hard-health: 3000
      brute-health: 3000
      god-health: 3000

   An objective whose survival sustains Atelian morale. While a stronghold
   stands, Atelian morale regenerates. Destruction lowers morale and stops
   regeneration until a stronghold is rebuilt.

   A destroyed stronghold can be rebuilt in Construction mode only at its
   original location. Move within range and select the stronghold construction
   option; with sufficient Power, the replacement snaps into position and
   construction begins.

   .. list-table:: Construction settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-cost-stronghold`
        - 150
        - 150
        - 150
        - 150
        - 150
        - 150
      * - :igw:cvar:`sk-buildtime-stronghold`
        - 20000
        - 20000
        - 20000
        - 20000
        - 20000
        - 20000

   .. list-table:: Power and morale settings
      :header-rows: 1

      * - Setting
        - Base
        - Easy
        - Medium
        - Hard
        - Brute
        - God
      * - :igw:cvar:`sk-power-stronghold`
        - 6
        - 4
        - 2
        - 2
        - 1
        - 1
      * - :igw:cvar:`sk-deadstronghold-morale`
        - 5
        - 5
        - 5
        - 5
        - 5
        - 5
      * - :igw:cvar:`sk-stronghold-morale`
        - 5
        - 5
        - 5
        - 5
        - 5
        - 5

   @TODO: Document the Power and morale formulas, their update intervals,
   rebuilding range, and behavior when a map has multiple strongholds.
