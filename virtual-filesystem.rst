Virtual filesystem and PK3 priority
===================================

Iron Grip: Warlord reads game files from directories and ``.pk3`` ZIP archives
through a shared search list. A request uses a path relative to the game
directory, such as ``scripts/ig_blend.shader``. The first allowed match wins.

Directory order
---------------

For the path roots, mod selection, and defaults, see :igw:cvar:`fs-homepath`,
:igw:cvar:`fs-basepath`, :igw:cvar:`fs-cdpath`, :igw:cvar:`fs-game`, and
:igw:cvar:`fs-basegame`.

Without a pure-server package list, directories are searched in the following
order, from highest to lowest priority:

1. ``fs_homepath/<fs_game>``
2. ``fs_basepath/<fs_game>``
3. ``fs_cdpath/<fs_game>``
4. ``fs_homepath/<fs_basegame>``
5. ``fs_basepath/<fs_basegame>``
6. ``fs_cdpath/<fs_basegame>``
7. ``fs_homepath/base``
8. ``fs_basepath/base``
9. ``fs_cdpath/base``

Only configured directory groups are included. Identical root/directory pairs
are added only once.

Each listed directory is a complete priority group: its PK3s are searched
first, followed by its loose files, before moving to the next directory. A loose file is a file outside
an archive. Thus a loose ``fs_homepath/<fs_game>/scripts/ig_blend.shader`` beats
the same path in any ``base`` PK3, but a PK3 in the same mod directory beats
that loose file.

An earlier directory beats a later directory regardless of archive names.
For example, ``fs_homepath/base/resources.pk3`` beats
``fs_basepath/base/zpatch113.pk3`` when the roots differ, even though
``zpatch113.pk3`` has the later archive name.

.. _vfs-pk3-order:

PK3 order
---------

Within each directory, PK3s are searched in reverse alphabetical order, ignoring
letter case. For example, these archives have the following relative priority:

.. code-block:: text

   zpatch114media.pk3 > zpatch114.pk3 > zpatch113.pk3 > resources.pk3 > loose files

Names are compared character by character, so ``textures_1.pk3`` beats
``textures2.pk3`` because ``_`` sorts after ``2``. The ``zpatch`` prefix has no
special meaning. File dates and copy order do not set priority. Avoid archive
names differing only in case; they compare equal and have no defined relative
priority.

The game indexes PK3s directly inside each game directory when the filesystem
starts or restarts. It does not search subdirectories for more PK3s or unpack
entire archives. Files inside indexed archives are read as needed. Restart the
game after adding, removing, or renaming PK3s to rebuild the search list.

A directory ending in ``.pk3dir`` is not mounted as an unpacked package. To use
loose assets, place their paths directly under a searched game directory, such
as ``base/scripts/ig_blend.shader``. These files retain the loose-file priority
described above.

Whole files override
--------------------

Only matching paths compete. A patch PK3 can contain just its changes: replacing
``scripts/ig_blend.shader`` leaves unrelated textures and sounds from older PK3s
available, and a new path adds a new file.

The winning file replaces the entire older file. Their contents do not merge.
For example, if a replacement shader file contains only one edited definition,
the other definitions from the older file at that path are unavailable. Include
everything that must remain in that file.

Different filenames remain separate virtual files. A subsystem that loads
several files, such as shader scripts, can still read each of them. Filesystem
priority alone does not describe how that subsystem resolves conflicting
definitions within those different files.

@TODO: Document shader-definition priority across differently named shader
files.

Paths inside PK3s ignore letter case and treat ``/`` and ``\`` as equivalent
separators. Use ``/`` in archive paths. Duplicate matching entries within one
PK3 resolve to the last entry in the ZIP central directory; avoid duplicates.
Loose files use the host filesystem's case handling, so keep spelling
consistent.

Pure servers
------------

When connecting to a pure server (``sv_pure 1``), the client receives a list of
allowed PK3 checksums. It moves matching packages to the front of the search
list in the server's order and skips packages whose checksums are absent from
that list. Changing a local PK3's filename cannot override the server's order
or make an unapproved package readable.

With a nonempty pure-server package list, loose files are allowed only for
these filename endings, compared without regard to case:

* ``.cfg``
* ``.ttf``
* ``.menu``
* ``.game``
* ``.dat``
* ``.dm_69`` (demos)

Loose textures, sounds, and models are skipped. Allowed loose files keep their
position behind the server-ordered packages; they do not receive an extra
priority boost. The same loose-file allowlist also applies when ``fs_restrict``
is enabled.

@TODO: Document any additional effects of restricted mode.

Downloads
---------

The client compares server-requested packages with the checksums of its mounted
PK3s to find missing packages. A local archive with the expected name but the
wrong checksum does not satisfy the request. When that name already exists, the
download list can select a local filename with the checksum appended as eight
hexadecimal digits: ``<name>.<checksum>.pk3``.

There are no special ``dlcache`` directories in the game-directory search setup.
Putting a PK3 in ``base/dlcache`` does not mount it; the normal PK3 scan is not
recursive.

@TODO: Document download destinations, transfer settings, and the filesystem
restart after downloads.

Inspecting the active filesystem
--------------------------------

.. list-table:: Console commands
   :header-rows: 1

   * - Command
     - Behavior
   * - ``path``
     - Prints the active search list, highest priority first. With a pure-server
       list active, it also marks whether each PK3 is on that list.
   * - ``dir scripts .shader``
     - Lists virtual filenames in a directory with the requested extension.
   * - ``fdir *ig_blend*``
     - Lists virtual filenames matching a filter.
   * - ``set fs_debug 1``
     - Logs the directory or PK3 used when a file is opened.
   * - ``touchFile scripts/ig_blend.shader``
     - Opens and closes a file through the normal read path. Combined with
       ``fs_debug``, this shows which allowed copy is selected.

There is no ``which`` console command. To inspect a particular file, run:

.. code-block:: text

   set fs_debug 1
   touchFile scripts/ig_blend.shader
   set fs_debug 0

Replace the example path with the file to inspect. Directory listings show
virtual names, not the source of each name; use the open-file logging to check
which copy actually wins.
