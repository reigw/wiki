CVARS
=====

Console variables expose game, client, and engine settings and runtime state.
The reference pages group variables by their name prefix and list them
alphabetically.

Flags
-----

Entries list their flags when present. The Flags row is omitted when no
flags are recorded for that variable.

.. list-table:: Cvar flags
   :header-rows: 1
   :widths: 25 10 65

   * - Flag
     - Console marker
     - Meaning
   * - ``CVAR_ARCHIVE``
     - ``A``
     - Saves the value when the engine writes its configuration, so it can
       be restored on a later launch. For an archived, latched variable,
       the pending value is saved even before it takes effect.
   * - ``CVAR_USERINFO``
     - ``U``
     - Includes the value in the client's user information sent to the
       server when connecting and when that information changes.
   * - ``CVAR_SERVERINFO``
     - ``S``
     - Includes the value in server information published to clients and
       returned by server-information queries.
   * - ``CVAR_ROM``
     - ``R``
     - Read-only to users. Console commands and configuration scripts cannot
       change it; the engine or game code controls its value.
   * - ``CVAR_INIT``
     - ``I``
     - Set during startup using ``+set <name> <value>`` on the command line.
       Once registered as initialization-only, it rejects changes from
       console commands and configuration scripts. Changing the startup
       value requires relaunching the game or dedicated server.
   * - ``CVAR_LATCH``
     - ``L``
     - Defers a requested change until the variable is registered again
       during initialization of the subsystem that uses it. The current
       value remains active while the new value is pending.
   * - ``CVAR_CHEAT``
     - ``C``
     - Rejects ordinary changes while :igw:cvar:`sv-cheats` is zero.
       Cheat-protected variables are restored to their defaults when the
       engine enforces the disabled-cheats state.

Changing protected variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The protections apply to ordinary assignments, including ``set`` commands
and assignments in configuration scripts. ``seta`` adds the archive flag
but does not bypass write protection. Engine and game code can use internal
setters to update protected variables directly.

Archive and information flags control saving and publication; they do not
grant permission to change a protected variable. A variable can have several
flags, such as ``CVAR_ARCHIVE`` together with ``CVAR_LATCH``.

Cheat permission is controlled by the server. ``sv_cheats`` is itself
read-only, so a normal ``set sv_cheats`` command cannot enable permission.

Applying latched changes
~~~~~~~~~~~~~~~~~~~~~~~~

Changing a latched variable prints ``will be changed upon restarting``.
Entering the variable's name without a value shows its current value and,
when present, a separate ``latched`` value. A further assignment replaces
the pending value.

The required restart depends on which subsystem initializes the variable.
It can be a renderer restart with ``vid_restart``, a sound restart with
``snd_restart``, a new map load, or a full game or dedicated-server restart.
A restart applies only the pending variables initialized by that operation;
there is no single subsystem restart that applies every latched variable.

Saving an archived value does not apply its pending change to the running
subsystem. Likewise, information sent over the network uses the active
value until the pending value takes effect.

@TODO: Document the required restart for each latched variable.

Skill settings
--------------

Skill values are grouped into a base setting and :igw:difficulty:`easy`,
:igw:difficulty:`medium`, :igw:difficulty:`hard`, :igw:difficulty:`brute`,
and :igw:difficulty:`god` difficulty settings. Each value represents a
configuration setting; engine defaults and allowed values remain to be
documented where marked with ``@TODO``. A missing difficulty setting leaves
the value unspecified.

.. important::

   Skill settings are not networked and must match on client and server.

Reference pages
---------------

.. toctree::
   :maxdepth: 1

   cvars/client-game
   cvars/client
   cvars/game
   cvars/skill-health
   cvars/skill-combat
   cvars/skill-other
   cvars/renderer
   cvars/server
   cvars/bots
   cvars/interface
   cvars/sound
   cvars/network
   cvars/input
   cvars/filesystem
   cvars/other

@TODO: Verify game-version applicability and document the remaining defaults,
valid values, units, and behavior.
