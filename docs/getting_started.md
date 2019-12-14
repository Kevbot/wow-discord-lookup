# World of Warcraft Simple Armory Discord Integration

## Getting started

### Basic usage principles

------

Once the bot has joined a Discord server, it can be called by any user by using a text channel.
The general command structure is described here:

    !<call to bot> <specific command> <argument 1> <argument 2> ... <argument N>

The argument list for the raid progression query commands are described here:

    !<general bot command> <expansion pack alias> <name of character> <region of character> <server name>

If the character specified exists then text will be printed into the text channel from which the bot was invoked.

### Accepted format of command fields

------

#### Note: all command fields are *case-insensitive.*

Table 1: command format structure
| Argument field | Accepted format | Examples |
| ---- | ---- | ---- |
| call to bot | single word | char |
| specific command| single word | bfa, wod, legion |
| name of character | single word | asmongold, kagarn, tanarage |
| region of character | single word | us, eu, kr, tw, cn |
| server name | single or multiple words, apostrophes and spaces allowed | Sister of Elune, kel'thuzad, emerald dream |

While the number of commands evolves over time, the currently supported commands are listed in Table 3.

### Output of basic commands

------

As of the current version, the output of all commands returns two types of information:
**general character information** and **command-specific information**. Each of these types
of information are described below.

**General character information:** Data returned that is common across all user commands types such as the character level and class.

**Command-specific information:** Data returned that is specific to a particular command, such as the raid progress of a particular expansion pack.

If an example input is given, such as:

     !char bfa asmongold us kel'thuzad

Then the general character information is listed below in Table 2.

Table 2: Example of output common across all commands

| Information  | Output example |
| ------------- |-------------:|
| character name        |   Asmongold   |
| character guild | \<Indestructible\> |
| character realm | Kel'thuzad |
| character level | 120 |
| character faction | Alliance |
| character race | Human |
| character specialization | Fury |
| character class | Warrior |
| character item level | 460 |

### Output of specific commands

------

A user must specify an expansion pack for which they wish
to view the character's raid progresss. To do so, specifiy
an alias phrase for the expansion pack's name as the command name. The
supported command names are given in Table 3 below.

Table 3: List of available commands for specific expansion packs
| Expansion name | Command name  | Additional command aliases | Command-specific raids | Description of output |
| :------------- | :-------------: |:-------------:| -----:| ------:|
| Classic | classic | vanilla |  "Molten Core", "Onyxia's Lair", "Blackwing Lair", "Ahn'Qiraj Temple", "Ruins of Ahn'Qiraj"| Single-boss kill recording, no LFR, heroic, or mythic data exists.|
| Burning Crusade | bc | tbc |   "Karazhan", "Gruul's Lair", "Magtheridon's Lair", "Serpentshrine Cavern", "Tempest Keep", "The Battle for Mount Hyjal", "Black Temple", "The Sunwell" | Single-boss kill recording, no LFR, heroic, or mythic data exists.|
| Wrath of the Lich King | wotlk | wrath, lich king | "Naxxramas", "The Obsidian Sanctum", "Vault of Archavon","The Eye of Eternity", "Ulduar", "Trial of the Crusader", "Icecrown Citadel", "The Ruby Sanctum" | Multi-boss kill recordings, no LFR or mythic data exists.|
| Cataclysm | cata | none | "Baradin Hold", "The Bastion of Twilight", "Blackwing Descent", "Throne of the Four Winds", "Firelands", "Dragon Soul"| Multi-boss kill recordings, no mythic data exists, LFR only for Dragon Soul.|
| Mists of Pandaria | mop | mists, pandaria  |  "Mogu'shan Vaults", "Heart of Fear", "Terrace of Endless Spring", "Throne of Thunder", "Siege of Orgrimmar"| Multi-boss kill recordings, all difficulties. |
| Warlords of Draenor| wod | warlords, draenor |   "Highmaul", "Blackrock Foundry", "Hellfire Citadel"| Multi-boss kill recordings, all difficulties. |
| Legion | legion  | none |  "The Emerald Nightmare", "Trial of Valor", "The Nighthold", "Tomb of Sargeras","Antorus, the Burning Throne",|  Multi-boss kill recordings, all difficulties. |
| Battle for Azeroth | bfa | battle | "Ny'alotha, the Waking City", "The Eternal Palace", "Battle of Dazar'alor", "Uldir"| Multi-boss kill recordings, all difficulties. |
| Shadowlands | sl | none | TBD | Multi-boss kill recordings, all difficulties. |

### Example usage of a raid progress query

------
This command will return the searched character's raid progression from the Cataclysm expansion pack.

    !char cata kagarn us emerald dream

This command will return the searched character's raid progression from the Mists of Pandaria expansion pack.

    !char mop asmongold us kel'thuzad
