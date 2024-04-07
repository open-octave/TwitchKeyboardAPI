import logging
import threading

import irc.client
import irc.events
import pyautogui

from twitch_emulator.window_manager import WindowManager


class TwitchBot:
    def __init__(self, username, password, server, port, channels):
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.channels = channels
        self.reactor = irc.client.Reactor()
        self.client = self.reactor.server()
        self.windowManagerClient = WindowManager("DeSmuME")

    def start(self):
        try:
            self.client.connect(
                self.server, self.port, self.username, password=self.password
            )
            self.client.add_global_handler("welcome", self.on_connected)
            self.client.add_global_handler("pubmsg", self.on_public_message)
            thread = threading.Thread(target=self.reactor.process_forever)
            thread.start()
        except Exception as e:
            logging.error(f"Failed to start IRC client: {e}")

    def on_connected(self, connection, event):
        try:
            for channel in self.channels:
                connection.join(channel)
            logging.info("* Connected to Twitch")
        except Exception as e:
            logging.error(f"Error connecting to Twitch: {e}")

    def execute_command(self, command_function):
        try:
            logging.info("Focusing on window")
            self.windowManagerClient.focus_on_window()
            logging.info("Window focused")

            logging.info(f"Executing command: {command_function.__name__}")
            command_function()
            logging.info(f"Command executed: {command_function.__name__}")

        except Exception as e:
            logging.error(f"Error executing command: {e}")

    def handle_up_command(self):
        try:
            logging.info("Move up command received")
            pyautogui.press("up")
            logging.info("Move up command handled")
        except Exception as e:
            logging.error(f"Error handling up command: {e}")

    def handle_down_command(self):
        try:
            logging.info("Move down command received")
            pyautogui.press("down")
            logging.info("Move down command handled")
        except Exception as e:
            logging.error(f"Error handling down command: {e}")

    def handle_left_command(self):
        try:
            logging.info("Move left command received")
            pyautogui.press("left")
            logging.info("Move left command handled")
        except Exception as e:
            logging.error(f"Error handling left command: {e}")

    def handle_right_command(self):
        try:
            logging.info("Move right command received")
            pyautogui.press("right")
            logging.info("Move right command handled")
        except Exception as e:
            logging.error(f"Error handling right command: {e}")

    def handle_a_command(self):
        try:
            logging.info("A command received")
            pyautogui.press("x")
            logging.info("A command handled")
        except Exception as e:
            logging.error(f"Error handling A command: {e}")

    def handle_b_command(self):
        try:
            logging.info("B command received")
            pyautogui.press("z")
            logging.info("B command handled")
        except Exception as e:
            logging.error(f"Error handling B command: {e}")

    def handle_y_command(self):
        try:
            logging.info("Y command received")
            pyautogui.press("v")
            logging.info("Y command handled")
        except Exception as e:
            logging.error(f"Error handling Y command: {e}")

    def handle_x_command(self):
        try:
            logging.info("X command received")
            pyautogui.press("c")
            logging.info("X command handled")
        except Exception as e:
            logging.error(f"Error handling X command: {e}")

    def handle_start_command(self):
        try:
            logging.info("Start command received")
            pyautogui.press("enter")
            logging.info("Start command handled")
        except Exception as e:
            logging.error(f"Error handling Start command: {e}")

    def on_public_message(self, connection, event):
        try:
            message = event.arguments[0].strip().lower()
            args = message.split()

            command = args[0] if args else None
            command = command.lower() if command else None

            commands = {
                "up": self.handle_up_command,
                "down": self.handle_down_command,
                "left": self.handle_left_command,
                "right": self.handle_right_command,
                "a": self.handle_a_command,
                "b": self.handle_b_command,
                "y": self.handle_y_command,
                "x": self.handle_x_command,
                "start": self.handle_start_command,
            }

            if command in commands:
                self.execute_command(commands[command])
                logging.info(f"Command executed: {command}")

        except Exception as e:
            logging.error(f"Error processing public message: {e}")
