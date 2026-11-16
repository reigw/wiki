Upgrades
========

Player upgrades improve health, weapon damage, reload time, repairs,
movement, or respawning, or grant access to the medkit. There are twelve
player upgrades. Structure upgrades are documented under :doc:`buildings`.

Buying and selling
------------------

Open the Weapons & Upgrades menu with ``M`` by default. Purchases cost
Power and apply their effects immediately. Health and Firepower each have
four levels: the preceding level must already be owned before buying the
next. Each level has its own purchase price, so reaching a higher level
requires paying for the earlier levels as well.

Selling returns 75% of the upgrade's current configured price, rounded
down to whole Power. A single-upgrade sale can also sell other upgrades:

* Selling a Health upgrade sells higher owned Health levels and
  :igw:upgrade:`firepower1`, if owned.
* Selling a Firepower upgrade sells higher owned Firepower levels and
  :igw:upgrade:`brute`, if owned.

A new round clears purchased upgrades.

@TODO: Verify upgrade retention through death, respawning, and class
selection, including the effects of menu selections made while dead.

Difficulty settings
-------------------

The tables reuse the configured values from :doc:`cvars/skill`. Prices are
in Power, maximum-health settings are in health points, and damage and
reload-time settings are multipliers. Regeneration intervals and respawn
delays are in milliseconds.

Base records the separate ``skill.cfg`` assignments. It is not an
additional difficulty or a confirmed runtime fallback. Missing assignments
are shown as ``Unspecified``. Configured values do not establish allowed
ranges, and :doc:`wave scripts <scripts/waves>` can override skill settings.

Health upgrades
---------------

``sk_upgrade_healthN`` is the purchase price in Power for Health Upgrade N.
``sk_upgrade_newhealthN`` is the resulting maximum health in health points.
For example, :igw:cvar:`sk-upgrade-health4` prices
:igw:upgrade:`health4`, while :igw:cvar:`sk-upgrade-newhealth4` sets its
maximum health.

The highest owned Health level sets maximum health to its
``sk_upgrade_newhealthN`` value. These settings are absolute maximums;
lower levels are not added to them. Buying a Health upgrade increases the
maximum without filling the additional health. Food, support stations,
and healing can restore health up to the new maximum.

Without a Health upgrade, a human player's maximum health is set by
:igw:cvar:`sk-health-player`; militia bots use :igw:cvar:`sk-health-militia`.

.. igw:upgrade:: health1
   :name: Health Upgrade 1
   :summary: First level of increased maximum health.
   :skill-cvars:
      sk-upgrade-health1
      sk-upgrade-newhealth1
   :stats:
      upgrade-id: 0
      bit-mask: 0x001

   No prerequisite upgrade.

.. igw:upgrade:: health2
   :name: Health Upgrade 2
   :summary: Second level of increased maximum health.
   :related: upgrade:health1
   :skill-cvars:
      sk-upgrade-health2
      sk-upgrade-newhealth2
   :stats:
      upgrade-id: 1
      bit-mask: 0x002

   Requires :igw:upgrade:`health1`.

.. igw:upgrade:: health3
   :name: Health Upgrade 3
   :summary: Third level of increased maximum health.
   :related: upgrade:health2
   :skill-cvars:
      sk-upgrade-health3
      sk-upgrade-newhealth3
   :stats:
      upgrade-id: 2
      bit-mask: 0x004

   Requires :igw:upgrade:`health2`.

.. igw:upgrade:: health4
   :name: Health Upgrade 4
   :summary: Fourth level of increased maximum health.
   :related: upgrade:health3
   :skill-cvars:
      sk-upgrade-health4
      sk-upgrade-newhealth4
   :stats:
      upgrade-id: 3
      bit-mask: 0x008

   Requires :igw:upgrade:`health3`.

Firepower upgrades
------------------

The highest owned Firepower level selects a damage multiplier from
``sk_upgrade_weapN`` and a reload-time multiplier from
``sk_upgrade_reload_weapN``. Lower levels do not multiply together. Damage
scaling is applied by the damage routine; reload scaling applies to the
weapon's reload delay. See :doc:`weapons` for weapon-specific reload rules.

``sk_upgrade_fireN`` is the purchase price. It does not set the weapon's
rate of fire.

@TODO: Verify any effect of Firepower on construction or structure-upgrade
speed.

.. igw:upgrade:: firepower1
   :name: Firepower Upgrade 1
   :summary: First level of increased damage and faster reloading.
   :skill-cvars:
      sk-upgrade-fire1
      sk-upgrade-weap1
      sk-upgrade-reload-weap1
   :stats:
      upgrade-id: 4
      bit-mask: 0x010

   No prerequisite upgrade.

.. igw:upgrade:: firepower2
   :name: Firepower Upgrade 2
   :summary: Second level of increased damage and faster reloading.
   :related: upgrade:firepower1
   :skill-cvars:
      sk-upgrade-fire2
      sk-upgrade-weap2
      sk-upgrade-reload-weap2
   :stats:
      upgrade-id: 5
      bit-mask: 0x020

   Requires :igw:upgrade:`firepower1`.

.. igw:upgrade:: firepower3
   :name: Firepower Upgrade 3
   :summary: Third level of increased damage and faster reloading.
   :related: upgrade:firepower2
   :skill-cvars:
      sk-upgrade-fire3
      sk-upgrade-weap3
      sk-upgrade-reload-weap3
   :stats:
      upgrade-id: 6
      bit-mask: 0x040

   Requires :igw:upgrade:`firepower2`.

.. igw:upgrade:: firepower4
   :name: Firepower Upgrade 4
   :summary: Fourth level of increased damage and faster reloading.
   :related: upgrade:firepower3
   :skill-cvars:
      sk-upgrade-fire4
      sk-upgrade-weap4
      sk-upgrade-reload-weap4
   :stats:
      upgrade-id: 7
      bit-mask: 0x080

   Requires :igw:upgrade:`firepower3`.

Player enhancements
-------------------

These four upgrades have no prerequisite upgrades.

.. igw:upgrade:: brute
   :name: Brute
   :summary: Regenerates health and doubles the toolkit's repair amount.
   :related: weapon:toolkit
   :skill-cvars:
      sk-upgrade-brute
      sk-brute-rate
   :stats:
      upgrade-id: 8
      bit-mask: 0x100

   Regenerates 1% of maximum health per pulse, rounded down to whole health
   points, while below maximum health. Healing is capped at that maximum.
   :igw:cvar:`sk-brute-rate` sets the interval between pulses in milliseconds.
   Regeneration scales with upgraded maximum health, subject to this rounding.

   With the :igw:weapon:`toolkit`, Brute doubles the repair amount configured
   by :igw:cvar:`sk-dmg-primary-toolkit` for each repair action. This applies
   to structure and stronghold repairs.

.. igw:upgrade:: spawning
   :name: Spawning
   :summary: Uses a separate respawn delay during an active round.
   :skill-cvars:
      sk-upgrade-spawning
      sk-upgrade-spawn
      sk-spawntime
   :stats:
      upgrade-id: 9
      bit-mask: 0x200

   During an active round, dying with this upgrade sets the respawn delay
   to :igw:cvar:`sk-upgrade-spawn` instead of :igw:cvar:`sk-spawntime`.
   Both delays are in milliseconds. ``sk_upgrade_spawning`` is the purchase
   price; ``sk_upgrade_spawn`` is the replacement delay.

   @TODO: Document mode-specific respawn rules and how class and spawn-point
   selection affect the time at which the player actually returns.

.. igw:upgrade:: adrenaline
   :name: Adrenaline
   :summary: Increases movement speed by 10%.
   :related: cvar:g-speed
   :skill-cvars:
      sk-upgrade-adren
   :stats:
      upgrade-id: 10
      bit-mask: 0x400
      movement-speed-multiplier: 1.1

   Multiplies movement speed by 1.1. The calculation starts from
   :igw:cvar:`g-speed`; bot movement scaling is applied before Adrenaline,
   and poison and weapon-deployment penalties are applied afterward.
   Speed is stored as an integer, so fractional results are truncated.

.. igw:upgrade:: medkit
   :name: Medkit
   :summary: Grants access to the medkit equipment.
   :related: weapon:medkit
   :skill-cvars:
      sk-upgrade-medkit
   :stats:
      upgrade-id: 11
      bit-mask: 0x800

   Grants the :igw:weapon:`medkit`, selectable through the weapons section
   in FPS mode, for healing yourself or allies. Removing the upgrade removes
   the equipment and forces a weapon switch if needed. Healing amounts,
   range, and use are documented with the weapon.

Upgrade identifiers
-------------------

``upgrade-id`` is the zero-based bit index in the player's upgrade mask.
``bit-mask`` is the corresponding ``1 << upgrade-id`` value. These identifiers
are separate from :doc:`weapon IDs <weapons>`.

The ``menu_upgrade N`` console command buys or sells the upgrade with ID
``N``. It uses the same purchase checks and cascading sales described above.
