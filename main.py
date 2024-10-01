from room import *
import enemy as em
import gamestate as gs
import json

def move(direction):
    name_room_name = gs.current_room.get_exit(direction)
    gs.new_room = gs.rooms.get(name_room_name)
    if name_room_name:
        if gs.new_room.is_locked:
            if gs.new_room.key in gs.inventory:
                print(f"\nThe Room in which you want to enter is locked. Use {gs.new_room.key} from your gs.inventory to unlock this room.")
            else:
                print(f"\nYou don't have the key to Unlock the {name_room_name}")
        elif gs.new_room.ridle_here:
            print("\nYou are about to complete the Castle Adventure. Just Solve the Riddle.")
            solve_Riddle()
        else:
            gs.current_room = gs.new_room
            print(f"\nYou moved to {gs.current_room.name}.")
    else:
        print("\nThis direction is not available in this room.")

def look(curentroom):
    print(gs.current_room.description)

def see_inventory():
    global inventory
    if gs.inventory:
        print(gs.inventory)
    else:
        print("\nInventory is empty")

def take_item(direction):
    if isinstance(gs.current_room.items, dict) and direction in gs.current_room.items:
        item = gs.current_room.items[direction]
        gs.inventory.append(item)
        gs.current_room.remove_item(direction)
        print(f"\nYou have taken the {item}.")
    else:
        print("\nThere is no item in that direction.")


def drop_item(item):
    if item in gs.inventory:
        gs.inventory.remove(item)
    else:
        print(f"\n{item} is not in your inventory.")

def use_key(key):
    if key in gs.inventory:
        gs.new_room.unlock_room(key)
        gs.current_room = gs.new_room
        print(f"\nYou moved to {gs.current_room.name}.")
        drop_item(key)
    else:
        print("\nYou don't have the key.")

def solve_Riddle():
    answer = input("\nRIDDLE ME THIS: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
    if answer.lower() == 'air':
        gs.current_room = gs.rooms.get("Exit")
        print(f"\n{gs.current_room.description}\n")
        gs.inventory.clear()
        quit()
    else:
        print("\nYou failed to solve the riddle. Try Again!")
        gs.current_room = gs.rooms.get("Miramar_Room")

def examine_item(curRoom):
    if isinstance(gs.current_room.items, dict) and len(gs.current_room.items) > 0:
        for key, value in gs.current_room.items.items():
            print(f"\nThere is a {value} in the {key}. Use: {gs.items.get(value)}")
    else:
        print("\nThere are no items in this room.")


def save():
    global inventory
    global Zombie_Alive, Beast_Alive, Venom_Alive

    # Create a dictionary to store the game state
    game_state = {
        'gs.current_room': gs.current_room.name,
        'gs.inventory': gs.inventory,
        'Zombie_Alive': Zombie_Alive,
        'Beast_Alive': Beast_Alive,
        'Venom_Alive': Venom_Alive
    }

    # Save the game state as a JSON string in a text file
    with open('game_save.txt', 'w') as save_file:
        save_file.write(json.dumps(game_state))
    print("\nGame saved successfully!")


def load():
    
    global inventory
    global Zombie_Alive, Beast_Alive, Venom_Alive

    try:
        # Read the saved game state from the text file
        with open('game_save.txt', 'r') as load_file:
            game_state = json.loads(load_file.read())

        # Restore the game state
        gs.current_room = gs.rooms.get(game_state['gs.current_room'])
        gs.inventory = game_state['gs.inventory']
        Zombie_Alive = game_state['Zombie_Alive']
        Beast_Alive = game_state['Beast_Alive']
        Venom_Alive = game_state['Venom_Alive']

        print("\nGame loaded successfully!")
        print(f"\nYou are in {gs.current_room.name}.")
    except FileNotFoundError:
        print("\nNo saved game found.")
    except Exception as e:
        print(f"\nError loading game: {e}")
        

def help(current_room):
    if isinstance(gs.current_room.exits, dict) and len(gs.current_room.exits) > 0:
        for key, value in gs.current_room.exits.items():
            print(f"\nThere is a {value} at the {key}.")
    else:
        print("\nThere are no exits in this room.")

    if isinstance(gs.current_room.hurdles, dict) and len(gs.current_room.hurdles) > 0:
        for key, value in gs.current_room.hurdles.items():
            print(f"\nThere is a {value} at the {key}.")
    else:
        print("\nThere are no hurdles in this room.")

def display():
    print("\nThere are exits in the following directions: north, east, south, and west.")
    print("Available actions: move, look, unlock, inventory, take, drop, examine, save, load, help, quit.")


# MAIN FILE
print('Welcome to Mysterious Castle Adventure!')

while True:
    if gs.current_room.name == "Dark_Room" and gs.Zombie_Alive:  # Use gs for shared state
        em.zombie_fight()
    elif gs.current_room.name == "Miramar_Room" and gs.Beast_Alive:
        em.beast_fight()
    elif gs.current_room.name == "Sanhok_Room" and gs.Venom_Alive:
        em.venom_fight()
    display()
    action = input(f"You are in {gs.current_room.name}\nWhat do you want to do?")
    action = action.strip()
    if action.lower() == "quit":
        print("\nThanks for Playing!")
        break
    elif action.lower() == "move":
        direction = input("\nEnter the direction in which you want to go.")
        if direction.lower() == "north":
            move(direction)
        elif direction.lower() == "south":
            move(direction)
        elif direction.lower() == "east":
            move(direction)
        elif direction.lower() == "west":
            move(direction)
        else:
            print("\nInvalid command.")
    elif action.lower() == "look":
        look(gs.current_room)
    elif action.lower() == "unlock":
        key = input("\nEnter the key.")
        use_key(key)
    elif action.lower() == "inventory":
        see_inventory()
    elif action.lower() == "take":
        direction = input("\nEnter the direction from which you want to take item.")
        if direction.lower() == "north":
            take_item(direction)
        elif direction.lower() == "south":
            take_item(direction)
        elif direction.lower() == "east":
            take_item(direction)
        elif direction.lower() == "west":
            take_item(direction)
        else:
            print("\nInvalid command.")         
    elif action.lower() == "drop":
        see_inventory()
        item = input("\nEnter the item name to drop.")
        drop_item(item)        
    elif action.lower() == "examine":
        examine_item(gs.current_room)       
    elif action.lower() == "save":
        save()     
    elif action.lower() == "load":
        load()        
    elif action.lower() == "help":
        help(gs.current_room)    
    else:
        print("\nInvalid command.")