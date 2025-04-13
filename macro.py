# this script is a simple macro that sends messages defined by the user when certain key combinations are pressed
# it uses the pyautogui and keyboard libraries to simulate key presses and detect key combinations
# it is designed to work with a specific application, so the messages and key combinations may need to be changed
# the script starts by defining the messages to be sent and the key combinations to trigger them
# runs in an infinite loop, checking for key presses and sending the corresponding messages
# macro can be stopped by pressing ctrl+shift+9 and started again by pressing ctrl+shift+0
# also prints the width and height of the screen to the console
# the script uses a very small interval for typing the messages, which may cause issues on some systems
# macro may require administrative privileges to run properly
# DISCLAMER: may not work on all machines, might require 16gb ram or above,
# and a good processor, as it uses pyautogui to simulate key presses
# tested with windows 10, may work with other versions of windows
# tested on windows 10, 8gb ram and i7 6th gen processor, but not recommended, very slow
# developed on windows 10, 16gb ram, i7 11th gen processor, works fine. 

# imports
import pyautogui as pag, keyboard as kb, time

# functions

def define():
    # this function defines the messages to be sent
    # it is called when the script is started
    # the messages are defined as global variables so they can be accessed by the main loop
    global val1, val2, val3, val4, val5, val6, val7, val8
    val1 = input('insert value 1: ') # first message to be sent
    val2 = input('insert value 2: ') # second message to be sent
    val3 = input('insert value 3: ') # third message to be sent
    val4 = input('insert value 4: ') # fourth message to be sent
    val5 = input('insert value 5: ') # fifth message to be sent
    val6 = input('insert value 6: ') # sixth message to be sent
    val7 = input('insert value 7: ') # seventh message to be sent
    val8 = input('insert value 8: ') # eighth message to be sent



print("Macro script started, press ctrl+shift+9 to stop and ctrl+shift+0 to start the macro") # message to indicate that the script has started
# define the messages to be sent
print("Press ctrl+shift+m to update the messages") # message to indicate that the messages can be updated
define() # call the define function to get the messages from the user

interval = 0.000000000000000000001 #  interval between key presses, very small to simulate fast typing
sleeptime = 0.5 # sleep time between after message is sent

print("Script started")
width, height = pag.size() # prints the width and height of the screen
print(f"Width of screen: {width}, Height of screen: {height}")

macro_running = True # variable to control the macro state

while True:
    if kb.is_pressed('ctrl+shift+9'): # macro stop
        macro_running = False
        print("Macro stopped")
    elif kb.is_pressed('ctrl+shift+0'): # macro start
        macro_running = True
        print("Macro started")
    
    if kb.is_pressed('ctrl+shift+m'): # recall define function
        define() # call the define function to get the messages from the user
        print("Messages updated")
    
    if macro_running:
        if kb.is_pressed('ctrl+shift+1'): # first message
            time.sleep(0.5)
            pag.typewrite(val1, interval) # type the message
            pag.press('enter')
            print(f"Sent message \"{val1}\"")
            time.sleep(0.5)
        elif kb.is_pressed('ctrl+shift+2'): # second message
            time.sleep(0.5)
            pag.typewrite(val2, interval) # type the message
            pag.press('enter')
            print(f"Sent message \"{val2}\"")
            time.sleep(0.5)
        elif kb.is_pressed('ctrl+shift+3'): # third message
            time.sleep(0.5)
            pag.typewrite(val3, interval) # type the message
            pag.press('enter')
            print(f"Sent message \"{val3}\"")
            time.sleep(0.5)
        elif kb.is_pressed('ctrl+shift+4'): # fourth message
            time.sleep(0.5)
            pag.typewrite(val4, interval) # type the message
            pag.press('enter')
            print(f"Sent message \"{val4}\"")
            time.sleep(0.5)
        elif kb.is_pressed('ctrl+shift+5'): # fifth message
            time.sleep(0.5)
            pag.typewrite(val5, interval) # type the message
            pag.press('enter')
            print(f"Sent message \"{val5}\"")
            time.sleep(0.5)
        elif kb.is_pressed('ctrl+shift+6'): # sixth message
            time.sleep(0.5)
            pag.typewrite(val6, interval) # type the message
            pag.press('enter')
            print(f"Sent message \"{val6}\"")
            time.sleep(0.5)
        elif kb.is_pressed('ctrl+shift+7'): # seventh message
            time.sleep(0.5)
            pag.typewrite(val7, interval) # type the message
            pag.press('enter')
            print(f"Sent message \"{val7}\"")
            time.sleep(0.5)
        elif kb.is_pressed('ctrl+shift+8'): # eigth message
            time.sleep(0.5)
            pag.typewrite(val8, interval) # type the message 
            pag.press('enter')
            print(f"Sent message: \"{val8}\"")
            time.sleep(0.5)
