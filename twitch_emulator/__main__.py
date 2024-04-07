import os
import subprocess
import sys
import threading

import irc.client
import irc.events
import pyautogui
import pygetwindow as gw
from dotenv import load_dotenv

load_dotenv()


def focus_on_desmume():
    if sys.platform == "darwin":  # macOS
        try:
            # Use AppleScript to bring DeSmuME to the front
            script = """/usr/bin/osascript -e 'tell app "DeSmuME" to activate' """
            subprocess.run(script, shell=True)
        except Exception as e:
            print(f"Error focusing on DeSmuME on macOS: {e}")
    elif sys.platform == "win32":  # Windows
        windows = gw.getWindowsWithTitle("DeSmuME")

        if windows:
            try:
                windows[0].activate()
            except Exception as e:
                print(f"Error focusing on DeSmuME on Windows: {e}")
        else:
            print("DeSmuME window not found.")


def execute_command(command_function):
    focus_on_desmume()
    command_function()


def on_connected(connection, event):
    for channel in CHANNELS:
        connection.join(channel)
    print(f"* Connected to Twitch")


def on_public_message(connection, event):
    message = event.arguments[0].strip().lower()
    args = message.split()

    command = args[0] if args else None
    command = command.lower()

    # Define command functions
    def handle_up_command():
        print("\ninput(handleUpCommand): Move up command received")
        pyautogui.press("up")
        print("input(handleUpCommand): Move up command handled")

    def handle_down_command():
        print("\ninput(handleDownCommand): Move down command received")
        pyautogui.press("down")
        print("input(handleDownCommand): Move down command handled")

    def handle_left_command():
        print("\ninput(handleLeftCommand): Move left command received")
        pyautogui.press("left")
        print("input(handleLeftCommand): Move left command handled")

    def handle_right_command():
        print("\ninput(handleRightCommand): Move right command received")
        pyautogui.press("right")
        print("input(handleRightCommand): Move right command handled")

    def handle_a_command():
        print("\ninput(handleACommand): A command received")
        pyautogui.press("x")
        print("input(handleACommand): A command handled")

    def handle_b_command():
        print("\ninput(handleBCommand): B command received")
        pyautogui.press("z")
        print("input(handleBCommand): B command handled")

    def handle_y_command():
        print("\ninput(handleYCommand): Y command received")
        pyautogui.press("v")
        print("input(handleYCommand): Y command handled")

    def handle_x_command():
        print("\ninput(handleXCommand): X command received")
        pyautogui.press("c")
        print("input(handleXCommand): X command handled")

    def handle_start_command():
        print("\ninput(handleStartCommand): Start command received")
        pyautogui.press("enter")
        print("input(handleStartCommand): Start command handled")

    # Execute commands
    if command == "up":
        execute_command(handle_up_command)
    elif command == "down":
        execute_command(handle_down_command)
    elif command == "left":
        execute_command(handle_left_command)
    elif command == "right":
        execute_command(handle_right_command)
    elif command == "a":
        execute_command(handle_a_command)
    elif command == "b":
        execute_command(handle_b_command)
    elif command == "y":
        execute_command(handle_y_command)
    elif command == "x":
        execute_command(handle_x_command)
    elif command == "start":
        execute_command(handle_start_command)


# Twitch Bot Configuration
USERNAME = os.getenv("TWITCH_USERNAME")
PASSWORD = os.getenv("TWITCH_OAUTH_TOKEN")
SERVER = "irc.chat.twitch.tv"
PORT = 6667
CHANNEL = os.getenv("TWITCH_CHANNEL")
CHANNELS = [f"#{CHANNEL}"]

# Creating IRC client and connecting
reactor = irc.client.Reactor()
client = reactor.server()
client.connect(SERVER, PORT, USERNAME, password=PASSWORD)

# Adding event handlers
client.add_global_handler("welcome", on_connected)
client.add_global_handler("pubmsg", on_public_message)

# Starting the IRC client
thread = threading.Thread(target=reactor.process_forever)
thread.start()
