Powerups
========

Powerups are pickups found in the world: food restores health, jewels grant
Power, and weapon pickups provide additional equipment. Walk over a pickup
to collect it. The pickup is shared, so collecting it removes it from the
world until it respawns, if applicable.

The difficulty tables use the configured values from :doc:`cvars/skill`.
Base records the separate ``skill.cfg`` settings. Population settings can
be overridden by :doc:`wave scripts <scripts/waves>` and are also limited by
the available spawn locations. These values do not establish allowed ranges
or guarantee that a particular number of pickups appears on every map.

Food and jewels
---------------

.. igw:entity:: food
   :name: Food
   :summary: Restores health when collected.
   :skill-cvars:
      sk-food-hp
      sk-food-respawn
      sk-max-food
   :stats:
      classname: item_food
      item-type: IT_FOOD

   Food can be collected only while health is below the player's maximum.
   Healing is capped at that maximum; any excess is lost. The healing amount
   is controlled by :igw:cvar:`sk-food-hp`.

   Fire damage can turn map food into :igw:entity:`entity:hot-food`. One of
   the four food model variants is excluded from this conversion.

   @TODO: Identify the food model variant that cannot be cooked and document
   which fire attacks can cook food.

.. igw:entity:: hot-food
   :name: Hot Food
   :summary: Cooked food with a separate healing amount.
   :related: entity:food
   :skill-cvars:
      sk-food-hot-hp
   :stats:
      classname: item_food_hot
      item-type: IT_HOTFOOD

   Cooking food switches it to hot food and sets its burning flag. That flag
   selects :igw:cvar:`sk-food-hot-hp` as the healing amount. Hot food follows
   the same collection restriction and maximum-health cap as ordinary food.

   Both kinds use :igw:cvar:`sk-food-respawn`. When food respawns, it becomes
   ordinary, uncooked food again, with a randomly selected model variant.
   Cooking food does not create an additional pickup or a separate population.

.. igw:entity:: jewel
   :name: Jewels
   :summary: Grant Power when collected.
   :skill-cvars:
      sk-jewel-power
      sk-jewel-respawn
      sk-max-jewel
   :stats:
      classname: item_jewel
      item-type: IT_JEWEL

   In cooperative play, each jewel grants :igw:cvar:`sk-jewel-power` Power.
   A player can collect a jewel while holding less than 9,999 Power. The
   resulting balance is capped at 9,999, so part of the reward can be lost
   when collecting near the cap.

   Deathmatch uses the jewel item's quantity for the Power reward instead.
   NPC drops set that quantity to 50 and player drops set it to 100. The
   quantity is shared by all jewels, so a later drop can change the reward
   of jewels already in the world.

   @TODO: Document jewel loot-score accounting and pickup effects for NPCs
   controlled by a player.

Weapon pickups
--------------

:igw:weapon:`dynamite` and the :igw:weapon:`suicide` use pickup locations
placed in the map. The :igw:weapon:`radio` and
:igw:weapon:`rocketlauncher` use wave-script locations outside Deathmatch
and require the Scorched Earth expansion to be enabled. Their attacks and
ammunition settings are documented under :doc:`weapons`.

The radio and rocket launcher can be collected only when both their clip
and reserve ammunition are empty. Other weapon pickups can be collected
even if the player already holds that weapon. A suicide-device pickup
sets its ammunition to one device.

.. list-table:: Map weapon pickup settings
   :header-rows: 1

   * - Weapon
     - Population cap
     - Respawn interval, seconds
     - Location after respawning
   * - :igw:weapon:`dynamite`
     - :igw:cvar:`sk-max-dynamite`
     - :igw:cvar:`sk-dynamiterespawn`
     - Random spawn location for that weapon
   * - :igw:weapon:`suicide`
     - :igw:cvar:`sk-max-suicide`
     - :igw:cvar:`sk-suiciderespawn`
     - Random spawn location for that weapon
   * - :igw:weapon:`radio`
     - :igw:cvar:`sk-max-radio`
     - :igw:cvar:`sk-radiorespawn`
     - Same location
   * - :igw:weapon:`rocketlauncher`
     - :igw:cvar:`sk-max-rocket`
     - :igw:cvar:`sk-rocketlauncherrespawn`
     - Same location

@TODO: Verify how :igw:cvar:`sk-dynamiterandomrespawn` and
:igw:cvar:`sk-suiciderandomrespawn` affect pickup timing. The pickup code
writes those values to the collecting entity, while the respawn logic reads
the pickup entity's random-delay field.

Placement and respawning
------------------------

At round start, food, jewels, dynamite, suicide devices, radios, and rocket
launchers are placed at distinct, randomly selected locations from their
respective spawn pools. For each kind, the number of active items is the
smaller of its population cap and its number of available spawn locations.

After collection, food, jewels, dynamite, and suicide devices respawn at a
random free location in their own pool. The previous location is released
before the selection, so an item can reappear where it was collected.
Radios and rocket launchers retain their locations when respawning.

The food population cap is :igw:cvar:`sk-max-food`; the jewel cap is
:igw:cvar:`sk-max-jewel`. Wave scripts can override these through the
``sk_max_food`` and ``sk_max_jewel`` elements in ``SKILLSETTINGS``.

An item's ``wait`` property overrides its normal respawn interval when
nonzero; ``wait -1`` prevents automatic respawning. Its ``random`` property
varies the delay in seconds. Dropped items are removed after collection
and do not respawn; uncollected drops disappear after 30 seconds.

Drops
-----

Killed officers drop their :igw:weapon:`minigun`. In Deathmatch, killed
looters can drop food, jewels, dynamite, a suicide device, a rocket launcher,
or a minigun. A single random roll selects the result:

.. list-table:: Deathmatch looter drops
   :header-rows: 1

   * - Result
     - Chance
   * - Food
     - 30%
   * - :igw:weapon:`dynamite`
     - 20%
   * - :igw:weapon:`suicide`
     - 5%
   * - :igw:weapon:`rocketlauncher`
     - 5%
   * - Nothing
     - 20%
   * - Jewels
     - 10%
   * - :igw:weapon:`minigun`
     - 10%

Internal item types
-------------------

Food, hot food, jewels, and weapons use the distinct item types recorded
above and in :doc:`weapons`. The item table contains no timed ``IT_POWERUP``
or persistent ``IT_PERSISTANT_POWERUP`` entries.

@TODO: Document the behavior and availability of the retained health,
armor, and holdable item entries separately from food and weapon pickups.
