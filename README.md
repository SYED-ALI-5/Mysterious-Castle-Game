abdul haseeb 001

Room Class
The Room class is the fundamental structure that models the rooms in the castle. Each room has:

Name: The title or identifier for the room.
Description: A textual description of the room, adding flavor to the game and guiding the player's actions.
Items: Each room can have items that the player can collect and use for future challenges.
Exits: Possible directions the player can move to from the room, with adjacent rooms mapped to directions (e.g., north, south, east, west).
Hurdles: Certain obstacles that the player must overcome in a room, which could require items or actions.
Lock/Unlock Mechanism: Some rooms are locked and require a key to unlock.
Riddle Flags: A room can have a riddle, set via the ridle_here flag.
Methods in the Room Class
unlock_room(key): This method allows a player to unlock a room if they possess the correct key.
remove_item(item): Removes an item from the room once the player collects it.
remove_hurle(item): Removes an obstacle (hurdle) in the room.
get_exit(direction): Retrieves the room in the specified direction.
get_item(direction): Retrieves items in the specified direction.
Room Definitions
You defined multiple rooms for the adventure, each with its own description, items, exits, and hurdles:

Entrance: The starting point of the adventure, leading to the Grand Hall.
Grand Hall: A central room with multiple doors leading to different areas.
Arena Room: Contains dusty weapons and secrets.
Store Room: A dark, dusty room with hidden secrets.
Dark Room: A creepy room with dangers that require special equipment.
Miramar Room: A locked room with a beast that must be defeated using a weapon.
Sanhok Room: The final step of the adventure, guarded by Papa Beasts.
Exit: The completion point of the adventure, marking the player's success.
Key and Lock System
Miramar Room, Arena Room, and Dark Room are locked and can only be accessed by finding specific keys:
MR_Key for Miramar Room
AR_Key for Arena Room
DR_Key for Dark Room
Keys are placed in various rooms, and the player must collect them to unlock the respective rooms and proceed with the adventure.
