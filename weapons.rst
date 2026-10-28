Weapons
=======

These definitions combine the supplied ``base/scripts/weapon_*.txt`` files
with the *Iron Grip: Warlord Game Manual*, version 2.4 (2012-03-23), transcribed
in ``Iron_Grip_Warlord_Manual.rst``. The weapon ID is the script filename with
``weapon_`` and ``.txt`` removed: ``weapon_bazooka.txt`` defines ``bazooka``.

``clip-size`` records the script's ``clipsize`` field, and ``weight`` records
its ``weight`` field. Values are copied as written. ``Unknown`` in the
comparison means a field is absent from the cited sources. Explicit zero
values are preserved.

Names, descriptions, and Deathmatch points below are attributed to the manual
sections cited with each entry. ``deathmatch-points`` is the reward for
killing another player with that weapon in Deathmatch. The manual's version
number identifies the publication; the supplied scripts' game version remains
unverified.

@TODO: Establish the runtime meaning of ``clipsize 0``, defaults for omitted
fields, and the meaning and units of ``weight``.

@TODO: Add remaining weapon information from other sources, verify
manual-to-script ID mappings against the game code, and establish which game
version these script values apply to.

Using weapons
-------------

The manual's ``Arsenal`` and ``Basic Gameplay / FPS & Construction Mode``
sections describe opening the Weapons & Upgrades menu with ``M`` and buying
additional weapons with Power. Weapons can be selected with the mouse wheel,
``[`` and ``]``, or the number keys ``1`` through ``9``. The left mouse button
fires the selected weapon. These are the manual's default controls.

Comparison
----------

.. igw:statistics::
   :type: weapon
   :columns: clip-size, weight, deathmatch-points

Definitions
-----------

.. igw:weapon:: bazooka
   :stats:
      clip-size: 1
      weight: 1

   Source: ``base/scripts/weapon_bazooka.txt``.

   @TODO: Identify this weapon's manual counterpart, including its relationship
   to :igw:weapon:`rge`. Both scripts reference a 40 RTE view model.

.. igw:weapon:: detonator
   :stats:
      weight: 2

   Source: ``base/scripts/weapon_detonator.txt``.

   The manual's ``Arsenal / Satchel Charge`` entry describes a detonator used
   by the person who placed the :igw:weapon:`satchel`. Its transmission range
   is limited, so the user must remain close enough to trigger the charge.

   @TODO: Verify that this script ID is the satchel detonator described in the
   manual and establish its transmission range.

.. igw:weapon:: dynamite
   :name: Dynamite
   :stats:
      clip-size: 0
      weight: 4
      deathmatch-points: 75
      acquisition: Map pickup; not purchasable
      map-availability: Specific locations on all maps

   Source: ``base/scripts/weapon_dynamite.txt``.

   The manual's ``Arsenal / Dynamite`` entry describes explosives made with a
   special Atelian composition for particularly strong blasts. Dynamite cannot
   be purchased and is collected at designated locations on maps.

.. igw:weapon:: fthrower
   :name: Flamethrower - Salamander Flamethrower
   :stats:
      clip-size: 0
      weight: 6
      deathmatch-points: 55
      documented-range: Approximately 20 feet

   Source: ``base/scripts/weapon_fthrower.txt``.

   The manual's ``Arsenal / Flamethrower - Salamander Flamethrower`` entry
   describes a pressure-driven, short-range flame attack. An alternative
   attack leaves a puddle that can be ignited to create a trap. Atelian
   warlords commonly employ the weapon.

   @TODO: Verify the documented reach against the game's distance units.

.. igw:weapon:: grenade
   :stats:
      clip-size: 0
      weight: 2

   Source: ``base/scripts/weapon_grenade.txt``.

.. igw:weapon:: hmg
   :name: Heavy Machine Gun - Pratorian Heavy Machine Gun
   :stats:
      clip-size: 250
      weight: 6
      deathmatch-points: 75
      deployment-required: Yes

   Source: ``base/scripts/weapon_hmg.txt``.

   The manual's ``Arsenal / Heavy Machine Gun - Pratorian Heavy Machine Gun``
   entry describes a portable defensive gun designed and built in Rahmos.
   Rahmos supplied many to the AAS, and some reached Warlord Sahrab's forces.

   Recoil requires deployment before firing. The bipod can be supported on a
   suitable flat surface or deployed while crouching. Sustained fire is
   effective against infantry squads, while the complicated belt-feed system
   makes reloading slow.

.. igw:weapon:: hrifle
   :name: Shotgun - Chimera Scattergun
   :stats:
      clip-size: 8
      weight: 5
      deathmatch-points: 40

   Source: ``base/scripts/weapon_hrifle.txt``.

   The manual's ``Arsenal / Shotgun - Chimera Scattergun`` entry describes an
   Atelian weapon commissioned by Warlord Sahrab during his rise to power.
   It combines a conventional shotgun attack with an incendiary burst of
   chemical fire.

.. igw:weapon:: knife
   :name: Atelian Hunting Knife
   :stats:
      weight: 1
      deathmatch-points: 120

   Source: ``base/scripts/weapon_knife.txt``.

   The manual's ``Arsenal / Atelian Hunting Knife`` entry describes a
   traditional Atelian hunting tool also used for close combat.

.. igw:weapon:: landmine
   :name: Landmines
   :stats:
      clip-size: 0
      weight: 4
      deathmatch-points: 10

   Source: ``base/scripts/weapon_landmine.txt``.

   The manual's ``Arsenal / Landmines`` entry describes defensive explosives
   stockpiled by Warlord Sahrab and distributed to Atelian soldiers. The
   ``Arsenal / Wrench`` entry explains that placed mines can be retrieved and
   repositioned using the :igw:weapon:`toolkit`.

   @TODO: Establish the simultaneous mine placement limit mentioned by the
   manual.

.. igw:weapon:: lmg2
   :name: Light Machine Gun - Vampire Submachine Gun
   :stats:
      clip-size: 50
      weight: 4
      deathmatch-points: 30

   Source: ``base/scripts/weapon_lmg2.txt``.

   The manual's ``Arsenal / Light Machine Gun - Vampire Submachine Gun`` entry
   describes a cheap, widely available weapon mass-produced for Confederate
   conscript armies. Atelians also use examples recovered from fallen enemies.

.. igw:weapon:: lpistol
   :name: Pistol - Gamonev Autofiring Handgun
   :stats:
      clip-size: 12
      weight: 2
      deathmatch-points: 65

   Source: ``base/scripts/weapon_lpistol.txt``.

   The manual's ``Arsenal / Pistol - Gamonev Autofiring Handgun`` entry
   describes an old Kathos handgun with an ornate design and a complicated
   firing mechanism. That mechanism makes it prone to wear and poor accuracy.

.. igw:weapon:: lrifle
   :name: Musket - Kham Hunting Rifle
   :stats:
      clip-size: 1
      weight: 3
      deathmatch-points: 35

   Source: ``base/scripts/weapon_lrifle.txt``.

   The manual's ``Arsenal / Musket - Kham Hunting Rifle`` entry describes a
   single-shot rifle used by nomadic tribes for centuries. This model is made
   in a small Kham factory and is carried by both allies and enemies.

.. igw:weapon:: machinegun
   :name: Machine Gun - Bretan Machine Gun
   :stats:
      clip-size: 30
      weight: 6
      deathmatch-points: 25

   Source: ``base/scripts/weapon_machinegun.txt``.

   The manual's ``Arsenal / Machine Gun - Bretan Machine Gun`` entry describes
   a large, cumbersome machine gun with a grenade-launcher attachment.
   Warlord Sahrab favors its close-range versatility and destructive effect in
   urban combat.

.. igw:weapon:: map
   :stats:
      weight: 1

   Source: ``base/scripts/weapon_map.txt``.

.. igw:weapon:: medkit
   :name: Med Kit
   :stats:
      weight: 1

   Source: ``base/scripts/weapon_medkit.txt``.

   The manual's ``Character Upgrades / Med Kit`` entry says that the upgrade
   grants access to the Med Kit through the weapons section in FPS mode.

   @TODO: Document the Med Kit's effects and usage requirements; this manual
   entry only explains how access is granted.

.. igw:weapon:: minigun
   :stats:
      clip-size: 250
      weight: 6

   Source: ``base/scripts/weapon_minigun.txt``.

.. igw:weapon:: molotov
   :name: Molotov
   :stats:
      clip-size: 0
      weight: 3
      deathmatch-points: 100

   Source: ``base/scripts/weapon_molotov.txt``.

   The manual's ``Arsenal / Molotov`` entry describes improvised incendiary
   bombs made from glass bottles, alcohol, and a wick. Atelians use them to
   set groups of Confederate infantry on fire.

.. igw:weapon:: radio
   :name: Propaganda Radio
   :stats:
      clip-size: 0
      weight: 4
      acquisition: Map pickup; not purchasable
      map-availability: Certain maps

   Source: ``base/scripts/weapon_radio.txt``.

   The manual's ``Arsenal / Propaganda Radio`` entry says its broadcasts make
   nearby Confederate troops and vehicles attack whichever target is nearest,
   often one another. It cannot be purchased. ``Game Modes / Scorched Earth
   Mode`` lists it among that mode's additional weapons.

   @TODO: Establish the broadcast effect's radius and duration.

.. igw:weapon:: rge
   :name: 40 RTE - "Forty"
   :stats:
      clip-size: 1
      weight: 5
      deathmatch-points: 40

   Source: ``base/scripts/weapon_rge.txt``.

   The manual's ``Arsenal / 40 RTE - "Forty"`` entry describes a heavy
   anti-tank weapon capable of defeating strong vehicle armor. Its size and
   power make loading difficult.

   @TODO: Confirm this manual-to-script match against the game code. The
   ``rge`` script names a 40 RTE world model, while :igw:weapon:`bazooka` also
   references a 40 RTE view model.

.. igw:weapon:: rocketlauncher
   :name: Rocket Launcher
   :stats:
      clip-size: 1
      weight: 5
      deathmatch-points: 100
      acquisition: Map pickup; not purchasable
      map-availability: Certain maps
      firestorm-duration: 20 seconds

   Source: ``base/scripts/weapon_rocketlauncher.txt``.

   The manual's ``Arsenal / Rocket Launcher`` entry describes a slow-moving,
   powerful projectile whose explosion leaves a persistent firestorm. The
   launcher is discarded after its single shot and cannot be purchased.
   ``Game Modes / Scorched Earth Mode`` lists it among that mode's additional
   weapons.

.. igw:weapon:: satchel
   :name: Satchel Charge
   :stats:
      clip-size: 0
      weight: 3
      deathmatch-points: 50

   Source: ``base/scripts/weapon_satchel.txt``.

   The manual's ``Arsenal / Satchel Charge`` entry describes an explosive pack
   that can be placed almost anywhere. The player who placed it must trigger
   it manually and remain within the :igw:weapon:`detonator`'s limited signal
   range.

.. igw:weapon:: shield
   :stats:
      weight: 2

   Source: ``base/scripts/weapon_shield.txt``.

.. igw:weapon:: sniper
   :name: Sniper Rifle - Falcon Heavy Sniper Rifle
   :stats:
      clip-size: 7
      weight: 5
      deathmatch-points: 35

   Source: ``base/scripts/weapon_sniper.txt``.

   The manual's ``Arsenal / Sniper Rifle - Falcon Heavy Sniper Rifle`` entry
   describes a powerful semiautomatic rifle made in Rahmos for special forces.
   It can inflict severe damage on targets lacking a tank's heavy armor, and
   rebels carrying it attract particular attention from Confederate forces.

.. igw:weapon:: suicide
   :name: Suicide Bomb
   :stats:
      weight: 1
      deathmatch-points: 40
      acquisition: Map pickup; not purchasable
      map-availability: Certain maps

   Source: ``base/scripts/weapon_suicide.txt``.

   The manual's ``Arsenal / Suicide Bomb`` entry describes a self-sacrificial
   attack in which an Atelian carries strapped-on explosives into a group of
   enemy troops and detonates them. It cannot be purchased.

.. igw:weapon:: sword
   :stats:
      weight: 1

   Source: ``base/scripts/weapon_sword.txt``.

.. igw:weapon:: templarmg
   :stats:
      clip-size: 250
      weight: 6

   Source: ``base/scripts/weapon_templarmg.txt``.

.. igw:weapon:: toolkit
   :name: Wrench
   :stats:
      weight: 1

   Source: ``base/scripts/weapon_toolkit.txt``.

   The manual's ``Arsenal / Wrench`` entry describes a tool for repairing
   damaged structures and retrieving placed :igw:weapon:`mines <landmine>`
   for repositioning. It also notes a limit on simultaneously deployed mines
   without giving the number.

   @TODO: Verify the manual's Wrench name against the ``toolkit`` script ID.
