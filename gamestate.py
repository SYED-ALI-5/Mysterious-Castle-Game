from room import *

Zombie_Alive = True
Beast_Alive = True
Venom_Alive = True

rooms = {
    "Entrance": entrance,
    "Grand_Hall": grand_hall,
    "Arena_Room": arena_room,
    "Store_Room": store_room,
    "Dark_Room": dark_room,
    "Miramar_Room": miramar_room,
    "Sanhok_Room": sanhok_room,
    "Exit": game_exit
}

items = {
    "Bat": "It will use to kill Zombies in dark room",
    "Gun": "It will use to kill Beast in Miramar room.",
    "voice": "It will use to kill Venom in Sanhok Room",
    "DR_Key": "It will use to open the Dark Room",
    "AR_Key": "It will use to open the Arena Room",
    "MR_Key": "It will use to open the Miramar Room",
}

inventory = []
current_room = rooms.get("Entrance")
new_room = None