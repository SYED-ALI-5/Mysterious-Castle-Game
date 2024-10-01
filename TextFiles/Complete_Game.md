HAFIZ HAMZA AHMAD
SP23-BAI-018


# Text Based Mysterious Castle Adventure Game

Introduction
Welcome to Mysterious Castle Adventure, an interactive text-based game where you explore a mysterious castle, solve riddles, fight enemies, and collect items. The game includes several rooms to explore, enemies to defeat, and puzzles to solve. Your objective is to survive and unlock rooms by using collected items and solving challenges along the way.

*How to Play*
-> The game is a text-based adventure where you, the player, enter commands to explore rooms, collect items, and fight enemies.
-> You can interact with the game by typing commands like move, look, take, unlock, and more.
-> The game can be saved and loaded, allowing you to pick up where you left off.
-> Game Setup
-> The game is divided into multiple rooms, each with its description, items, exits, and potential hurdles. These are the core game components:

*Room Setup*
    Each room has:
-> name: The name of the room.
-> description: A description of what the room looks like and what's in it.
-> items: Objects found in the room, which can be used later.
-> exits: Directions (north, east, south, west) leading to other rooms.
-> hurdles: Obstacles in the room that need specific items or actions to overcome.
-> is_locked: A boolean that indicates if the room is locked.
-> key: If the room is locked, you must possess a key to unlock it.
     *Rooms*
-> Entrance: Start your journey here. Leads to the Grand Hall.
-> Grand Hall: Main hub with exits to multiple rooms. Contains important items.
-> Arena Room: Contains weapons and keys to progress further in the game.
-> Store Room: Hidden secrets are found here, along with keys to other rooms.
-> Dark Room: A dangerous place with zombies and other dangers.
-> Miramar Room: Fight a beast here to unlock special abilities.
-> Sanhok Room: The final challenge, where you must defeat the ultimate enemy.
-> Exit: Successfully complete the adventure by reaching this room.
    
    *Inventory*
Throughout the game, you will collect items (e.g., Bat, Gun, keys). Items are stored in your inventory.
Some items are required to unlock rooms or fight enemies. You can take, use, or drop items.
Enemies
There are various enemies to fight, each with different mechanics:
-> Zombie: You must solve a riddle quickly to defeat it.
-> Beast: Use a gun and face the beast in multiple directions.
-> Venom: Shout into your microphone to defeat this enemy.

*Controls/Commands*
The following commands can be used to interact with the game:

-> move: Move between rooms. Enter a direction (north, east, south, west) to move.
-> look: Look around the room and see a description of your surroundings.
-> inventory: View the items you currently possess.
-> take: Take an item from the room by specifying a direction (north, east, south, west).
-> drop: Drop an item from your inventory.
-> examine: Examine the room to see if there are any items to pick up.
-> unlock: Unlock a locked room with a key from your inventory.
-> save: Save your current game progress.
-> load: Load a previously saved game.
-> help: Get a list of available exits and hurdles in the room.
-> quit: Exit the game.

*Saving and Loading*
The game can be saved at any point using the save command.
A saved game stores your current room, inventory, and enemy status.
You can load the game later using the load command.
Fighting Enemies
You will encounter enemies like Zombies, Beasts, and Venom that require specific strategies to defeat:

-> Zombie: Solve a riddle within a limited time.
-> Beast: Use a gun and fight in three rounds, hitting the beast each time.
-> Venom: Shout into your microphone to kill the Venom.

*Audio Features*
The game includes the ability to detect sounds:
-> Shouting: In the final battle with Venom, you must shout to defeat it using your microphone.
-> Victory Sound: A victory sound will play when you defeat Venom.
-> Additional Features
-> Riddles: Some rooms and fights require you to solve riddles to proceed.
-> Item Usage: Certain items in your inventory are required to progress or defeat enemies.
-> JSON Save System: Game progress is saved to a JSON file, allowing you to continue your adventure later.