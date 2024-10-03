# Enemy File

from inputimeout import inputimeout, TimeoutOccurred
import soundfile as sf
import sounddevice as sd
import numpy as np
import gamestate as gs  # Import shared state variables

def zombie_fight():
    if 'Bat' in gs.inventory:
        print(gs.current_room.name)
        try:
            input1 = inputimeout(
                "The ZOMBIE is in the WEST!!!! Write 'West' to face the zombie.\nYou have only 3 seconds: ",
                timeout=3)
            if input1.lower() != 'west':
                print("You have not moved to the west. The zombie got you!")
                gs.current_room = gs.rooms.get("Grand_Hall")
                return 'lost'

            print("Solve this Ridle in 10 seconds to kill the zombie.")

            input2 = inputimeout("Riddle ME THIS: I have cities but not houses, I have mountains but not trees, I have water but not fish. What am I? ", timeout=10)
            if input2.lower() == 'map':
                print("You killed the zombie.")
                print(gs.current_room.name)
                gs.current_room.remove_hurle("west")
                gs.Zombie_Alive = False  # Update state in game_state
                return 'WON!'
            else:
                print("You failed to hit the zombie.")
                gs.current_room = gs.rooms.get("Grand_Hall")
                return 'lost'

        except TimeoutOccurred:
            print("You lost the zombie fight, type faster next time!")
            gs.current_room = gs.rooms.get("Grand_Hall")
            return 'lost'
    else:
        print("You don't have the bat to kill the zombie.")
        gs.current_room = gs.rooms.get("Grand_Hall")
        return 'lost'

# The same applies to beast_fight and venom_fight, using gs.Beast_Alive and gs.Venom_Alive respectively.


def beast_fight():
    if 'Gun' in gs.inventory:
        directions = ['north', 'west', 'south']
        direction_index = 0
        fire_count = 0

        try:
            while fire_count < 3:
                current_direction = directions[direction_index]
                prompt = f"The BEAST is in the {current_direction.upper()}!!!! Write '{current_direction}' to face the beast.\nYou have 3 seconds: "
                direction_input = inputimeout(prompt, timeout=3)

                if direction_input.lower() != current_direction:
                    print(f"You did not face the beast in the {current_direction}. The beast got you!")
                    gs.current_room = gs.rooms.get("Dark_Room")
                    return 'lost'

                fire_input = inputimeout("Write 'FIRE' to attack the beast: ", timeout=3)
                if fire_input.lower() == 'fire':
                    fire_count += 1
                    print(f"You hit the beast with fire {fire_count}/3.")

                    if fire_count < 3:
                        direction_index = (direction_index + 1) % len(directions)
                        print(f"The beast has moved to the {directions[direction_index].upper()}!")
                else:
                    print("You failed to attack the beast with fire!")
                    gs.current_room = gs.rooms.get("Dark_Room")
                    return 'lost'


            print("You defeated the beast!")
            gs.inventory.append('voice')
            print('You have absorbed beast Aura!! You are Mythical now')
            gs.current_room.remove_hurle("west")
            gs.Beast_Alive = False
            return 'WON!'

        except TimeoutOccurred:
            print("You lost the beast fight, type faster next time!")
            gs.current_room = gs.rooms.get("Dark_Room")
            return 'lost'

    else:
        print("You don't have the Gun to fight the beast.")
        gs.current_room = gs.rooms.get("Dark_Room")
        return 'lost'

def listen_for_shout(threshold=0.9, duration=2):
    """Listens to the microphone for a loud shout for a specific duration."""
    print("Listening for a shout...")

    shout_detected = [False]  # Use a mutable object to track shout detection inside the callback

    def audio_callback(indata, frames, time, status):
        # Calculate the norm of the input audio data to get the volume level
        volume_norm = np.linalg.norm(indata)  # Normalized volume level
        print(f"Volume Level: {volume_norm:.2f}")  # Log the volume level for debugging
        if volume_norm > threshold:
            print("Detected a shout!")
            shout_detected[0] = True  # Set shout_detected to True
            raise sd.CallbackStop()  # Stop the callback when shout is detected

    try:
        # Open a stream, listening for audio input
        with sd.InputStream(callback=audio_callback):
            sd.sleep(int(duration * 1000))  # Listen for the specified duration

        # Return the result based on shout detection
        if shout_detected[0]:
            return True
        else:
            print("No shout detected.")
            return False

    except sd.CallbackStop:
        # This block will execute if the shout is detected and the callback stops
        return True


def play_victory_sound(file_path):
    """Plays the victory sound from an opus file."""
    try:
        # Read the opus audio file
        data, samplerate = sf.read(file_path)
        # Play the audio
        sd.play(data, samplerate)
        sd.wait()  # Wait until the file is played completely
    except Exception as e:
        print(f"Error playing sound: {e}")


def venom_fight():
    if 'voice' in gs.inventory:
        print("The beast is in the NORTH! Shout 'AAA' to kill it.")
        if listen_for_shout(threshold=10):  # Adjust threshold here
            print("You killed the beast with your shout!")
            play_victory_sound('beast_kill_sound.mp3')  # Path to your opus file
            gs.current_room.remove_hurle("west")
            gs.Venom_Alive = False
            return 'WON!'
        else:
            print("You didn't shout loud enough. The beast defeated you.")
            gs.current_room = gs.rooms.get("Miramar_Room")
            return 'lost'
    else:
        print("You don't have the ability to shout at the beast.")
        gs.current_room = gs.rooms.get("Miramar_Room")
        return 'lost'