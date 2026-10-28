Weapons
=======

Weapons include firearms, melee weapons, explosives, and utility equipment.

``clip-size`` records the script's ``clipsize`` field, and ``weight`` records
its ``weight`` field. These are configured values, not allowed ranges or
confirmed runtime values. ``Unknown`` in the comparison means that a value
remains undocumented. Explicit zero values are preserved.

``deathmatch-points`` is the reward for killing another player with that
weapon in Deathmatch.

@TODO: Establish the runtime meaning of ``clipsize 0``, defaults for omitted
fields, and the meaning and units of ``weight``.

@TODO: Document the remaining weapon properties, verify weapon names against
their IDs, and establish which game version these configured values apply to.

Using weapons
-------------

Open the Weapons & Upgrades menu with ``M`` to buy additional weapons with
Power. Select weapons with the mouse wheel, ``[`` and ``]``, or the number
keys ``1`` through ``9``. The left mouse button fires the selected weapon.
These are the default controls.

Secondary actions
-----------------

The right mouse button activates the selected weapon's secondary action by
default. Secondary actions include aiming down sights, alternate attacks,
and utility actions. The action depends on the weapon.

``secondary-action`` records each weapon's secondary action. ``Unknown``
marks an action that remains to be documented, including whether that weapon
has one.

Comparison
----------

.. igw:statistics::
   :type: weapon
   :columns: clip-size, weight, secondary-action, deathmatch-points

Definitions
-----------

.. igw:weapon:: bazooka
   :stats:
      clip-size: 1
      weight: 1
      secondary-action: Unknown

   @TODO: Identify this weapon, including its relationship to
   :igw:weapon:`rge`.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: detonator
   :stats:
      weight: 2
      secondary-action: Unknown

   A satchel charge is triggered by the person who placed it. The detonator's
   transmission range is limited, so the user must remain close enough to
   trigger the charge.

   @TODO: Verify that this weapon ID is the :igw:weapon:`satchel` detonator
   and establish its transmission range.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: dynamite
   :name: Dynamite
   :stats:
      clip-size: 0
      weight: 4
      deathmatch-points: 75
      acquisition: Map pickup; not purchasable
      map-availability: Specific locations on all maps
      secondary-action: Unknown

   Dynamite uses a special Atelian composition for particularly strong blasts.
   It cannot be purchased and is collected at designated locations on maps.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: fthrower
   :name: Flamethrower - Salamander Flamethrower
   :stats:
      clip-size: 0
      weight: 6
      deathmatch-points: 55
      documented-range: Approximately 20 feet
      secondary-action: Dispense fuel to form an ignitable puddle

   The Salamander delivers a pressure-driven, short-range flame attack. Its
   secondary action leaves a puddle that can be ignited to create a trap.
   Atelian warlords commonly employ the weapon.

   @TODO: Verify the documented reach against the game's distance units.

.. igw:weapon:: grenade
   :stats:
      clip-size: 0
      weight: 2
      secondary-action: Unknown

   @TODO: Document this weapon's attacks and usage.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: hmg
   :name: Heavy Machine Gun - Pratorian Heavy Machine Gun
   :stats:
      clip-size: 250
      weight: 6
      deathmatch-points: 75
      deployment-required: Yes
      secondary-action: Unknown

   The Pratorian is a portable defensive gun designed and built in Rahmos.
   Rahmos supplied many to the AAS, and some reached Warlord Sahrab's forces.

   Recoil requires deployment before firing. The bipod can be supported on a
   suitable flat surface or deployed while crouching. Sustained fire is
   effective against infantry squads, while the complicated belt-feed system
   makes reloading slow.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: hrifle
   :name: Shotgun - Chimera Scattergun
   :stats:
      clip-size: 8
      weight: 5
      deathmatch-points: 40
      secondary-action: Fire an incendiary burst

   The Chimera is an Atelian weapon commissioned by Warlord Sahrab during his
   rise to power. It combines a conventional shotgun attack with an incendiary
   burst of chemical fire.

.. igw:weapon:: knife
   :name: Atelian Hunting Knife
   :stats:
      weight: 1
      deathmatch-points: 120
      secondary-action: Stab

   A traditional Atelian hunting tool also used for close combat.

.. igw:weapon:: landmine
   :name: Landmines
   :stats:
      clip-size: 0
      weight: 4
      deathmatch-points: 10
      secondary-action: Unknown

   Defensive explosives stockpiled by Warlord Sahrab and distributed to Atelian
   soldiers. Placed mines can be retrieved and repositioned using the
   :igw:weapon:`toolkit`.

   @TODO: Document the simultaneous mine placement limit.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: lmg2
   :name: Light Machine Gun - Vampire Submachine Gun
   :stats:
      clip-size: 50
      weight: 4
      deathmatch-points: 30
      secondary-action: Aim down sights

   The Vampire is a cheap, widely available weapon mass-produced for
   Confederate conscript armies. Atelians also use examples recovered from
   fallen enemies.

.. igw:weapon:: lpistol
   :name: Pistol - Gamonev Autofiring Handgun
   :stats:
      clip-size: 12
      weight: 2
      deathmatch-points: 65
      secondary-action: Unknown

   The Gamonev is an old Kathos handgun with an ornate design and a complicated
   firing mechanism. That mechanism makes it prone to wear and poor accuracy.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: lrifle
   :name: Musket - Kham Hunting Rifle
   :stats:
      clip-size: 1
      weight: 3
      deathmatch-points: 35
      secondary-action: Aim down sights

   A single-shot rifle used by nomadic tribes for centuries. This model is
   made in a small Kham factory and is carried by both allies and enemies.

.. igw:weapon:: machinegun
   :name: Machine Gun - Bretan Machine Gun
   :stats:
      clip-size: 30
      weight: 6
      deathmatch-points: 25
      secondary-action: Fire the attached grenade launcher

   The Bretan is a large, cumbersome machine gun with a grenade-launcher
   attachment.
   Warlord Sahrab favors its close-range versatility and destructive effect in
   urban combat.

.. igw:weapon:: map
   :stats:
      weight: 1
      secondary-action: Unknown

   @TODO: Document this item's purpose and usage.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: medkit
   :name: Med Kit
   :stats:
      weight: 1
      secondary-action: Unknown

   The Med Kit upgrade grants access to this item through the weapons section
   in FPS mode.

   @TODO: Document the Med Kit's effects and usage requirements.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: minigun
   :stats:
      clip-size: 250
      weight: 6
      secondary-action: Unknown

   @TODO: Document this weapon's attacks and usage.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: molotov
   :name: Molotov
   :stats:
      clip-size: 0
      weight: 3
      deathmatch-points: 100
      secondary-action: Unknown

   Improvised incendiary bombs made from glass bottles, alcohol, and a wick.
   Atelians use them to set groups of Confederate infantry on fire.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: radio
   :name: Propaganda Radio
   :stats:
      clip-size: 0
      weight: 4
      acquisition: Map pickup; not purchasable
      map-availability: Certain maps
      secondary-action: Unknown

   The radio's broadcasts make nearby Confederate troops and vehicles attack
   whichever target is nearest, often one another. It cannot be purchased and
   is among the additional weapons available in Scorched Earth mode.

   @TODO: Establish the broadcast effect's radius and duration.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: rge
   :name: 40 RTE - "Forty"
   :stats:
      clip-size: 1
      weight: 5
      deathmatch-points: 40
      secondary-action: Unknown

   A heavy anti-tank weapon capable of defeating strong vehicle armor. Its
   size and power make loading difficult.

   @TODO: Verify the 40 RTE name against this weapon ID and establish its
   relationship to :igw:weapon:`bazooka`.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: rocketlauncher
   :name: Rocket Launcher
   :stats:
      clip-size: 1
      weight: 5
      deathmatch-points: 100
      acquisition: Map pickup; not purchasable
      map-availability: Certain maps
      firestorm-duration: 20 seconds
      secondary-action: Unknown

   Fires a slow-moving, powerful projectile whose explosion leaves a
   persistent firestorm. The launcher is discarded after its single shot and
   cannot be purchased. It is among the additional weapons available in
   Scorched Earth mode.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: satchel
   :name: Satchel Charge
   :stats:
      clip-size: 0
      weight: 3
      deathmatch-points: 50
      secondary-action: Unknown

   An explosive pack that can be placed almost anywhere. The player who
   placed it must trigger it manually and remain within the
   :igw:weapon:`detonator`'s limited signal range.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: shield
   :stats:
      weight: 2
      secondary-action: Unknown

   @TODO: Document this item's protection and usage.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: sniper
   :name: Sniper Rifle - Falcon Heavy Sniper Rifle
   :stats:
      clip-size: 7
      weight: 5
      deathmatch-points: 35
      secondary-action: Aim through the scope

   The Falcon is a powerful semiautomatic rifle made in Rahmos for special
   forces. It can inflict severe damage on targets lacking a tank's heavy
   armor, and rebels carrying it attract particular attention from Confederate
   forces.

.. igw:weapon:: suicide
   :name: Suicide Bomb
   :stats:
      weight: 1
      deathmatch-points: 40
      acquisition: Map pickup; not purchasable
      map-availability: Certain maps
      secondary-action: Unknown

   A self-sacrificial attack in which an Atelian carries strapped-on explosives
   into a group of enemy troops and detonates them. It cannot be purchased.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: sword
   :stats:
      weight: 1
      secondary-action: Unknown

   @TODO: Document this weapon's attacks and usage.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: templarmg
   :stats:
      clip-size: 250
      weight: 6
      secondary-action: Unknown

   @TODO: Document this weapon's attacks and usage.

   @TODO: Document this weapon's secondary action, if available.

.. igw:weapon:: toolkit
   :name: Wrench
   :stats:
      weight: 1
      secondary-action: Unknown

   A tool for repairing damaged structures and retrieving placed
   :igw:weapon:`mines <landmine>` for repositioning.

   @TODO: Verify the Wrench name against the ``toolkit`` weapon ID.

   @TODO: Document this weapon's secondary action, if available.
