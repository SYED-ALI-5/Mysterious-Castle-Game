# Room File

class Room:
    def __init__(self, name, description, items=None, exits=None, hurdle=None):
        self.description = description
        self.name = name
        self.items = items if items is not None else {}
        self.exits = exits if exits is not None else {}
        self.hurdles = hurdle if hurdle is not None else {}
        self.is_locked = False
        self.ridle_here = False
        self.key = ''


    def unlock_room(self, key):
        if self.key != key:
            return False
        self.is_locked = False
        return True

    def remove_item(self, item):
        self.items.pop(item)

    def remove_hurle(self, item):
        self.hurdles.pop(item)

    def get_exit(self, direction):
        return self.exits.get(direction)

    def get_item(self, direction):
        return self.items.get(direction)
    
entrance = Room("Entrance", "You are standing at the entrance of a mysterious castle. Here is the door of Grand_Hall.", None, {"south": "Grand_Hall"})
grand_hall = Room("Grand_Hall",
                  "The Grand Hall is vast and have an items for future help. There are 2 doors at the east and 1 at west.", {"south": "Bat"}, {"north": "Entrance", "east": "Arena_Room", "south": "Store_Room", "west": "Dark_Room"})
arena_room = Room("Arena_Room",
                  "Dusty weapons in the Room. You feel like there's are secrets hidden here useful for future help.", {"north": "Gun", "east": "MR_Key"}, {"south": "Store_Room", "west": "Grand_Hall"})
store_room = Room("Store_Room", "It's dark and dusty. A secret hidden here.", {"east": "DR_Key"}, {"north": "Arena_Room", "west": "Grand_Hall"})
dark_room = Room("Dark_Room",
                 "A secret hidden here. There's something creepy about this place. Need an Equipment to deal with this danger. A door seems to be locked here.", {"north": "AR_Key"},{"east": "Grand_Hall", "south": "Miramar_Room"}, {"west": "Zombie"})
miramar_room = Room("Miramar_Room",
                    "Almost to Complete the Castle Journey. A huge Beast here for fight and you will won only if you have a weapon.", None, {"north": "Dark_Room" ,"south": "Sanhok_Room"}, {"west": "Beast"})
sanhok_room = Room("Sanhok_Room",
                   "Last Step to Complete the Castle Journey. Papa Beasts here for fight and you will won only if u have something special(Present at recent stage).", None, {"west": "Exit", "north": "Miramar_Room"}, {"west": "Venom"})
game_exit = Room("Exit", "Congratulations! You Completed the Castle Adventure.")

miramar_room.is_locked = True
arena_room.is_locked = True
dark_room.is_locked = True
game_exit.ridle_here = True

miramar_room.key = "MR_Key"
arena_room.key = "AR_Key"
dark_room.key = "DR_Key"