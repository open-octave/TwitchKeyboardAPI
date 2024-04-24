import logging
import threading

import irc.bot
import pyautogui

from twitch_emulator.window_manager import WindowManager


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(
        self, channel, nickname="justinfan12345", server="irc.chat.twitch.tv", port=6667
    ):
        self.client = irc.bot.SingleServerIRCBot.__init__(
            self, [(server, port)], nickname, nickname
        )
        self.channel = "#" + channel

    def on_welcome(self, connection, event):
        logging.info(f"Joining channel: {self.channel}")
        connection.join(self.channel)

    def on_join(self, connection, event):
        logging.info(f"Joined channel: {self.channel}")

    def on_pubmsg(self, connection, event):
        author = irc.strings.lower(event.source.nick)
        message = event.arguments[0]
        logging.info(f"{author}: {message}")

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
            }

            if command in commands:
                self.execute_command(commands[command])
                logging.info(f"Command executed: {command}")

        except Exception as e:
            logging.error(f"Error processing public message: {e}")

    def execute_command(self, command_function):
        try:
            # logging.info("Focusing on window")
            # self.windowManagerClient.focus_on_window()
            # logging.info("Window focused")

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
