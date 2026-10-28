Enemies
=======

The health values below apply to God difficulty, selected through
:igw:cvar:`sv-difficulty`. Each enemy links to its health cvar, which lists
the settings for other difficulties. ``god-health`` records the configured
health value for God difficulty.

Comparison
----------

.. igw:statistics::
   :type: enemy
   :columns: god-health, armament

Definitions
-----------

.. igw:enemy:: bomber
   :name: Bomber
   :related: cvar:sk-health-bomber
   :stats:
      god-health: 500

   @TODO: Document the Bomber's armament, attacks, and behavior.

.. igw:enemy:: bosswalker
   :name: Boss Walker
   :related: cvar:sk-health-bosswalker
   :stats:
      god-health: 9500
      armament: Cannon and machine gun turrets

   @TODO: Document the Boss Walker's attacks and behavior.

.. igw:enemy:: conscript
   :name: Conscript
   :related: cvar:sk-health-conscript
   :stats:
      god-health: 175
      armament: Weapons include pistols and light machine guns

   @TODO: Document the remaining Conscript weapon variants, attacks, and behavior.

.. igw:enemy:: engineer
   :name: Engineer
   :related: cvar:sk-health-engineer
   :stats:
      god-health: 230

   @TODO: Document the Engineer's armament, attacks, and behavior.

.. igw:enemy:: grenadier
   :name: Grenadier
   :related: cvar:sk-health-grenadier
   :stats:
      god-health: 200
      armament: Grenades and a shield

   Throws grenades and carries a shield.

   @TODO: Document the Grenadier's attack timing, shield protection, and behavior.

.. igw:enemy:: herrad
   :name: Herrad
   :related: cvar:sk-health-herrad
   :stats:
      god-health: 250
      armament: Rocket launcher

   @TODO: Document the Herrad's attacks and behavior.

.. igw:enemy:: legionnaire
   :name: Legionnaire
   :related: cvar:sk-health-legionnaire
   :stats:
      god-health: 250
      armament: Flamethrower

   @TODO: Document the Legionnaire's attacks and behavior.

.. igw:enemy:: officer
   :name: Officer
   :related: cvar:sk-health-officer
   :stats:
      god-health: 2500
      armament: Minigun

   @TODO: Document the Officer's attacks and behavior.

.. igw:enemy:: ontos
   :name: Ontos
   :related: cvar:sk-health-ontos
   :stats:
      god-health: 2500
      armament: Cannon or rockets, plus machine gun turrets

   @TODO: Document the Ontos weapon variants, attacks, and behavior.

.. igw:enemy:: scarab
   :name: Scarab
   :related: cvar:sk-health-scarab
   :stats:
      god-health: 1550
      armament: Small cannon

   @TODO: Document the Scarab's attacks and behavior.

.. igw:enemy:: spy
   :name: Spy
   :related: cvar:sk-health-spy
   :stats:
      god-health: 230

   @TODO: Document the Spy's armament, attacks, and behavior.

.. igw:enemy:: templar
   :name: Templar
   :related: cvar:sk-health-templar
   :stats:
      god-health: 250

   @TODO: Document the Templar's armament, attacks, and behavior.

.. igw:enemy:: walker
   :name: Walker
   :related: cvar:sk-health-walker
   :stats:
      god-health: 5000
      armament: Ball of Doom and machine gun turrets

   @TODO: Document the Walker's attacks and behavior.

@TODO: Document how difficulty scaling and other runtime modifiers affect
the configured health values.
