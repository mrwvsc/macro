# variables
interval = 0.000000001  # interval between key presses, very small to simulate fast typing
sleeptime = 0.5  # sleep time between after message is sent
key_bindings = { # keybinds for messages. added here for easier fixes when needed. 
    "stop_macro": "ctrl+shift+9",
    "start_macro": "ctrl+shift+0",
    "exit_program": "ctrl+shift+q",
    "update_messages": "ctrl+shift+m",
    "message_1": "ctrl+shift+1",
    "message_2": "ctrl+shift+2",
    "message_3": "ctrl+shift+3",
    "message_4": "ctrl+shift+4",
    "message_5": "ctrl+shift+5",
    "message_6": "ctrl+shift+6",
    "message_7": "ctrl+shift+7",
    "message_8": "ctrl+shift+8",
}

# imports
import pyautogui as pag, keyboard as kb, time


# functions

def define():
    global val1, val2, val3, val4, val5, val6, val7, val8
    val1 = val2 = val3 = val4 = val5 = val6 = val7 = val8 = ""  # reset values
    try:
        val1 = input('Insert value 1: ')
        val2 = input('Insert value 2: ')
        val3 = input('Insert value 3: ')
        val4 = input('Insert value 4: ')
        val5 = input('Insert value 5: ')
        val6 = input('Insert value 6: ')
        val7 = input('Insert value 7: ')
        val8 = input('Insert value 8: ')
    except Exception as e:
        print(f"An error occurred while defining values: {e}")

def startMessage():
    print("Macro script started, press ctrl+shift+9 to stop and ctrl+shift+0 to start the macro")  # message to indicate that the script has started
    print("Press ctrl+shift+m to update the messages")  # message to indicate that the messages can be updated
    define()  # call the define function to get the messages from the user
    print("Script started")
    width, height = pag.size()  # prints the width and height of the screen
    print(f"Width of screen: {width}, Height of screen: {height}")

def main():
    startMessage()
    macro_running = True  # variable to control the macro state

    while True:
        if kb.is_pressed(key_bindings["stop_macro"]):  # macro stop
            macro_running = False
            print("Macro stopped")
        elif kb.is_pressed(key_bindings["start_macro"]):  # macro start
            macro_running = True
            print("Macro started")

        if kb.is_pressed(key_bindings["exit_program"]):  # exit the script
            print("Exiting program...")
            break

        if kb.is_pressed(key_bindings["update_messages"]):  # recall define function
            define()
            print("Messages updated")

        if macro_running:
            try:
                if kb.is_pressed(key_bindings["message_1"]):  # first message
                    time.sleep(sleeptime)
                    pag.typewrite(val1, interval)
                    pag.press('enter')
                    print(f"Sent message \"{val1}\"")
                    time.sleep(sleeptime)
                elif kb.is_pressed(key_bindings["message_2"]):  # second message
                    time.sleep(sleeptime)
                    pag.typewrite(val2, interval)
                    pag.press('enter')
                    print(f"Sent message \"{val2}\"")
                    time.sleep(sleeptime)
                elif kb.is_pressed(key_bindings["message_3"]):  # third message
                    time.sleep(sleeptime)
                    pag.typewrite(val3, interval)
                    pag.press('enter')
                    print(f"Sent message \"{val3}\"")
                    time.sleep(sleeptime)
                elif kb.is_pressed(key_bindings["message_4"]):  # fourth message
                    time.sleep(sleeptime)
                    pag.typewrite(val4, interval)
                    pag.press('enter')
                    print(f"Sent message \"{val4}\"")
                    time.sleep(sleeptime)
                elif kb.is_pressed(key_bindings["message_5"]):  # fifth message
                    time.sleep(sleeptime)
                    pag.typewrite(val5, interval)
                    pag.press('enter')
                    print(f"Sent message \"{val5}\"")
                    time.sleep(sleeptime)
                elif kb.is_pressed(key_bindings["message_6"]):  # sixth message
                    time.sleep(sleeptime)
                    pag.typewrite(val6, interval)
                    pag.press('enter')
                    print(f"Sent message \"{val6}\"")
                    time.sleep(sleeptime)
                elif kb.is_pressed(key_bindings["message_7"]):  # seventh message
                    time.sleep(sleeptime)
                    pag.typewrite(val7, interval)
                    pag.press('enter')
                    print(f"Sent message \"{val7}\"")
                    time.sleep(sleeptime)
                elif kb.is_pressed(key_bindings["message_8"]):  # eighth message
                    time.sleep(sleeptime)
                    pag.typewrite(val8, interval)
                    pag.press('enter')
                    print(f"Sent message \"{val8}\"")
                    time.sleep(sleeptime)
            except Exception as e:
                print(f"An error occurred while sending a message: {e}")

if __name__ == "__main__":
    main()