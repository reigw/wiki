File formats
============

This section documents Iron Grip: Warlord's BSP, AAS, RCD, spline, and
:igw:file-format:`XML wave script <xml-wave-script>` file formats.
Unconfirmed interpretations are marked explicitly.

.. toctree::
   :maxdepth: 1

   scripts/waves

For the binary formats below, all offsets and lengths are in bytes. The
documented integers use little-endian byte order and occupy four bytes unless
stated otherwise. Floating point examples use IEEE 754 binary32. A *lump* is a
section addressed by an offset and length stored in the file header.

BSP: compiled map
-----------------

The ``.bsp`` files contain the map geometry, collision data, entities, lighting,
and visibility data. The signature is ``IBSP`` and the version is ``48``.
The directory follows the 17-lump arrangement in
`Quake III's qfiles.h <https://github.com/id-Software/Quake-III-Arena/blob/master/code/qcommon/qfiles.h>`_,
with format differences described below.

Header
~~~~~~

The header occupies 144 bytes:

.. list-table:: BSP header
   :header-rows: 1

   * - Offset
     - Size
     - Meaning
   * - 0
     - 4
     - ASCII signature ``IBSP`` (hex ``49 42 53 50``)
   * - 4
     - 4
     - Signed integer version, ``48`` (hex ``30 00 00 00``)
   * - 8
     - 136
     - 17 pairs of signed integers: absolute file offset and byte length

Directory entry ``i`` begins at ``8 + 8 * i``. Read each lump using its directory
entry: the data need not be stored in directory order or immediately after the
header.

Lumps
~~~~~

Names follow Quake III's directory. The record sizes are consistent with upstream
structures, except for the extended brush sides.
This does not establish the meaning of every field or flag in the game variant.

.. list-table:: BSP lump directory
   :header-rows: 1

   * - Index
     - Contents
     - Record size
   * - 0
     - Entity text
     - Variable
   * - 1
     - Shader references
     - 72
   * - 2
     - Planes
     - 16
   * - 3
     - BSP nodes
     - 36
   * - 4
     - Leaves
     - 48
   * - 5
     - Leaf surface indices
     - 4
   * - 6
     - Leaf brush indices
     - 4
   * - 7
     - Models
     - 40
   * - 8
     - Brushes
     - 12
   * - 9
     - Brush sides
     - 12
   * - 10
     - Draw vertices
     - 44
   * - 11
     - Draw indices
     - 4
   * - 12
     - Fog definitions
     - Not yet documented
   * - 13
     - Draw surfaces
     - 104
   * - 14
     - Lightmap data
     - Image bytes
   * - 15
     - Light grid
     - 8
   * - 16
     - Visibility data
     - Variable

Stock Quake III uses version 46 and eight-byte brush sides. This variant uses
12-byte brush sides. The additional four bytes per side remain undocumented.
Changing the version number alone is therefore insufficient to convert this
format to stock Quake III.

Entity text
~~~~~~~~~~~

Lump 0 contains brace-delimited entities with quoted key/value strings. Use the
stored lump length when extracting the text.

AAS: navigation areas
---------------------

The ``.aas`` files hold Area Awareness System navigation data. The signature is
``EAAS`` and the version is ``5``, matching the header layout in
`Quake III's aasfile.h <https://github.com/id-Software/Quake-III-Arena/blob/master/code/botlib/aasfile.h>`_.

Header
~~~~~~

The header occupies 124 bytes. Bytes 8 through 123 are XOR-masked on disk, using
the scheme implemented by ``AAS_DData`` in
`Quake III's AAS loader <https://github.com/id-Software/Quake-III-Arena/blob/master/code/botlib/be_aas_file.c>`_.
Decode that range before reading the checksum and directory:

.. code-block:: python

   # Work on a copy; only the header after the first eight bytes is masked.
   header = bytearray(data[:124])
   for i in range(116):
       header[8 + i] ^= (i * 119) & 0xff

.. list-table:: Decoded AAS header
   :header-rows: 1

   * - Offset
     - Size
     - Meaning
   * - 0
     - 4
     - ASCII signature ``EAAS`` (hex ``45 41 41 53``)
   * - 4
     - 4
     - Signed integer version, ``5``
   * - 8
     - 4
     - BSP checksum field
   * - 12
     - 112
     - 14 pairs of signed integers: absolute file offset and byte length

The payloads are not subject to this header mask. The checksum calculation has
not been verified here.

Lumps
~~~~~

The directory follows the upstream AAS order and record sizes:

.. list-table:: AAS lump directory
   :header-rows: 1

   * - Index
     - Contents
     - Record size
   * - 0
     - Presence bounding boxes
     - 32
   * - 1
     - Vertices
     - 12
   * - 2
     - Planes
     - 20
   * - 3
     - Edges
     - 8
   * - 4
     - Edge indices
     - 4
   * - 5
     - Faces
     - 24
   * - 6
     - Face indices
     - 4
   * - 7
     - Areas
     - 48
   * - 8
     - Area settings
     - 28
   * - 9
     - Reachability records
     - 44, including two trailing padding bytes
   * - 10
     - BSP nodes
     - 12
   * - 11
     - Cluster portals
     - 20
   * - 12
     - Portal indices
     - 4
   * - 13
     - Clusters
     - 16

Readers must allow lumps with a length of zero.

RCD: routing cache dump
-----------------------

The ``.rcd`` files contain cached navigation routes. They use the 32-byte, version
2 header described by ``routecacheheader_t`` in
`Quake III's routing code <https://github.com/id-Software/Quake-III-Arena/blob/master/code/botlib/be_aas_route.c>`_.

.. list-table:: RCD header
   :header-rows: 1

   * - Offset
     - Type
     - Meaning
   * - 0
     - Four bytes
     - ASCII signature ``MERC`` (hex ``4d 45 52 43``)
   * - 4
     - Signed integer
     - Version, ``2``
   * - 8
     - Signed integer
     - Number of navigation areas
   * - 12
     - Signed integer
     - Number of clusters
   * - 16
     - Integer
     - Area CRC field
   * - 20
     - Integer
     - Cluster CRC field
   * - 24
     - Signed integer
     - Number of portal cache records
   * - 28
     - Signed integer
     - Number of area cache records

The header is followed by the portal cache records and then the area cache
records. Each record starts with a four-byte integer giving its total byte size,
including the size field itself. The records begin at byte 32; their total count
is the sum of the two cache counts in the header.
Record lengths need not be multiples of four; do not add alignment padding.
The internal cache fields and CRC calculations remain undocumented here.

Spline: binary curve data
-------------------------

The ``.spline`` files contain binary data. Their complete structure and use by the
game remain unverified.

.. list-table:: Spline prefix
   :header-rows: 1

   * - Offset
     - Size
     - Interpretation
   * - 0
     - 4
     - Signed integer; meaning unverified
   * - 4
     - 4
     - Signed integer; meaning unverified
   * - 8
     - 48
     - Twelve floats, possibly four curve control points

There is no ASCII signature at the beginning. The first two integers should not
yet be treated as confirmed version or count fields.

The interpretation of the floats as curve control points is a hypothesis;
record boundaries and the remaining payload still need to be established.
