Weapons
=======

Weapons include firearms, melee weapons, explosives, and utility equipment.
There are 28 numeric weapon IDs, including utility items and Confederate
weapon variants.

``clip-size`` records the script's ``clipsize`` field. Explicit zero values
are preserved; omitted fields are not treated as zero. ``weight`` is the
priority used to select the highest-weight held weapon at spawn, not a
physical mass. ``deathmatch-points`` is the reward for killing another player
with that weapon in Deathmatch.

The difficulty tables reuse the configured ``sk_`` values from :doc:`Skill <cvars/skill>`.
The selected ``skill-*.cfg`` supplies the difficulty settings. The Base column
records separate ``skill.cfg`` assignments, not an additional difficulty or
a confirmed runtime fallback. Configured values do not establish allowed
ranges or final damage after upgrades and other modifiers. Missing assignments
are shown as ``Unspecified``.

Several ``sk_dmg_splash_*`` settings control explosion radius rather than
splash damage. The medkit's damage-named settings control healing and range.
Consult the linked CVAR entries for the meaning of each setting.

@TODO: Establish the runtime meaning of ``clipsize 0``, defaults for omitted
script fields and unassigned CVARs, and applicability to other game versions.

Using weapons
-------------

Open the Weapons & Upgrades menu with ``M`` to buy additional weapons with
Power. Select weapons with the mouse wheel, ``[`` and ``]``, or the number
keys ``1`` through ``9``. The left mouse button fires the selected weapon.
These are the default controls. The console command ``weapon N`` selects a
numeric weapon ID from the `Weapon identifiers`_ table.

The :igw:weapon:`map`, :igw:weapon:`knife`, and :igw:weapon:`toolkit` are
always held. The Atelian starting equipment also includes the
:igw:weapon:`lpistol`, :igw:weapon:`lrifle`, and :igw:weapon:`molotov`.
Weapon purchases are cleared on death. Selling a purchased weapon returns
75% of its purchase price.

The standard server shop sells the LMG, MG, shotgun, sniper rifle, 40 RTE,
flamethrower, HMG, landmines, and satchel charges. Buying satchel charges also
grants their detonator. The medkit is obtained through its upgrade.

@TODO: Establish which of the client's nine-entry and twelve-entry buy lists
the menus use. The larger list also includes hand grenades, dynamite, and the
IPE device, but their presence there does not establish server-side purchasing
support in another mode.

Secondary actions
~~~~~~~~~~~~~~~~~

The right mouse button activates the selected weapon's secondary action by
default. Secondary actions include aiming down sights, alternate attacks,
and deployment. ``secondary-action`` describes the action; ``Unknown`` means
it remains unresolved, and ``None`` means no secondary attack activity or
deployment action is defined.

The sniper rifle, musket, both LMG variants, HMG, 40 RTE, and rocket launcher
use the secondary button to deploy or undeploy. Firing the sniper rifle,
musket, or either LMG while deployed follows the secondary firing path.
This explains the aimed damage and spread settings for the player rifles
and LMG.

The HMG requires deployment and a suitable surface ahead before firing.
The 40 RTE and rocket launcher also require deployment for ordinary player
fire. Deployment is released before reloading. Movement speed was observed
to fall from 320 to 96 while deployed; this does not establish fixed speed
limits for every situation.

Reloading and ammunition
~~~~~~~~~~~~~~~~~~~~~~~~

An empty clip reloads automatically. The reload button also starts reloading
when the clip is not full. Reloading transfers only the missing rounds from
reserve ammunition. The shotgun loads individual shells and allows a shot
to interrupt reloading; the last or only shell uses its second reload
animation.

A weapon needs the corresponding primary or secondary attack activity in its
script before the firing path can run. A firing function or timing constant
alone does not prove that an attack is available. Only the knife and sword
pass the melee check that permits attacking while fully underwater.

@TODO: Document the default reload binding, weapon-specific ammunition
accounting, and the runtime relationship between script ammunition types and
reserve limits. Shared script ammunition names do not alone establish a
shared reserve pool.

Priming throwables
~~~~~~~~~~~~~~~~~~

The Molotov, dynamite, and hand grenade share a priming sequence. Pressing
primary attack starts a 1840 ms wind-up. The 4000 ms fuse begins after that
wind-up. Holding the button keeps the primed throwable in hand; releasing it
throws it. With 100 ms of fuse remaining, it is thrown automatically and can
detonate at the player's feet. The delay after throwing is 410 ms.

Firepower upgrades
~~~~~~~~~~~~~~~~~~

The highest Firepower upgrade owned sets the damage multiplier and reduces
reload time. Damage scaling is applied by the damage routine. The linked
settings provide the configured prices and multipliers:

.. list-table:: Firepower settings
   :header-rows: 1

   * - Level
     - Price
     - Damage multiplier
     - Reload-time multiplier
   * - 1
     - :igw:cvar:`sk-upgrade-fire1`
     - :igw:cvar:`sk-upgrade-weap1`
     - :igw:cvar:`sk-upgrade-reload-weap1`
   * - 2
     - :igw:cvar:`sk-upgrade-fire2`
     - :igw:cvar:`sk-upgrade-weap2`
     - :igw:cvar:`sk-upgrade-reload-weap2`
   * - 3
     - :igw:cvar:`sk-upgrade-fire3`
     - :igw:cvar:`sk-upgrade-weap3`
     - :igw:cvar:`sk-upgrade-reload-weap3`
   * - 4
     - :igw:cvar:`sk-upgrade-fire4`
     - :igw:cvar:`sk-upgrade-weap4`
     - :igw:cvar:`sk-upgrade-reload-weap4`

Deathmatch acquisition
~~~~~~~~~~~~~~~~~~~~~~

One roll per Deathmatch looter death selects a weapon, food, jewels, or no
drop. Weapon outcomes have these probabilities:

.. list-table:: Weapon drops
   :header-rows: 1

   * - Weapon
     - Probability
   * - :igw:weapon:`dynamite`
     - 20%
   * - :igw:weapon:`suicide`
     - 5%
   * - :igw:weapon:`rocketlauncher`
     - 5%
   * - :igw:weapon:`minigun`
     - 10%

Kill streaks award weapons and additional score:

.. list-table:: Kill-streak rewards
   :header-rows: 1

   * - Consecutive kills
     - Weapons
     - Additional score
   * - 2
     - :igw:weapon:`landmine`
     - 25
   * - 4
     - :igw:weapon:`satchel` and :igw:weapon:`detonator`
     - 50
   * - 6
     - :igw:weapon:`rocketlauncher`
     - 100

Comparison
----------

.. igw:statistics::
   :type: weapon
   :columns: weapon-id, clip-size, weight, secondary-action, deathmatch-points

Definitions
-----------

Timings below are weapon-code durations in milliseconds, before runtime
modifiers. ``refire-time`` is the firing delay, not a measured sustained
rate including reloads. ``wind-up-time`` precedes the attack. An explicit
code timing does not guarantee that its animation or attack is available.
Shared defaults and special movement flags are described under
`Weapon state machine`_.

.. igw:weapon:: bazooka
   :name: Confederate Bazooka
   :skill-cvars:
      sk-dmg-npc-cbazooka
      sk-dmg-splash-cbazooka
   :stats:
      weapon-id: 14
      enum-name: WP_CONF_BAZOOKA
      engine-token: CONF_BAZOOKA
      classname: weapon_bazooka
      clip-size: 1
      weight: 1
      secondary-action: None
      acquisition: Herrad weapon
      primary-ammo: AMMO_BAZOOKA
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 10730 ms

   The Confederate bazooka is carried by Herrads. It fires a rocket and is
   separate from the player-operated :igw:weapon:`rge`, despite sharing its
   first-person model and icon. Its world model, ammunition type, and firing
   function differ. No ordinary world spawner creates its weapon item.

   Its 10730 ms reload combines a 5250 ms bazooka delay with the 40 RTE's
   5480 ms delay because the reload switch falls through to that case.

.. igw:weapon:: conf-lmg
   :name: Confederate Light Machine Gun
   :related: cvar:cg-ragdoll-knockback-conf-lightmg, weapon:lmg2
   :skill-cvars:
      sk-dmg-npc-conflmg
   :stats:
      weapon-id: 13
      enum-name: WP_CONF_LIGHTMG
      engine-token: CONF_LIGHTMG
      classname: weapon_lmg2
      secondary-action: Aim down sights
      acquisition: Conscript weapon
      clip-size: 50
      weight: 4
      primary-ammo: AMMO_LIGHTMG2
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 2000 ms
      deploy-time: 240 ms
      undeploy-time: 240 ms
      refire-time: 170 ms

   A Confederate Conscript variant with its own numeric ID, firing function,
   damage setting, and 170 ms firing delay. It shares the classname and script
   of the player :igw:weapon:`lmg2`, whose firing delay is 70 ms. Half of
   non-Templar Conscripts receive this variant and half receive the musket.
   Its weapon item has no ordinary world spawner.

   @TODO: Establish how its deployed firing path selects damage and spread;
   the shared script does not establish the player LMG's secondary values
   for this variant.

.. igw:weapon:: detonator
   :name: Satchel Detonator
   :related: weapon:satchel
   :stats:
      weapon-id: 21
      enum-name: WP_DETONATOR
      engine-token: DETONATOR
      classname: weapon_detonator
      weight: 2
      secondary-action: None
      acquisition: Granted with satchel charges
      primary-ammo: AMMO_DETONATOR
      holster-time: 250 ms
      draw-time: 250 ms
      wind-up-time: 300 ms
      refire-time: 420 ms

   The satchel detonator triggers the user's placed :igw:weapon:`satchel`
   charges. It is granted with satchel purchases and the four-kill Deathmatch
   reward. Its transmission range is limited, so the user must remain close
   enough to trigger the charges. :igw:cvar:`sk-satchel-maxdist` configures
   the maximum distance, with a difficulty setting of 750.

   @TODO: Establish the distance units and exact range check.

.. igw:weapon:: dynamite
   :name: Dynamite
   :skill-cvars:
      sk-dmg-primary-dynamite
      sk-dmg-splash-dynamite
      sk-max-ammo-dynamite
      sk-max-dynamite
      sk-dynamiterespawn
      sk-dynamiterandomrespawn
      sk-dmg-npc-dynamite
      sk-npc-dynamite-splash-dmg
      sk-npc-dynamite-splash-radius
   :stats:
      weapon-id: 20
      enum-name: WP_DYNAMITE
      engine-token: DYNAMITE
      classname: weapon_dynamite
      clip-size: 0
      weight: 4
      deathmatch-points: 75
      acquisition: Map pickup or Deathmatch looter drop; not sold in the standard shop
      map-availability: Certain maps
      secondary-action: None
      primary-ammo: AMMO_DYNAMITE
      holster-time: 410 ms with ammunition; 0 ms without
      draw-time: 770 ms

   Dynamite uses a special Atelian composition for particularly strong blasts.
   It is thrown using the shared priming and fuse sequence. It cannot be
   purchased from the standard shop; players collect map pickups or loot it
   in Deathmatch. Shield-equipped Grenadiers also carry dynamite.

   @TODO: Document the exact behavior of the pickup population and respawn
   settings, which are separate from the ammunition limit.

.. igw:weapon:: fthrower
   :name: Flamethrower - Salamander Flamethrower
   :related: cvar:g-flamefueltimeout, cvar:cg-flametime
   :skill-cvars:
      sk-dmg-primary-flamer
      sk-dmg-secondary-flamer
      sk-dmg-splash-flamethrower
      sk-max-ammo-flamethrower
      sk-weapcost-flamer
      sk-dmg-npc-flamer
   :stats:
      weapon-id: 17
      enum-name: WP_FLAMETHROWER
      engine-token: FLAMETHROWER
      classname: weapon_fthrower
      clip-size: 0
      weight: 6
      deathmatch-points: 55
      documented-range: Approximately 20 feet
      secondary-action: Dispense fuel to form an ignitable puddle
      acquisition: Shop; Heavy Legionnaire weapon
      primary-ammo: AMMO_FLAMETHROWER
      secondary-ammo: AMMO_FLAMETHROWER
      holster-time: 500 ms
      draw-time: 250 ms
      wind-up-time: 200 ms
      refire-time: 150 ms

   The Salamander delivers a pressure-driven, short-range flame attack. Its
   secondary action leaves a fuel-gel puddle that can be ignited by weapon
   fire to create a trap. Both attacks specify the same ammunition type.
   Atelian warlords commonly employ the weapon, and Confederate Heavy
   Legionnaires carry it. Players can purchase it from the shop.

   Fuel persistence and flame presentation have separate controls,
   :igw:cvar:`g-flamefueltimeout` and :igw:cvar:`cg-flametime`.

   @TODO: Verify the documented reach against the game's distance units and
   document fuel persistence and flame duration.

.. igw:weapon:: grenade
   :name: Hand Grenade
   :skill-cvars:
      sk-dmg-primary-hgrenade
      sk-dmg-splash-hgrenade
      sk-max-ammo-hgrenade
      sk-dmg-npc-hgrenade
   :stats:
      weapon-id: 22
      enum-name: WP_HANDGRENADE
      engine-token: HANDGRENADE
      classname: weapon_grenade
      clip-size: 0
      weight: 2
      secondary-action: None
      acquisition: Grenadier weapon
      holster-time: 410 ms with ammunition; 0 ms without
      draw-time: 770 ms

   A standard hand grenade: prime it, then release primary attack to throw.
   It uses the shared throwable wind-up and fuse sequence. Grenadiers carrying
   the shotgun or MG also carry hand grenades. No ordinary world spawner
   creates the hand-grenade weapon item.

   The client includes a purchase-menu entry, but the standard server shop
   does not sell it. Its script omits ``primary_ammo`` despite the presence
   of ``AMMO_HANDGRENADE`` in the ammunition table.

   @TODO: Establish the effect of the omitted ammunition field and whether
   players can obtain hand grenades in another mode.

.. igw:weapon:: hmg
   :name: Heavy Machine Gun - Pratorian Heavy Machine Gun
   :related: cvar:cg-ragdoll-knockback-heavymg
   :skill-cvars:
      sk-dmg-primary-hmg
      sk-spread-primary-hmg
      sk-max-ammo-hmg
      sk-weapcost-hmg
   :stats:
      weapon-id: 10
      enum-name: WP_HEAVYMG
      engine-token: HEAVYMG
      classname: weapon_hmg
      clip-size: 250
      weight: 6
      deathmatch-points: 75
      deployment-required: Yes for ordinary player fire
      secondary-action: Deploy or undeploy
      acquisition: Shop; Walker weapon ID
      primary-ammo: AMMO_HEAVYMG
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 7250 ms
      deploy-time: 820 ms
      undeploy-time: 420 ms
      refire-time: 50 ms

   The Pratorian is a portable defensive gun designed and built in Rahmos.
   Rahmos supplied many to the AAS, and some reached Warlord Sahrab's forces.
   Players can purchase it from the shop. The Walker's weapon ID is also HMG;
   vehicle damage settings remain separate from player weapon settings.

   Firing requires deployment, which checks for a suitable surface ahead.
   Sustained fire is effective against infantry squads, while the complicated
   belt-feed system makes reloading slow.

   An unidentified player-state flag multiplies its spread by six and enables
   its view kick. @TODO: Identify the flag before attributing those effects
   to a particular stance or deployment condition.

   @TODO: Establish when crouching permits deployment and how it interacts
   with the surface check.

.. igw:weapon:: hrifle
   :name: Shotgun - Chimera Scattergun
   :related: cvar:cg-ragdoll-knockback-heavyrifle
   :skill-cvars:
      sk-dmg-primary-heavyrifle
      sk-dmg-secondary-heavyrifle
      sk-max-ammo-hrifle
      sk-max-secammo-hrifle
      sk-weapcost-shotgun
      sk-dmg-npc-heavyrifle
   :stats:
      weapon-id: 11
      enum-name: WP_HEAVYRIFLE
      engine-token: HEAVYRIFLE
      classname: weapon_hrifle
      clip-size: 8
      weight: 5
      deathmatch-points: 40
      secondary-action: Fire an incendiary burst
      acquisition: Shop; Grenadier weapon
      primary-ammo: AMMO_HEAVYRIFLE
      secondary-ammo: AMMO_HEAVYRIFLEBLAST
      holster-time: 400 ms
      draw-time: 400 ms
      reload-start-time: 820 ms
      shell-reload-time: 820 ms
      last-shell-reload-time: 2020 ms
      refire-time: 1200 ms

   The Chimera is an Atelian weapon commissioned by Warlord Sahrab during his
   rise to power. It combines a conventional shotgun attack with an incendiary
   burst of chemical fire. Primary damage is configured per pellet, not per
   shell. Secondary attack uses a separate ammunition type.

   Players can purchase it from the shop. Half of the Grenadiers without a
   shield carry it with hand grenades; the other half carry the MG. The
   help-screen name is also "Heavy Rifle".

   Reloading starts with an 820 ms delay. Individual shell reloads take 820 ms;
   the last or only shell uses a 2020 ms delay and ``ACT_RELOAD2``. Firing can
   interrupt the reload. The scripted ``clip2size 5`` is not a confirmed
   secondary magazine capacity; see `Weapon scripts`_.

.. igw:weapon:: knife
   :name: Atelian Hunting Knife
   :skill-cvars:
      sk-dmg-primary-knife
      sk-dmg-secondary-knife
   :stats:
      weapon-id: 2
      enum-name: WP_KNIFE
      engine-token: KNIFE
      classname: weapon_knife
      weight: 1
      deathmatch-points: 120
      secondary-action: Stab
      acquisition: Always held
      holster-time: 250 ms
      draw-time: 370 ms
      wind-up-time: 160 ms
      refire-time: 530 ms

   A traditional Atelian hunting tool also used for close combat. Primary
   attack swings the knife; secondary attack stabs with higher configured
   damage. It is always held and can attack underwater. Knife kills award
   more Deathmatch points than the other documented weapons.

   Spies and Deathmatch looters are given knives. @TODO: Verify whether those
   NPCs actually attack with them.

.. igw:weapon:: landmine
   :name: Landmines
   :skill-cvars:
      sk-dmg-primary-landmine
      sk-dmg-splash-landmine
      sk-max-ammo-landmine
      sk-weapcost-landmine
   :stats:
      weapon-id: 24
      enum-name: WP_LANDMINE
      engine-token: LANDMINE
      classname: weapon_landmine
      clip-size: 0
      weight: 4
      deathmatch-points: 10
      secondary-action: None
      acquisition: Shop or two-kill Deathmatch streak
      primary-ammo: AMMO_LANDMINE
      holster-time: 410 ms with ammunition; 0 ms without
      draw-time: 280 ms
      wind-up-time: 50 ms
      refire-time: 450 ms

   Defensive explosives stockpiled by Warlord Sahrab and distributed to Atelian
   soldiers. Primary attack places a mine for use against infantry or vehicles.
   Placed mines can be retrieved and repositioned using the
   :igw:weapon:`toolkit`. Players can purchase mines or earn them with a
   two-kill Deathmatch streak.

   @TODO: Document the simultaneous mine placement limit; the ammunition limit
   does not establish the number of deployed mines allowed.

.. igw:weapon:: lmg2
   :name: Light Machine Gun - Vampire Submachine Gun
   :related: cvar:cg-ragdoll-knockback-lightmg2
   :skill-cvars:
      sk-dmg-primary-lmg2
      sk-dmg-secondary-lmg2
      sk-spread-primary-lmg2
      sk-spread-secondary-lmg2
      sk-max-ammo-lmg2
      sk-weapcost-lmg
   :stats:
      weapon-id: 9
      enum-name: WP_LIGHTMG2
      engine-token: LIGHTMG2
      classname: weapon_lmg2
      clip-size: 50
      weight: 4
      deathmatch-points: 30
      secondary-action: Aim down sights
      acquisition: Shop
      primary-ammo: AMMO_LIGHTMG2
      holster-time: 440 ms
      draw-time: 440 ms
      reload-time: 2000 ms
      deploy-time: 240 ms
      undeploy-time: 240 ms
      refire-time: 70 ms

   The Vampire is a cheap, widely available weapon mass-produced for
   Confederate conscript armies. Atelians also use examples recovered from
   fallen enemies. Players can purchase it from the shop.

   Aiming down sights uses the deployed secondary firing path, increasing the
   configured damage and reducing spread. Its numeric ID is separate from the
   :igw:weapon:`conf-lmg`, which shares its script and classname.

.. igw:weapon:: lpistol
   :name: Pistol - Gamonev Autofiring Handgun
   :related: cvar:cg-ragdoll-knockback-lightpistol
   :skill-cvars:
      sk-dmg-primary-pistol
      sk-spread-primary-pistol
      sk-max-ammo-lpistol
      sk-dmg-npc-pistol
   :stats:
      weapon-id: 5
      enum-name: WP_LIGHTPISTOL
      engine-token: LIGHTPISTOL
      classname: weapon_lpistol
      clip-size: 12
      weight: 2
      deathmatch-points: 65
      secondary-action: None
      acquisition: Starting equipment; Engineer and Bomber weapon
      primary-ammo: AMMO_LIGHTPISTOL
      holster-time: 250 ms
      draw-time: 360 ms
      reload-time: 1800 ms
      wind-up-time: 200 ms
      refire-time: 250 ms

   The Gamonev is an old Kathos handgun with an ornate design and a complicated
   firing mechanism. That mechanism makes it prone to wear and poor accuracy.
   It fires bullets and is part of the player's starting equipment and every
   bot equipment set. Engineers and Bombers carry pistols; shield-equipped
   Grenadiers use the same bullet-firing function.

.. igw:weapon:: lrifle
   :name: Musket - Kham Hunting Rifle
   :skill-cvars:
      sk-dmg-primary-lrifle
      sk-dmg-secondary-lrifle
      sk-spread-primary-lrifle
      sk-spread-secondary-lrifle
      sk-max-ammo-lightrifle
      sk-dmg-npc-lrifle
   :stats:
      weapon-id: 7
      enum-name: WP_LIGHTRIFLE
      engine-token: LIGHTRIFLE
      classname: weapon_lrifle
      clip-size: 1
      weight: 3
      deathmatch-points: 35
      secondary-action: Aim down sights
      acquisition: Starting equipment; Conscript weapon
      primary-ammo: AMMO_LIGHTRIFLE
      holster-time: 200 ms
      draw-time: 770 ms
      reload-time: 3000 ms
      deploy-time: 240 ms
      undeploy-time: 240 ms
      refire-time: 840 ms
      deployed-refire-time: 420 ms

   A single-shot rifle used by nomadic tribes for centuries. This model is
   made in a small Kham factory and is carried by both allies and enemies.
   It is part of the player's starting equipment. Half of non-Templar
   Conscripts receive it with a ten-round clip, which differs from the player's
   one-round script setting.

   The player's clip reloads after each shot. Aiming down sights reduces spread
   and changes the refire delay from 840 to 420 ms, but both paths have the
   same configured damage. An aimed shot passes through undeployment before
   reloading.

.. igw:weapon:: machinegun
   :name: Machine Gun - Bretan Machine Gun
   :related: cvar:cg-ragdoll-knockback-machine-gun
   :skill-cvars:
      sk-dmg-primary-mg
      sk-dmg-secondary-mg
      sk-dmg-splash-mgnade
      sk-spread-primary-mg
      sk-max-ammo-mg
      sk-max-secammo-mg
      sk-weapcost-mg
      sk-dmg-npc-mg
   :stats:
      weapon-id: 12
      enum-name: WP_MACHINEGUN
      engine-token: MACHINE_GUN
      classname: weapon_machinegun
      clip-size: 30
      weight: 6
      deathmatch-points: 25
      secondary-action: Fire the attached grenade launcher
      acquisition: Shop; Grenadier weapon
      primary-ammo: AMMO_MACHINE_GUN
      secondary-ammo: AMMO_MGROCKET
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 3840 ms
      refire-time: 90 ms
      secondary-wind-up-time: 110 ms
      secondary-fuse-time: 2000 ms
      secondary-refire-time: 2280 ms with grenades left; 360 ms otherwise

   The Bretan is a large, cumbersome machine gun with a grenade-launcher
   attachment. Warlord Sahrab favors its close-range versatility and destructive
   effect in urban combat. Players can purchase it from the shop. Grenadiers
   without shields carry either this weapon or the shotgun, with hand grenades.

   Secondary attack launches a grenade with a 110 ms wind-up and a 2000 ms fuse.
   Its refire delay is 2280 ms while grenades remain, or 360 ms otherwise.
   The script specifies separate grenade ammunition, but ``clip2size 3`` is
   not a confirmed secondary magazine capacity; see `Weapon scripts`_.

.. igw:weapon:: map
   :name: Map
   :stats:
      weapon-id: 1
      enum-name: WP_MAP
      engine-token: MAP
      classname: weapon_map
      weight: 1
      secondary-action: None
      acquisition: Always held
      holster-time: 410 ms
      draw-time: 400 ms

   Displays the positions of friendly and enemy forces. It is always held.
   The map has no firing function and defines only idle, draw, and holster
   activities.

.. igw:weapon:: medkit
   :name: Med Kit
   :skill-cvars:
      sk-dmg-primary-medkit
      sk-dmg-splash-medkit
      sk-upgrade-medkit
   :stats:
      weapon-id: 26
      enum-name: WP_MEDKIT
      engine-token: MEDKIT
      classname: weapon_medkit
      weight: 1
      secondary-action: None
      acquisition: Med Kit upgrade
      holster-time: 250 ms
      draw-time: 250 ms
      wind-up-time: 2286 ms
      refire-time: 150 ms

   The Med Kit upgrade grants access to this item through the weapons section
   in FPS mode. It is used for healing yourself or allies. The primary action
   uses a trace to apply healing, with a 2286 ms wind-up and 150 ms refire
   delay. :igw:cvar:`sk-dmg-primary-medkit` configures the healing amount;
   :igw:cvar:`sk-dmg-splash-medkit` configures the healing range.

   @TODO: Document self-healing versus ally-targeting behavior, eligibility
   checks, and any usage costs or restrictions.

.. igw:weapon:: minigun
   :name: Minigun
   :related: cvar:cg-ragdoll-knockback-minigun
   :skill-cvars:
      sk-dmg-primary-minigun
      sk-spread-primary-minigun
      sk-max-ammo-minigun
      sk-dmg-npc-minigun
   :stats:
      weapon-id: 16
      enum-name: WP_MINIGUN
      engine-token: MINIGUN
      classname: weapon_minigun
      clip-size: 250
      weight: 6
      secondary-action: None
      acquisition: Officer death pickup, Deathmatch looter drop, or team-2 starting equipment
      primary-ammo: AMMO_HEAVYMG
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 100 ms
      refire-time: 25 ms
      secondary-refire-time: 1000 ms

   A rapid-fire bullet weapon carried by Confederate Officers alongside their
   swords. An Officer drops it on death. Players can also obtain it from a
   Deathmatch looter drop. Its script uses ``AMMO_HEAVYMG`` and a 250-round
   clip; the separate reserve setting is :igw:cvar:`sk-max-ammo-minigun`.

   The lone player allowed on team 2 (``confed`` or ``blue``) starts with the
   minigun. The script defines neither reload nor secondary attack activities,
   despite code delays of 100 ms for reload and 1000 ms for a secondary shot.

   @TODO: Establish its effective reload behavior and the purpose of the
   otherwise unavailable secondary firing delay.

.. igw:weapon:: molotov
   :name: Molotov
   :skill-cvars:
      sk-dmg-primary-molotov
      sk-dmg-splash-molotov
      sk-max-ammo-molotov
      sk-dmg-npc-molotov
   :stats:
      weapon-id: 18
      enum-name: WP_MOLOTOV
      engine-token: MOLOTOV
      classname: weapon_molotov
      clip-size: 0
      weight: 3
      deathmatch-points: 100
      secondary-action: None
      acquisition: Starting equipment
      primary-ammo: AMMO_MOLOTOV
      holster-time: 410 ms with ammunition; 0 ms without
      draw-time: 770 ms

   Improvised incendiary bombs made from glass bottles, alcohol, and a wick.
   Atelians use them to set groups of Confederate infantry on fire. They are
   part of the player's starting equipment and every bot equipment set and
   use the shared throwable priming sequence.

   No ordinary NPC class is given Molotovs. The NPC firing path permits their
   use for NPCs taken over by a player through the developer commands.

.. igw:weapon:: radio
   :name: Propaganda Radio
   :skill-cvars:
      sk-max-ammo-radio
      sk-radio-radius
      sk-radiorespawn
      sk-max-radio
   :stats:
      weapon-id: 27
      enum-name: WP_RADIO
      engine-token: RADIO
      classname: weapon_radio
      clip-size: 0
      weight: 4
      acquisition: Wave-script pickup; not purchasable
      map-availability: Certain maps
      secondary-action: None
      primary-ammo: AMMO_RADIO
      holster-time: 410 ms with ammunition; 0 ms without
      draw-time: 280 ms
      wind-up-time: 50 ms
      refire-time: 450 ms

   The radio's broadcasts make nearby Confederate troops and vehicles attack
   whichever target is nearest, often one another. Primary attack places it.
   It cannot be purchased and is among the additional weapons available in
   Scorched Earth mode. Outside Deathmatch, radios are spawned at
   ``radiospot`` positions in wave scripts.

   :igw:cvar:`sk-radio-radius` configures an effect radius of 600. Carrying
   capacity, pickup population, and respawn have separate settings.

   @TODO: Establish radius units, broadcast duration, and exact pickup
   population and respawn behavior.

.. igw:weapon:: rge
   :name: 40 RTE - "Forty"
   :skill-cvars:
      sk-dmg-primary-40rge
      sk-dmg-splash-40rge
      sk-max-ammo-40rge
      sk-weapcost-40rte
   :stats:
      weapon-id: 8
      enum-name: WP_RGE
      engine-token: RGE
      classname: weapon_rge
      clip-size: 1
      weight: 5
      deathmatch-points: 40
      secondary-action: Deploy or undeploy
      acquisition: Shop
      deployment-required: Yes for ordinary player fire
      primary-ammo: AMMO_RGE
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 5480 ms
      deploy-time: 400 ms
      undeploy-time: 280 ms
      refire-time: 860 ms

   A heavy anti-tank weapon capable of defeating strong vehicle armor. Its
   size and power make loading difficult. It fires a 40 RTE projectile and
   can also be used against infantry. Players can purchase it from the shop.

   Secondary action deploys the launcher; ordinary player fire requires it
   to be deployed. It is distinct from the Herrad's :igw:weapon:`bazooka` and
   from the single-use :igw:weapon:`rocketlauncher`.

.. igw:weapon:: rocketlauncher
   :name: Rocket Launcher
   :skill-cvars:
      sk-dmg-primary-rocketlauncher
      sk-dmg-splash-rocketlauncher
      sk-max-ammo-rocketlauncher
      sk-rocketlauncherrespawn
      sk-max-rocket
   :stats:
      weapon-id: 28
      enum-name: WP_ROCKET_LAUNCHER
      engine-token: ROCKETLAUNCHER
      classname: weapon_rocketlauncher
      clip-size: 1
      weight: 5
      deathmatch-points: 100
      acquisition: Wave-script pickup, Deathmatch looter drop, or six-kill streak
      map-availability: Certain maps
      firestorm-duration: 20 seconds
      secondary-action: Deploy or undeploy
      deployment-required: Yes for ordinary player fire
      primary-ammo: AMMO_RGE
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 5480 ms
      deploy-time: 400 ms
      undeploy-time: 280 ms
      refire-time: 860 ms

   Fires a slow-moving, powerful projectile whose explosion leaves a
   persistent firestorm. The launcher is discarded after its single shot and
   cannot be purchased. It is among the additional weapons available in
   Scorched Earth mode.

   Secondary action deploys it before ordinary player fire. Outside Deathmatch,
   it is spawned at ``rocketspot`` positions in wave scripts. Deathmatch
   players obtain it from looter drops or a six-kill streak. Its script uses
   ``AMMO_RGE``, even though ``AMMO_ROCKETLAUNCHER`` exists.

.. igw:weapon:: satchel
   :name: Satchel Charge
   :skill-cvars:
      sk-dmg-primary-satchel
      sk-dmg-splash-satchel
      sk-max-ammo-satchel
      sk-satchel-maxdist
      sk-weapcost-satchel
   :stats:
      weapon-id: 19
      enum-name: WP_SATCHEL
      engine-token: SATCHEL
      classname: weapon_satchel
      clip-size: 0
      weight: 3
      deathmatch-points: 50
      secondary-action: None
      acquisition: Shop or four-kill Deathmatch streak
      primary-ammo: AMMO_SATCHEL
      holster-time: 410 ms with ammunition; 0 ms without
      draw-time: 640 ms
      wind-up-time: 240 ms
      refire-time: 450 ms

   An explosive pack that can be thrown and placed almost anywhere. The player
   who placed it must trigger it manually and remain within the
   :igw:weapon:`detonator`'s limited signal range. Purchasing charges also
   grants the detonator. A four-kill Deathmatch streak grants both items.

   :igw:cvar:`sk-satchel-maxdist` configures maximum detonator distance.
   Primary damage and explosion radius settings vary with difficulty.

.. igw:weapon:: shield
   :name: Confederate Shield
   :stats:
      weapon-id: 23
      enum-name: WP_SHIELD
      engine-token: SHIELD
      classname: weapon_shield
      weight: 2
      secondary-action: None
      acquisition: Grenadier weapon
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 1800 ms
      refire-time: 250 ms

   The Confederate shield is used by shield-equipped Grenadiers, which also
   carry dynamite. Its primary attack calls the pistol's bullet-firing
   function and uses the pistol damage type. A separate shield death-message
   token does not establish a melee attack.

   Its weapon item has no ordinary world spawner. Its shield model is an addon;
   the first-person model is the detonator and the world model is the pistol.
   It is separate from the ``ig_meat_shield`` map object.

   @TODO: Establish its protection, the behavior of ``shieldattack``, and any
   additional attack or player-use rules.

.. igw:weapon:: sniper
   :name: Sniper Rifle - Falcon Heavy Sniper Rifle
   :related: cvar:cg-ragdoll-knockback-sniper
   :skill-cvars:
      sk-dmg-primary-sniper
      sk-dmg-secondary-sniper
      sk-spread-primary-sniper
      sk-spread-secondary-sniper
      sk-max-ammo-sniper
      sk-weapcost-sniper
   :stats:
      weapon-id: 6
      enum-name: WP_SNIPER
      engine-token: SNIPER
      classname: weapon_sniper
      clip-size: 7
      weight: 5
      deathmatch-points: 35
      secondary-action: Aim through the scope
      acquisition: Shop
      primary-ammo: AMMO_SNIPER
      holster-time: 200 ms
      draw-time: 770 ms
      reload-time: 3200 ms
      deploy-time: 240 ms
      undeploy-time: 240 ms
      refire-time: 840 ms
      deployed-refire-time: 420 ms

   The Falcon is a powerful semiautomatic rifle made in Rahmos for special
   forces. It can inflict severe damage on targets lacking a tank's heavy
   armor, and rebels carrying it attract particular attention from Confederate
   forces. Players can purchase it from the shop.

   The scope uses the deployed secondary firing path. It raises configured
   damage, sets configured spread to zero, reduces view kick, and changes the
   refire delay from 840 to 420 ms. These settings do not guarantee a kill
   against every target.

   @TODO: Identify the condition behind the "No more snipers available"
   message before documenting a sniper availability limit.

.. igw:weapon:: suicide
   :name: IPE Device - Suicide Bomb
   :skill-cvars:
      sk-dmg-primary-suicide
      sk-dmg-splash-suicide
      sk-max-suicide
      sk-suiciderespawn
      sk-suiciderandomrespawn
      sk-dmg-npc-suicide
      sk-npc-splash-suicide
   :stats:
      weapon-id: 25
      enum-name: WP_SUICIDE
      engine-token: SUICIDE_DET
      classname: weapon_suicide
      weight: 1
      deathmatch-points: 40
      acquisition: Map pickup or Deathmatch looter drop; Bomber weapon
      map-availability: Certain maps
      secondary-action: None
      holster-time: 240 ms
      draw-time: 320 ms
      wind-up-time: 3050 ms

   Also named the IPE Device, this is a self-sacrificial attack in which an
   Atelian carries strapped-on explosives into a group of enemy troops and
   detonates them. It kills the user and creates an explosion. Players obtain
   it from map pickups or Deathmatch looter drops; the standard shop does not
   sell it. Confederate Bombers also use it.

   The code specifies a 3050 ms wind-up, while the interface description
   advertises a five-second arming sequence. @TODO: Resolve how that description
   relates to the complete arming sequence and runtime modifiers.

.. igw:weapon:: sword
   :name: Sword
   :skill-cvars:
      sk-dmg-npc-sword
      sk-dmg-primary-sword
   :stats:
      weapon-id: 4
      enum-name: WP_SWORD
      engine-token: SWORD
      classname: weapon_sword
      weight: 1
      secondary-action: Unknown
      acquisition: Officer weapon
      holster-time: 250 ms
      draw-time: 370 ms
      wind-up-time: 0 ms
      refire-time: 530 ms

   A melee weapon carried by Confederate Officers alongside the
   :igw:weapon:`minigun`. It uses a melee trace and can attack underwater.
   Its first-person model is the knife; its world model is a sword.

   The script includes a secondary attack activity, but the known firing
   function is primary. :igw:cvar:`sk-dmg-primary-sword` is registered without
   an assignment in the difficulty configurations; NPC damage is separate.

   @TODO: Establish the player's effective damage and secondary attack.

.. igw:weapon:: templarmg
   :name: Templar Machine Gun
   :skill-cvars:
      sk-dmg-primary-templarmg
      sk-dmg-splash-templarmg
      sk-spread-primary-templarmg
      sk-dmg-npc-templarmgnade
   :stats:
      weapon-id: 15
      enum-name: WP_TEMPLARMG
      engine-token: TEMPLARMG
      classname: weapon_templarmg
      clip-size: 250
      weight: 6
      secondary-action: Fire the attached grenade launcher
      acquisition: Templar Conscript weapon
      primary-ammo: AMMO_MACHINE_GUN
      secondary-ammo: AMMO_MGROCKET
      holster-time: 250 ms
      draw-time: 250 ms
      reload-time: 3840 ms
      refire-time: 30 ms
      secondary-refire-time: 2000 ms

   The Templar MG is carried by the Templar share of Conscripts, selected
   by the wave's ``TEMPLAR_RATIO``. It fires bullets and has the MG's grenade
   secondary attack. Its 250-round script clip and 30 ms primary refire delay
   differ from the ordinary :igw:weapon:`machinegun`. No ordinary world spawner
   creates its weapon item.

   It shares the MG's ammunition names. Its grenade model and NPC grenade
   damage setting are distinct. ``clip2size 3`` is not a confirmed secondary
   magazine capacity.

   @TODO: Establish the effective NPC bullet damage path and secondary
   ammunition accounting. Its localization name key has no display text.

.. igw:weapon:: toolkit
   :name: Wrench
   :skill-cvars:
      sk-dmg-primary-toolkit
   :stats:
      weapon-id: 3
      enum-name: WP_TOOLKIT
      engine-token: TOOLKIT
      classname: weapon_toolkit
      weight: 1
      secondary-action: Unknown
      acquisition: Always held
      holster-time: 250 ms
      draw-time: 320 ms
      wind-up-time: 360 ms
      refire-time: 150 ms

   The Toolkit, also called the Wrench, is always held. Primary attack builds
   or repairs friendly structures. It also retrieves placed
   :igw:weapon:`mines <landmine>` for repositioning.
   :igw:cvar:`sk-dmg-primary-toolkit` configures the repair amount despite its
   damage-style name.

   The script defines a secondary attack activity whose effect remains
   unresolved. @TODO: Document that action and the requirements for building,
   repairing, and retrieving mines.

Technical reference
-------------------

Weapon identifiers
~~~~~~~~~~~~~~~~~~

Numeric IDs identify item-list weapon rows and the ``weapon N`` command.
The ``WP_*`` enum names below are descriptive reconstruction names, not
symbols preserved in the game binary. Engine tokens retain spellings such
as ``MACHINE_GUN``, ``ROCKETLAUNCHER``, and ``SUICIDE_DET``.

.. igw:statistics::
   :type: weapon
   :columns: weapon-id, enum-name, engine-token, classname
   :sort-by: weapon-id

The two ``weapon_lmg2`` rows are distinct weapon IDs with a shared script.
``WP_NUM_WEAPONS`` is 29; the ammunition and clip arrays provide
``MAX_WEAPONS = 32`` entries. Neither constant creates additional weapon
items.

Ownership for sword and higher IDs uses bit ``weapon - 4``. The map, knife,
and toolkit are treated as always owned when selecting a weapon. At spawn,
the held weapon with the highest script ``weight`` is selected.

The ownership mask is at player-state offset ``0x314``; ammunition and clip
arrays start at ``0x164`` and ``0x1e4``. An NPC's embedded player state starts
at offset ``0x10`` in its NPC data, putting its ownership mask at ``0x324``
and ammunition array at ``0x174``. These are structure offsets, not function
addresses.

Names and settings
~~~~~~~~~~~~~~~~~~

Weapon classnames come from the item list and normally select
``scripts/<classname>.txt``. Scripts are loaded during world initialization.
Localized names and descriptions use ``#weapon-name-*`` and
``#weapon-desc-*`` keys in ``scripts/languages/default.lang``. Name suffixes
need not match classnames: ``lpistol`` uses the pistol description key,
``lrifle`` uses musket naming, ``hrifle`` uses shotgun naming, and ``rge``
uses ``40rte`` naming. The sword and Templar MG name keys have no display
text. The Confederate LMG, bazooka, and shield have literal item-list names.

Skill damage CVARs are registered separately from the main game CVAR table.
Per-weapon tables associate primary and NPC damage settings with weapon IDs.
The NPC Templar entry names its grenade setting, and a registered setting
need not have an assignment in a difficulty file.

Character animation families include ``ANIM_ATTACK_*``,
``ANIM_WEAPON_IDLE_*``, ``ANIM_RELOAD_*``, and ``ANIM_DEPLOYED_*``.
Torso animation uses ``TORSO_*_IDLE``, ``TORSO_*_ATTACK``,
``TORSO_*_RELOAD``, and ``TORSO_*_DEPLOYED``. The Confederate LMG has torso
names but no corresponding ``ANIM_*`` entries. The Templar attack name is
``TORSO_WP_TEMPLARMG_ATTACK``. Script activities are a separate first-person
animation system.

Death messages use ``#mod_*`` localization keys. Client ragdoll impulse
settings use ``cg_ragdoll_knockback_<token>`` names and are linked from the
applicable weapon definitions. Ragdoll effects and weapon view kick are
separate controls.

Weapon scripts
~~~~~~~~~~~~~~

The script parser recognizes these fields:

.. list-table:: Script properties
   :header-rows: 1

   * - Field
     - Meaning
   * - ``viewmodel``
     - First-person model
   * - ``worldmodel``
     - World model
   * - ``addonmodel``
     - Additional model
   * - ``isStandard``
     - @TODO: Document its effect and accepted values.
   * - ``clipsize``
     - Configured primary clip size
   * - ``secondaryclipsize``
     - Parser key for secondary clip size
   * - ``primary_ammo`` and ``secondary_ammo``
     - Names resolved through the ammunition table
   * - ``ACT_*``
     - First-person animation activities
   * - ``event``
     - Animation event blocks, at most 31
   * - ``bucket`` and ``bucketpos``
     - Weapon-selection placement
   * - ``weaponorder``
     - Stored internally as the script value plus one
   * - ``weight``
     - Spawn-time weapon-selection priority

Activity lines use this layout:

.. code-block:: text

   ACT_<name> <first frame> <numframes> <loopingframes> <fps>

The activity names are ``IDLE``, ``DRAW``, ``HOLSTER``, ``PRIMARYATTACK``,
``SECONDARYATTACK``, ``RELOAD``, ``RELOAD2``, ``DEPLOY``, ``DEPLOYED``,
``UNDEPLOY``, ``PRIME``, and ``PRIMARYATTACK_LOOP``. The event names are
``SHOOT``, ``SHOOT2``, ``SOUND``, ``TEXTURE``, ``SWITCH``, ``PARTICLE``,
``IMPACT_DECAL``, and ``SHAKE``. These have ``ACT_`` and ``EVENT_`` prefixes
in their respective name tables.

The shotgun script writes ``clip2size 5``; the MG and Templar MG scripts
write ``clip2size 3``. The parser's recognized key is ``secondaryclipsize``.
@TODO: Establish whether ``clip2size`` is read before documenting these
numbers as effective secondary clip capacities.

Conflicting bucket placements can produce ``All weapon buckets full!``.
Shared layout values do not establish that two weapon IDs are the same.

@TODO: Document event-block syntax and arguments, activity requirements,
parser defaults, valid field values, and handling of bucket collisions.

.. list-table:: Script selection and activities
   :header-rows: 1

   * - Weapon
     - Bucket
     - Bucket position
     - Script order
     - Activities
     - Events
   * - :igw:weapon:`map`
     - 0
     - 0
     - 0
     - ``ACT_IDLE``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - ``EVENT_SOUND``
   * - :igw:weapon:`knife`
     - 0
     - 1
     - 1
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_SECONDARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - Not specified
   * - :igw:weapon:`toolkit`
     - 0
     - 2
     - 2
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_PRIMARYATTACK_LOOP``, ``ACT_SECONDARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - ``EVENT_SOUND``
   * - :igw:weapon:`sword`
     - 0
     - 4
     - 4
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_SECONDARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - Not specified
   * - :igw:weapon:`lpistol`
     - 1
     - 0
     - 4
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``, ``ACT_RELOAD``
     - Not specified
   * - :igw:weapon:`sniper`
     - 2
     - 0
     - 9
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_SECONDARYATTACK``, ``ACT_DRAW``, ``ACT_RELOAD``, ``ACT_HOLSTER``, ``ACT_DEPLOY``, ``ACT_DEPLOYED``, ``ACT_UNDEPLOY``
     - Not specified
   * - :igw:weapon:`lrifle`
     - 2
     - 1
     - 5
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_RELOAD``, ``ACT_SECONDARYATTACK``, ``ACT_HOLSTER``, ``ACT_DEPLOY``, ``ACT_DEPLOYED``, ``ACT_UNDEPLOY``
     - ``EVENT_SOUND``, ``EVENT_SWITCH``
   * - :igw:weapon:`rge`
     - 3
     - 0
     - 11
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_HOLSTER``, ``ACT_DRAW``, ``ACT_UNDEPLOY``, ``ACT_DEPLOYED``, ``ACT_DEPLOY``, ``ACT_RELOAD``
     - Not specified
   * - :igw:weapon:`lmg2`
     - 2
     - 2
     - 6
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_RELOAD``, ``ACT_SECONDARYATTACK``, ``ACT_DEPLOY``, ``ACT_DEPLOYED``, ``ACT_UNDEPLOY``, ``ACT_HOLSTER``
     - ``EVENT_SOUND``
   * - :igw:weapon:`hmg`
     - 3
     - 1
     - 12
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_RELOAD``, ``ACT_DEPLOY``, ``ACT_DEPLOYED``, ``ACT_UNDEPLOY``, ``ACT_HOLSTER``
     - ``EVENT_SOUND``, ``EVENT_SWITCH``
   * - :igw:weapon:`hrifle`
     - 2
     - 3
     - 8
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_RELOAD``, ``ACT_RELOAD2``, ``ACT_SECONDARYATTACK``, ``ACT_HOLSTER``
     - ``EVENT_SOUND``, ``EVENT_SWITCH``
   * - :igw:weapon:`machinegun`
     - 2
     - 4
     - 7
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_SECONDARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``, ``ACT_RELOAD``, ``ACT_PRIME``
     - ``EVENT_SWITCH``
   * - :igw:weapon:`bazooka`
     - 4
     - 9
     - 23
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_HOLSTER``, ``ACT_DRAW``, ``ACT_UNDEPLOY``, ``ACT_DEPLOYED``, ``ACT_DEPLOY``, ``ACT_RELOAD``
     - Not specified
   * - :igw:weapon:`templarmg`
     - 2
     - 4
     - 7
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_SECONDARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``, ``ACT_RELOAD``, ``ACT_PRIME``
     - ``EVENT_SWITCH``
   * - :igw:weapon:`minigun`
     - 3
     - 2
     - 20
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - Not specified
   * - :igw:weapon:`fthrower`
     - 3
     - 3
     - 10
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_PRIMARYATTACK_LOOP``, ``ACT_DRAW``, ``ACT_HOLSTER``, ``ACT_SECONDARYATTACK``
     - ``EVENT_SWITCH``
   * - :igw:weapon:`molotov`
     - 4
     - 0
     - 13
     - ``ACT_IDLE``, ``ACT_PRIME``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - ``EVENT_SOUND``, ``EVENT_SWITCH``
   * - :igw:weapon:`satchel`
     - 4
     - 1
     - 15
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - ``EVENT_SWITCH``
   * - :igw:weapon:`dynamite`
     - 4
     - 2
     - 14
     - ``ACT_IDLE``, ``ACT_PRIME``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - ``EVENT_SHOOT``, ``EVENT_SWITCH``
   * - :igw:weapon:`detonator`
     - 4
     - 6
     - 16
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - Not specified
   * - :igw:weapon:`grenade`
     - 4
     - 3
     - 17
     - ``ACT_IDLE``, ``ACT_PRIME``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - ``EVENT_SWITCH``
   * - :igw:weapon:`shield`
     - 4
     - 7
     - 22
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - Not specified
   * - :igw:weapon:`landmine`
     - 4
     - 4
     - 18
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - ``EVENT_SWITCH``
   * - :igw:weapon:`suicide`
     - 4
     - 5
     - 19
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - Not specified
   * - :igw:weapon:`medkit`
     - 0
     - 3
     - 21
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_PRIMARYATTACK_LOOP``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - Not specified
   * - :igw:weapon:`radio`
     - 4
     - 4
     - 18
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_DRAW``, ``ACT_HOLSTER``
     - ``EVENT_SWITCH``
   * - :igw:weapon:`rocketlauncher`
     - 3
     - 0
     - 11
     - ``ACT_IDLE``, ``ACT_PRIMARYATTACK``, ``ACT_HOLSTER``, ``ACT_DRAW``, ``ACT_UNDEPLOY``, ``ACT_DEPLOYED``, ``ACT_DEPLOY``, ``ACT_RELOAD``
     - ``EVENT_SWITCH``

The Confederate LMG shares the player LMG's script layout and activities.

Asset references
~~~~~~~~~~~~~~~~

Model and texture paths identify game assets; they do not establish attack
behavior. The Confederate LMG shares the player LMG's script model paths
and icon. Pickup and projectile models are listed where known.

:igw:weapon:`map`
   :View model: ``models/weapons/v_map.md3``
   :World model: ``models/weapons/w_map.md3``
   :Icon: ``textures/ui/weapons/weap_test``

:igw:weapon:`knife`
   :View model: ``models/weapons/v_knife.md3``
   :World model: ``models/weapons/w_knife.md3``
   :Icon: ``textures/ui/weapons/weap_knife``

:igw:weapon:`toolkit`
   :View model: ``models/weapons/v_toolkit.md3``
   :World model: ``models/weapons/w_toolkit.md3``
   :Addon model: ``models/weapons/w_toolkit1.md3``
   :Icon: ``textures/ui/weapons/weap_toolkit``

:igw:weapon:`sword`
   :View model: ``models/weapons/v_knife.md3``
   :World model: ``models/weapons/w_sword.md3``
   :Icon: ``textures/ui/weapons/weap_sword``

:igw:weapon:`lpistol`
   :View model: ``models/weapons/v_lpistol.md3``
   :World model: ``models/weapons/w_lpistol.md3``
   :Icon: ``textures/ui/weapons/weap_lpistol``

:igw:weapon:`sniper`
   :View model: ``models/weapons/v_sniper.md3``
   :World model: ``models/weapons/w_sniper.md3``
   :Icon: ``textures/ui/weapons/weap_sniper``

:igw:weapon:`lrifle`
   :View model: ``models/weapons/v_lrifle.md3``
   :World model: ``models/weapons/w_lrifle.md3``
   :Icon: ``textures/ui/weapons/weap_lrifle``

:igw:weapon:`rge`
   :View model: ``models/weapons/v_40rte.md3``
   :World model: ``models/weapons/w_40rte.md3``
   :Icon: ``textures/ui/weapons/weap_40rge``
   :Projectile models: ``models/weapons/w_40rte1.md3``, ``models/effects/40rte_Shell.md3``

:igw:weapon:`lmg2`
   :View model: ``models/weapons/v_lmg2.md3``
   :World model: ``models/weapons/w_lmg2.md3``
   :Icon: ``textures/ui/weapons/weap_lmg2``

:igw:weapon:`hmg`
   :View model: ``models/weapons/v_hmg.md3``
   :World model: ``models/weapons/w_hmg.md3``
   :Icon: ``textures/ui/weapons/weap_hmg``

:igw:weapon:`hrifle`
   :View model: ``models/weapons/v_hrifle.md3``
   :World model: ``models/weapons/w_hrifle.md3``
   :Icon: ``textures/ui/weapons/weap_hrifle``

:igw:weapon:`machinegun`
   :View model: ``models/weapons/v_mgun.md3``
   :World model: ``models/weapons/w_mgun.md3``
   :Icon: ``textures/ui/weapons/weap_mgun``
   :Projectile models: ``models/weapons/w_mgunnade.md3``

:igw:weapon:`bazooka`
   :View model: ``models/weapons/v_40rte.md3``
   :World model: ``models/weapons/w_bazooka.md3``
   :Icon: ``textures/ui/weapons/weap_40rge``
   :Projectile models: ``models/weapons/w_baznade.md3``

:igw:weapon:`templarmg`
   :View model: ``models/weapons/v_mgun.md3``
   :World model: ``models/weapons/w_templarmg.md3``
   :Icon: ``textures/ui/weapons/weap_mgun``
   :Projectile models: ``models/effects/templarmg_nade.md3``

:igw:weapon:`minigun`
   :View model: ``models/weapons/v_minigun.md3``
   :World model: ``models/weapons/w_minigun.md3``
   :Addon model: ``models/weapons/w_minigunbarrel.md3``
   :Icon: ``textures/ui/weapons/weap_minigun``
   :Pickup model: ``models/effects/minigun_pickup.md3``

:igw:weapon:`fthrower`
   :View model: ``models/weapons/v_flamethr.md3``
   :World model: ``models/weapons/w_flamethr.md3``
   :Addon model: ``models/weapons/w_flamepack.md3``
   :Icon: ``textures/ui/weapons/weap_flamethr``

:igw:weapon:`molotov`
   :View model: ``models/weapons/v_molotov.md3``
   :World model: ``models/weapons/w_molotov.md3``
   :Icon: ``textures/ui/weapons/weap_molotov``

:igw:weapon:`satchel`
   :View model: ``models/weapons/v_satchel.md3``
   :World model: ``models/weapons/w_satchel.md3``
   :Icon: ``textures/ui/weapons/weap_satchel``
   :Projectile models: ``models/effects/satchel_throw.md3``

:igw:weapon:`dynamite`
   :View model: ``models/weapons/v_clsdynamite.md3``
   :World model: ``models/weapons/w_clsdynamite.md3``
   :Icon: ``textures/ui/weapons/weap_clsdynamite``
   :Pickup model: ``models/effects/dynamite_pickup.md3``
   :Projectile models: ``models/effects/dynamite_throw.md3``, ``models/effects/dynamite_chunk.md3``

:igw:weapon:`detonator`
   :View model: ``models/weapons/v_detonator.md3``
   :World model: ``models/weapons/w_detonator.md3``
   :Icon: ``textures/ui/weapons/weap_detonator``

:igw:weapon:`grenade`
   :View model: ``models/weapons/v_molotov.md3``
   :World model: ``models/weapons/w_hgrenade.md3``
   :Icon: ``textures/ui/weapons/weap_hgrenade``

:igw:weapon:`shield`
   :View model: ``models/weapons/v_detonator.md3``
   :World model: ``models/weapons/w_lpistol.md3``
   :Addon model: ``models/weapons/w_shield.md3``
   :Icon: ``textures/ui/weapons/weap_lpistol``

:igw:weapon:`landmine`
   :View model: ``models/weapons/v_landmine.md3``
   :World model: ``models/weapons/w_landmine.md3``
   :Icon: ``textures/ui/weapons/weap_landmine``
   :Projectile models: ``models/effects/landmine.md3``

:igw:weapon:`suicide`
   :View model: ``models/weapons/v_suicide.md3``
   :World model: ``models/weapons/w_suicide.md3``
   :Addon model: ``models/weapons/w_suicidepacks.md3``
   :Icon: ``textures/ui/weapons/weap_suicide``
   :Pickup model: ``models/effects/suicide_pickup.md3``

:igw:weapon:`medkit`
   :View model: ``models/weapons/v_medkit.md3``
   :World model: ``models/weapons/w_medkit.md3``
   :Icon: ``textures/ui/weapons/weap_medkit``

:igw:weapon:`radio`
   :View model: ``models/weapons/v_radio.md3``
   :World model: ``models/weapons/w_radio.md3``
   :Icon: ``textures/ui/weapons/weap_radio``
   :Pickup model: ``models/effects/radio.md3``

:igw:weapon:`rocketlauncher`
   :View model: ``models/weapons/v_rocketlauncher.md3``
   :World model: ``models/weapons/w_bazooka.md3``
   :Icon: ``textures/ui/weapons/weap_rocketlauncher``
   :Pickup model: ``models/weapons/w_bazooka.md3``

@TODO: Document remaining pickup and projectile asset mappings.

Ammunition types
~~~~~~~~~~~~~~~~

The parser maps ``AMMO_*`` names to indices in this order. Script assignments
are recorded in each weapon definition. Absence from a script is not an
explicit assignment of ``AMMO_NONE``.

.. list-table:: Ammunition name table
   :header-rows: 1

   * - Index
     - Name
     - Notes
   * - 0
     - ``AMMO_NONE``
     - No ammunition type
   * - 1
     - ``AMMO_LIGHTMG``
     - Not used by a weapon script
   * - 2
     - ``AMMO_LIGHTPISTOL``
     - See the corresponding weapon script assignment
   * - 3
     - ``AMMO_LIGHTRIFLE``
     - See the corresponding weapon script assignment
   * - 4
     - ``AMMO_RGE``
     - 40 RTE and rocket launcher scripts
   * - 5
     - ``AMMO_FLAMETHROWER``
     - See the corresponding weapon script assignment
   * - 6
     - ``AMMO_HEAVYMG``
     - HMG and minigun scripts
   * - 7
     - ``AMMO_HEAVYRIFLE``
     - See the corresponding weapon script assignment
   * - 8
     - ``AMMO_LIGHTMG2``
     - See the corresponding weapon script assignment
   * - 9
     - ``AMMO_MACHINE_GUN``
     - MG and Templar MG scripts
   * - 10
     - ``AMMO_MOLOTOV``
     - See the corresponding weapon script assignment
   * - 11
     - ``AMMO_SATCHEL``
     - See the corresponding weapon script assignment
   * - 12
     - ``AMMO_DYNAMITE``
     - See the corresponding weapon script assignment
   * - 13
     - ``AMMO_FUELBOMB``
     - Building ammunition name
   * - 14
     - ``AMMO_TOOLKIT``
     - In the name table; omitted from the toolkit script
   * - 15
     - ``AMMO_DETONATOR``
     - See the corresponding weapon script assignment
   * - 16
     - ``AMMO_CHEMSPRAYER``
     - Unused chemical-sprayer name; no corresponding weapon item or assets
   * - 17
     - ``AMMO_HANDGRENADE``
     - In the name table; omitted from the hand-grenade script
   * - 18
     - ``AMMO_SHIELD``
     - In the name table; omitted from the shield script
   * - 19
     - ``AMMO_SNIPER``
     - See the corresponding weapon script assignment
   * - 20
     - ``AMMO_BAZOOKA``
     - See the corresponding weapon script assignment
   * - 21
     - ``AMMO_LANDMINE``
     - See the corresponding weapon script assignment
   * - 22
     - ``AMMO_MGROCKET``
     - MG and Templar MG grenade scripts
   * - 23
     - ``AMMO_HEAVYRIFLEBLAST``
     - Shotgun incendiary secondary ammunition
   * - 24
     - ``AMMO_RADIO``
     - See the corresponding weapon script assignment
   * - 25
     - ``AMMO_ROCKETLAUNCHER``
     - Not used by a weapon script; the launcher specifies AMMO_RGE

Weapon state machine
~~~~~~~~~~~~~~~~~~~~

State names from ``RELOADING`` onward are descriptive reconstruction names.
State 8 is tested by weapon code but no assignment to it has been identified.

.. list-table:: Weapon states
   :header-rows: 1

   * - Value
     - Name
     - Notes
   * - 0
     - ``READY``
     - Ready
   * - 1
     - ``RAISING``
     - Raising
   * - 2
     - ``DROPPING``
     - Dropping
   * - 3
     - ``FIRING``
     - Firing
   * - 4
     - ``RELOADING``
     - Reloading
   * - 5
     - ``DEPLOYING``
     - Plays ACT_DEPLOY, then enters state 7
   * - 6
     - ``UNDEPLOYING``
     - Plays ACT_UNDEPLOY, then returns to state 0
   * - 7
     - ``DEPLOYED``
     - Deployed movement and firing
   * - 8
     - ``STATE_8``
     - Purpose unresolved
   * - 9
     - ``FIRING_DEPLOYED``
     - Shot from state 7; secondary path for aimed rifles and LMGs
   * - 10
     - ``UNDEPLOY_TO_RELOAD``
     - Undeploys before reloading
   * - 11
     - ``RELOADING_UNDEPLOYED``
     - Reload after undeployment
   * - 12
     - ``FIRING_RELOADING``
     - Shotgun shot between shell reloads
   * - 13
     - ``RELOADING_SHELL``
     - One shotgun shell reload

Shared default code timings are 250 ms for holstering, 250 ms for drawing,
3000 ms for reloading, 820 ms for deployment, 420 ms for undeployment, and
20 ms for attack wind-up. Weapon-specific paths override these values;
code defaults do not establish omitted script-field defaults.

Two movement flags alter the normal ammunition and timing paths:

* ``pm_flags & 0x8000`` supplies 999 rounds and adds 999 ammunition per shot.
  Throwable wind-up becomes 1000 ms, fuse time 2500 ms, and the weapon delay
  after throwing 1500 ms. IPE wind-up becomes 10 ms.
* ``pm_flags & 0x10000`` prevents shots from consuming rounds and makes the
  40 RTE load three rounds per reload.

The 40 RTE and rocket launcher bypass their deployment requirement when
``pm->tracemask & 0x400000`` is set.

@TODO: Identify which actors and modes set these flags. Their presence does
not establish that an exception is specific to bots or NPCs.

View kick
~~~~~~~~~

View kick is applied in 15 ms steps over ``kickDuration``. While crouched,
its pitch and duration are halved on every movement frame, so the effect
can fade rapidly. The table records kick parameters, not final camera
displacement. Missing components are left unspecified.

.. list-table:: View-kick parameters
   :header-rows: 1

   * - Weapon
     - Path
     - Duration
     - Pitch
     - Yaw
   * - :igw:weapon:`lpistol`
     - Primary
     - 20 ms
     - 0.1
     - Unspecified
   * - :igw:weapon:`sniper`
     - Primary
     - 260 ms
     - 0.7
     - Unspecified
   * - :igw:weapon:`sniper`
     - Deployed
     - 100 ms
     - 0.2
     - Unspecified
   * - :igw:weapon:`lrifle`
     - Primary
     - 160 ms
     - 0.4
     - Unspecified
   * - :igw:weapon:`lrifle`
     - Deployed
     - 100 ms
     - 0.2
     - Unspecified
   * - :igw:weapon:`lmg2`
     - Primary
     - 40 ms
     - 0.1
     - 0.05
   * - :igw:weapon:`lmg2`
     - Deployed
     - 30 ms
     - 0.1
     - 0
   * - :igw:weapon:`hmg`
     - Primary
     - 80 ms
     - 0.1
     - 0.05
   * - :igw:weapon:`hrifle`
     - Primary
     - 40 ms
     - 0.1
     - 0.05
   * - :igw:weapon:`machinegun`
     - Primary
     - 20 ms
     - 0.03
     - Unspecified
   * - :igw:weapon:`machinegun`
     - Secondary
     - 30 ms
     - 0.1
     - Unspecified
   * - :igw:weapon:`templarmg`
     - Primary
     - 20 ms
     - 0.03
     - Unspecified
   * - :igw:weapon:`templarmg`
     - Secondary
     - 30 ms
     - 0.1
     - Unspecified
   * - :igw:weapon:`shield`
     - Primary
     - 20 ms
     - 0.1
     - Unspecified

The HMG's view kick is enabled only by unidentified bit 0 at player-state
offset ``0x340``. The same flag multiplies HMG spread by six.

@TODO: Establish the pitch and yaw units and identify the HMG flag.

Damage types and death messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Weapon IDs, ammunition indices, and ``MOD_*`` means-of-death values are
separate namespaces. Both LMG variants use ``MOD_LIGHTMG``; the MG and
Templar MG use ``MOD_MACHINE_GUN``; shield bullets use ``MOD_LIGHTPISTOL``.
A separately named damage type does not prove a distinct attack path.

.. list-table:: Weapon damage types and death messages
   :header-rows: 1

   * - Weapon
     - Damage type
     - Message key
     - Message text
   * - :igw:weapon:`knife`
     - ``MOD_KNIFE``
     - ``#mod_knife``
     - was knifed
   * - :igw:weapon:`toolkit`
     - ``MOD_TOOLKIT``
     - ``#mod_toolkit``
     - was wrenched to death
   * - :igw:weapon:`sword`
     - ``MOD_SWORD (absent from name table)``
     - ``#mod_sword``
     - was cut down
   * - :igw:weapon:`lpistol`
     - ``MOD_LIGHTPISTOL``
     - ``#mod_lightpistol``
     - was pistoled. The humanity
   * - :igw:weapon:`sniper`
     - ``MOD_SNIPER``
     - ``#mod_sniper``
     - was sniped
   * - :igw:weapon:`lrifle`
     - ``MOD_LIGHTRIFLE``
     - ``#mod_lightrifle``
     - was killed with a rifle
   * - :igw:weapon:`rge`
     - ``MOD_RGE``
     - ``#mod_rge``
     - took a RGE to the face
   * - :igw:weapon:`lmg2`
     - ``MOD_LIGHTMG``
     - ``#mod_lightmg``
     - was riddled with bullets
   * - :igw:weapon:`hmg`
     - ``MOD_HEAVYMG``
     - ``#mod_heavymg``
     - was mowed down by a HMG
   * - :igw:weapon:`hrifle`
     - ``MOD_HEAVYRIFLE``
     - ``#mod_heavyrifle``
     - was shotgunned... to death
   * - :igw:weapon:`machinegun`
     - ``MOD_MACHINE_GUN``
     - ``#mod_machinegun``
     - ate a few rounds from the MG
   * - :igw:weapon:`conf-lmg`
     - ``MOD_LIGHTMG``
     - ``#mod_lightmg``
     - was riddled with bullets
   * - :igw:weapon:`bazooka`
     - ``MOD_BAZOOKA``
     - ``#mod_bazooka``
     - saw the business end of a bazooka
   * - :igw:weapon:`templarmg`
     - ``MOD_MACHINE_GUN``
     - Not documented
     - Not documented
   * - :igw:weapon:`minigun`
     - ``MOD_MINIGUN``
     - ``#mod_minigun``
     - looks like swiss cheese now
   * - :igw:weapon:`fthrower`
     - ``MOD_FLAMETHROWER``
     - ``#mod_flamethrower``
     - was toasted like a marshmellow
   * - :igw:weapon:`molotov`
     - ``MOD_MOLOTOV``
     - ``#mod_molotov``
     - was incinerated by a molotov
   * - :igw:weapon:`satchel`
     - ``MOD_SATCHEL``
     - ``#mod_satchel``
     - confused a satchel for candy
   * - :igw:weapon:`dynamite`
     - ``MOD_DYNAMITE``
     - ``#mod_dynamite``
     - thought the dynamite was a cigar
   * - :igw:weapon:`detonator`
     - ``MOD_DETONATOR``
     - ``#mod_detonator``
     - managed to die via a button
   * - :igw:weapon:`grenade`
     - ``MOD_HANDGRENADE``
     - ``#mod_handgrenade``
     - thought a handgrenade was a pineapple
   * - :igw:weapon:`shield`
     - ``MOD_LIGHTPISTOL (bullets); separate MOD_SHIELD message``
     - ``#mod_shield``
     - was bashed in the noggin
   * - :igw:weapon:`landmine`
     - ``MOD_LANDMINE``
     - ``#mod_landmine``
     - didn't watch his step
   * - :igw:weapon:`suicide`
     - ``No distinct weapon-specific MOD identified``
     - Not documented
     - Not documented
   * - :igw:weapon:`rocketlauncher`
     - ``MOD_ROCKETLAUNCHER``
     - ``#mod_rocketlauncher``
     - couldn't dodge the rocket

Burning also uses ``MOD_BBQ`` ("was left cooked"); fuel explosions use
``MOD_FUEL`` ("stood too close to the fuel"). The fallback message is
``#mod_default`` ("was killed"). ``MOD_SUICIDE`` belongs to the console
suicide action; its name does not identify the IPE device's damage type.

The damage-name table omits the sword entry. Numeric values from
``MOD_LIGHTMG`` onward are one higher than their name-table positions.
The exact sword value among values 10 through 17 remains unresolved;
17 must not be treated as confirmed.

Other names in that interval are ``MOD_CRUSH``, ``MOD_TELEFRAG``,
``MOD_FALLING``, ``MOD_SUICIDE``, ``MOD_TARGET_LASER``, ``MOD_TRIGGER_HURT``,
and ``MOD_KNIFE``. Their name-table positions alone do not resolve the
missing sword's position.

.. list-table:: Established numeric damage types
   :header-rows: 1

   * - Value
     - Damage type
   * - 0
     - ``MOD_UNKNOWN``
   * - 1
     - ``MOD_SHOTGUN``
   * - 2
     - ``MOD_MACHINEGUN``
   * - 3
     - ``MOD_GRENADE``
   * - 4
     - ``MOD_GRENADE_SPLASH``
   * - 5
     - ``MOD_ROCKET``
   * - 6
     - ``MOD_ROCKET_SPLASH``
   * - 7
     - ``MOD_WATER``
   * - 8
     - ``MOD_SLIME``
   * - 9
     - ``MOD_LAVA``
   * - 18
     - ``MOD_LIGHTMG``
   * - 19
     - ``MOD_LIGHTPISTOL``
   * - 20
     - ``MOD_LIGHTRIFLE``
   * - 21
     - ``MOD_RGE``
   * - 22
     - ``MOD_BBQ``
   * - 23
     - ``MOD_HEAVYMG``
   * - 24
     - ``MOD_HEAVYRIFLE``
   * - 25
     - ``MOD_LIGHTMG2``
   * - 26
     - ``MOD_MACHINE_GUN``
   * - 27
     - ``MOD_MOLOTOV``
   * - 28
     - ``MOD_SATCHEL``
   * - 29
     - ``MOD_TRIPMINE``
   * - 30
     - ``MOD_DYNAMITE``
   * - 31
     - ``MOD_FUELBOMB``
   * - 32
     - ``MOD_TOOLKIT``
   * - 33
     - ``MOD_DETONATOR``
   * - 34
     - ``MOD_HANDGRENADE``
   * - 35
     - ``MOD_SHIELD``
   * - 36
     - ``MOD_SNIPER``
   * - 37
     - ``MOD_BAZOOKA``
   * - 38
     - ``MOD_LANDMINE``
   * - 39
     - ``MOD_MINIGUN``
   * - 40
     - ``MOD_VEHICLE``
   * - 41
     - ``MOD_STRONGHOLD``
   * - 42
     - ``MOD_MGTURRET``
   * - 43
     - ``MOD_POISON``
   * - 44
     - ``MOD_ONTOS``
   * - 45
     - ``MOD_MORTAR``
   * - 46
     - ``MOD_FLAMETHROWER``
   * - 47
     - ``MOD_FUEL``
   * - 48
     - ``MOD_WALKERMG``
   * - 49
     - ``MOD_MIRROR``
   * - 50
     - ``MOD_ROCKETLAUNCHER``

@TODO: Establish the individual numeric values between 10 and 17 and verify
whether ``#mod_vehiclemg`` ("was killed by a vehicle's MG") corresponds to
``MOD_WALKERMG``.

@TODO: Document the Templar MG's death-message selection and the IPE device's
effective damage type and death messages.

NPC equipment and firing
~~~~~~~~~~~~~~~~~~~~~~~~

These assignments describe weapon ownership and firing paths, not complete
enemy spawning rules. See :doc:`enemies` for the enemy reference.

.. list-table:: NPC weapon assignments
   :header-rows: 1

   * - Class
     - Weapon assignment
   * - ``CONSCRIPT``
     - Templar MG for the TEMPLAR_RATIO share; otherwise half Confederate LMG, half musket
   * - ``GRENADIER``
     - Shield and dynamite, or half shotgun and half MG, both with hand grenades
   * - ``HLEGIONNAIRE``
     - Flamethrower
   * - ``OFFICER``
     - Minigun and sword; drops the minigun on death
   * - ``WALKER``
     - HMG weapon ID; vehicle damage uses separate settings
   * - ``SPY``
     - Knife; attacking remains unverified
   * - ``ENGINEER``
     - Pistol
   * - ``BOMBER``
     - Pistol and IPE device
   * - ``CIV``
     - Knife; Deathmatch looter, attacking remains unverified
   * - ``HERRAD``
     - Confederate bazooka

The NPC firing dispatcher normally calls the weapon's firing function.
Knife, sword, dynamite, Molotov, hand grenade, IPE device, and MG or Templar
MG grenades have separate NPC firing paths. Molotov firing is restricted
to NPCs taken over by a player. NPC damage settings must therefore be kept
separate from player primary and secondary settings.

Player bots receive one of three equipment sets, selected by arguments
``0xe``, ``0xf``, or ``0x10``. Every set includes a pistol and Molotovs:

.. list-table:: Bot equipment sets
   :header-rows: 1

   * - Argument
     - Additional weapons
   * - ``0xe``
     - :igw:weapon:`machinegun`
   * - ``0xf``
     - :igw:weapon:`rge` and :igw:weapon:`hrifle`
   * - ``0x10``
     - :igw:weapon:`lmg2`

@TODO: Establish how bots select their equipment-set argument.

Developer commands let players whose names contain ``kongulu`` take over
NPCs. ``waypointx`` takes over a Confederate Officer with a minigun;
``waypointn`` takes over a Herrad and grants the MG. These paths are separate
from normal purchasing and pickups.

Shop identifiers
~~~~~~~~~~~~~~~~

The server uses nine purchase bits. The client contains a twelve-entry list
with icons and a second nine-entry name and description list. Menu visibility
remains unresolved; server purchase support is recorded below.

.. list-table:: Server shop bits
   :header-rows: 1

   * - Bit
     - Shop ID
     - Granted weapons
     - Price setting
   * - 0
     - ``lmg``
     - :igw:weapon:`lmg2`
     - :igw:cvar:`sk-weapcost-lmg`
   * - 1
     - ``mg``
     - :igw:weapon:`machinegun`
     - :igw:cvar:`sk-weapcost-mg`
   * - 2
     - ``shotgun``
     - :igw:weapon:`hrifle`
     - :igw:cvar:`sk-weapcost-shotgun`
   * - 3
     - ``sniper``
     - :igw:weapon:`sniper`
     - :igw:cvar:`sk-weapcost-sniper`
   * - 4
     - ``40rte``
     - :igw:weapon:`rge`
     - :igw:cvar:`sk-weapcost-40rte`
   * - 5
     - ``flamethrower``
     - :igw:weapon:`fthrower`
     - :igw:cvar:`sk-weapcost-flamer`
   * - 6
     - ``hmg``
     - :igw:weapon:`hmg`
     - :igw:cvar:`sk-weapcost-hmg`
   * - 7
     - ``landmine``
     - :igw:weapon:`landmine`
     - :igw:cvar:`sk-weapcost-landmine`
   * - 8
     - ``satchel``
     - :igw:weapon:`satchel`, :igw:weapon:`detonator`
     - :igw:cvar:`sk-weapcost-satchel`

The additional client-list IDs are ``suicideattack``, ``hgrenade``, and
``dynamite``. A purchase toggles its persistent weapon bit and transfers the
price from the player's money to spent Power. Applying that selection grants
the corresponding weapons. The medkit upgrade uses upgrade bit ``0x800``
and grants weapon bit ``0x400000``.

Objects outside the weapon list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Buildings, vehicle attacks, and support strikes can have ammunition names,
projectiles, or damage types without being selectable weapon items.

* Buildings include ``mgturret``, ``atturret``, ``fuelbomb``, ``tripmine``,
  ``deathhand``, ``supportstation``, and poison effects.
* Vehicle attacks include Scarab attacks, Ontos hellfire rockets, Walker MG
  and mortar attacks, and the boss Walker's doomball and mortar attacks.
* Support and artillery entities include ``airstrike``, ``bigartillery``,
  and ``mortar_grenade``.

Projectile classnames include ``dynamite``, ``machine gun grenade``,
``grenade``, ``mortar_grenade``, ``rocket``, ``hellfire_rocket``,
``Ontos rocket``, ``molotov cocktail``, ``radio``, ``satchel``,
``rocketlauncher projectile``, ``40rte rocket``, and ``flame``.
These differ from weapon item classnames such as ``weapon_dynamite``.

Unused and unresolved entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``AMMO_CHEMSPRAYER`` has no corresponding weapon item, script, model, or
damage type. No weapon script uses ``AMMO_LIGHTMG`` or
``AMMO_ROCKETLAUNCHER``. The player LMG uses ``AMMO_LIGHTMG2`` and the
rocket launcher uses ``AMMO_RGE``. No firing function has been identified
that uses ``MOD_LIGHTMG2``.

The absence of ordinary world spawners for the hand grenade, shield,
Confederate bazooka, Templar MG, and Confederate LMG item rows does not mean
those weapons are unused by NPCs. Missing localized text for the sword and
Templar MG likewise does not establish that those weapons are unused.

@TODO: Verify whether apparently unused ammunition and damage-type entries
have any remaining runtime consumers.
