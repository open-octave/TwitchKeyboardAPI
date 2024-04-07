import logging
import os
import subprocess
import sys
import threading

import irc.client
import irc.events
import pyautogui
import pygetwindow as gw
from dotenv import load_dotenv

# Setup basic configuration for logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Attempt to load environment variables; exit if .env file is missing or malformed
try:
    load_dotenv()
except Exception as e:
    logging.error(f"Error loading .env file: {e}")
    sys.exit(1)

# Ensure that the necessary environmental variables are present
for var in ["TWITCH_USERNAME", "TWITCH_OAUTH_TOKEN", "TWITCH_CHANNEL"]:
    if not os.getenv(var):
        logging.error(f"Error: {var} is not set in .env file.")
        sys.exit(1)


def focus_on_desmume():
    if sys.platform == "darwin":
        try:
            script = """/usr/bin/osascript -e 'tell app "DeSmuME" to activate' """
            subprocess.run(script, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error focusing on DeSmuME on macOS: {e}")
    elif sys.platform == "win32":
        try:
            windows = gw.getWindowsWithTitle("DeSmuME")
            if windows:
                windows[0].activate()
            else:
                logging.info("DeSmuME window not found.")
        except Exception as e:
            logging.error(f"Error focusing on DeSmuME on Windows: {e}")


def execute_command(command_function):
    try:
        focus_on_desmume()
        command_function()
    except Exception as e:
        logging.error(f"Error executing command: {e}")


def on_connected(connection, event):
    try:
        for channel in CHANNELS:
            connection.join(channel)
        logging.info(f"* Connected to Twitch")
    except Exception as e:
        logging.error(f"Error connecting to Twitch: {e}")


def on_public_message(connection, event):
    try:
        message = event.arguments[0].strip().lower()
        args = message.split()

        command = args[0] if args else None
        command = command.lower() if command else None

        def handle_up_command():
            try:
                logging.info("Move up command received")
                pyautogui.press("up")
                logging.info("Move up command handled")
            except Exception as e:
                logging.error(f"Error handling up command: {e}")

        def handle_down_command():
            try:
                logging.info("Move down command received")
                pyautogui.press("down")
                logging.info("Move down command handled")
            except Exception as e:
                logging.error(f"Error handling down command: {e}")

        def handle_left_command():
            try:
                logging.info("Move left command received")
                pyautogui.press("left")
                logging.info("Move left command handled")
            except Exception as e:
                logging.error(f"Error handling left command: {e}")

        def handle_right_command():
            try:
                logging.info("Move right command received")
                pyautogui.press("right")
                logging.info("Move right command handled")
            except Exception as e:
                logging.error(f"Error handling right command: {e}")

        def handle_a_command():
            try:
                logging.info("A command received")
                pyautogui.press("x")
                logging.info("A command handled")
            except Exception as e:
                logging.error(f"Error handling A command: {e}")

        def handle_b_command():
            try:
                logging.info("B command received")
                pyautogui.press("z")
                logging.info("B command handled")
            except Exception as e:
                logging.error(f"Error handling B command: {e}")

        def handle_y_command():
            try:
                logging.info("Y command received")
                pyautogui.press("v")
                logging.info("Y command handled")
            except Exception as e:
                logging.error(f"Error handling Y command: {e}")

        def handle_x_command():
            try:
                logging.info("X command received")
                pyautogui.press("c")
                logging.info("X command handled")
            except Exception as e:
                logging.error(f"Error handling X command: {e}")

        def handle_start_command():
            try:
                logging.info("Start command received")
                pyautogui.press("enter")
                logging.info("Start command handled")
            except Exception as e:
                logging.error(f"Error handling Start command: {e}")

        commands = {
            "up": handle_up_command,
            "down": handle_down_command,
            "left": handle_left_command,
            "right": handle_right_command,
            "a": handle_a_command,
            "b": handle_b_command,
            "y": handle_y_command,
            "x": handle_x_command,
            "start": handle_start_command,
        }

        if command in commands:
            execute_command(commands[command])
            logging.info(f"Command executed: {command}")

    except Exception as e:
        logging.error(f"Error processing public message: {e}")


# Twitch Bot Configuration
USERNAME = os.getenv("TWITCH_USERNAME")
PASSWORD = os.getenv("TWITCH_OAUTH_TOKEN")
SERVER = "irc.chat.twitch.tv"
PORT = 6667
CHANNEL = os.getenv("TWITCH_CHANNEL")
CHANNELS = [f"#{CHANNEL}"]


if __name__ == "__main__":
    try:
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
    except Exception as e:
        logging.error(f"Failed to start IRC client: {e}")
