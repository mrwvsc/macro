# Macro Script

This script is a simple macro tool that sends predefined messages when specific key combinations are pressed. It uses the `pyautogui` and `keyboard` libraries to simulate key presses and detect key combinations. The script is designed to work with a specific application and may require adjustments to the messages and key combinations for your use case.

## Features

- Define up to 8 custom messages (By all means, change this according to your needs).
- Start and stop the macro using `Ctrl+Shift+0` and `Ctrl+Shift+9`.
- Update messages dynamically using `Ctrl+Shift+M`.
- Send messages using `Ctrl+Shift+1` to `Ctrl+Shift+8`.

## Requirements

- Python 3.x
- `pyautogui` library
- `keyboard` library
- install using `pip install -r requirements.txt`
- Windows OS (developed tested on Windows 10)

## Example Output

When the script is running, you might see the following output in the console:

```
Macro script started, press ctrl+shift+9 to stop and ctrl+shift+0 to start the macro
Press ctrl+shift+m to update the messages
insert value 1: Hello
insert value 2: How are you?
insert value 3: Good morning
insert value 4: Thank you
insert value 5: Goodbye
insert value 6: Yes
insert value 7: No
insert value 8: See you later
Script started
Width of screen: 1920, Height of screen: 1080
Macro started
Sent message "Hello"
Sent message "Good morning"
Macro stopped
```

## Disclaimer

- The script may require administrative privileges to run properly.
- It is optimized for systems with at least 16GB RAM and a good processor.
- Developed on Windows 10 with 16gb ram and an i7 11th gen processor.
- Tested on another machine, with Windowes 10, 8 gb ram, and i7 6th gen.
  - Results: Very slow. Reducing the intervals ended up working. Generally not recommended use.

## Usage

1. Run the script in a Python environment.
2. Define your messages when prompted.
3. Use the specified key combinations to control the macro and send messages.
