# Why UniversalNBT (UNBT)?

UNBT is a convenience API to simplify working between different versions of the Minecraft game. It is designed with collaboration and community contribution as goals, structuring the code in a modular way so that people can add mapping modules incrementally over time as the need arises.

# A common use case

At the time of writing the immediate use case is to translate NBT structures from Java worlds into Bedrock (Pocket Edition/Mobile/Console) worlds. Many map making tools exist for use with Java worlds which are not yet compatible with Bedrock, and so map makers are frequently working first in Java, then migrating to Bedrock and hand crafting their worlds without the aid of accelerators like existing MCEdit filters.

# What problems does this solve?

The traditional approach to the problem of translating between game versions has been for Filter writers to build a one-way translation scripts. Then when the game is updated the script has to be updated or becomes obsolete.

Version control and alignment between all elements of the game need to be closely managed to be able to state with confidence that a particular script can work with the mix of:
1. Minecraft game
2. MCEdit
3. Minecraft world
4. Filter script

... and the pace of development and change makes this very challenging.

# How does UNBT approach the problem

UNBT realises that this is a data integration issue, and so adopts the patterns of enterprise application integration (EAI) to solve it. Through the use of a modular set of adapters the UNBT framework supports incremental extensions to the mapping library.

![Simple Architecture](https://i.imgur.com/3Wzy5P6.png)

Mappings are bi-directional between a 'master' data structure for each object, termed the "CANONICAL", and the version-specific data structures.

Through the use of a standard format for all objects the act of translating between arbitrary versions is simplified, and the decisions about where to place translation and formatting code becomes prescriptive and less prone to differences between filter authors.

![Handling future releases](https://i.imgur.com/O5w7mZ2.png)

# Example

1. A sample MCEdit Filter is supplied, called UniversalNBT_MCEditUnifiedFilter_v1.py. This is installed in MCEdit Filters.
2. Create a UNBT folder in the MCEdit Filters directory and place files UNBT.PY and __init__.py in it.
3. Copy the files starting with BE*.py into the director where MCEdit runs from, and the MCEdit Filters directory.
4. Open a Java world in MCEdit, select an area containing Signs and Command Blocks, and run the filter in 'READ' mode
5. Open the Bedrock world in the same MCEdit session, select the same area containing the same Signs and Command Blocks and run the filter in "WRITE" mode.
6. Check the console for warnings and errors.
7. The Bedrock block entities should have the Java NBT applied to the Bedrock NBT properties where appropriate.

# How can you help?

The mapping libraries need to be developed for each entity and block entity for each Minecraft version needed. If you have existing mappings from point-to-point filters please make them available, or submit an adapter following the existin convention shown in the examples.

The translations of commands and other control strings between versions will also need to be taken care of. This means that the metadata associated with enumerations and values should be tabulated and placed in reusable classes for the adapters to work with.


