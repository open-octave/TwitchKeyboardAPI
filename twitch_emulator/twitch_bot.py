import logging

import irc.bot
import pydirectinput

from twitch_emulator.window_manager import WindowManager
from threading import Timer


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(
        self, channel, nickname="justinfan12345", server="irc.chat.twitch.tv", port=6667
    ):
        self.client = irc.bot.SingleServerIRCBot.__init__(
            self, [(server, port)], nickname, nickname
        )
        self.channel = "#" + channel
        self.windowManagerClient = WindowManager()

        self.currentlyHeldKey = None

    def on_welcome(self, connection, event):
        """
        This function will handle the bot connecting to the server. It will log the event.
        """
        logging.info(f"Joining channel: {self.channel}")

        # Request the "twitch.tv/tags" capability
        connection.cap("REQ", ":twitch.tv/tags")
        connection.join(self.channel)

    def on_join(self, connection, event):
        """
        This function will handle the bot joining the channel. It will log the event.
        """
        logging.info(f"Joined channel: {self.channel}")

    def on_pubmsg(self, connection, event):
        """
        This function will handle public messages sent in the chat. It will parse the message
        and execute the appropriate command.
        """

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
                "start": self.handle_start_command,
                "select": self.handle_select_command,
                "!hold": self.handle_hold_command,
                "!release": self.handle_stop_command,
                "!stop": self.handle_stop_command,
                "!toggle-fast-forward": self.handle_fast_forward_toggle_command,
                "!tff": self.handle_fast_forward_toggle_command,
                "!mod-kill-api": self.handle_mod_kill_api_command,
            }

            if command in commands:
                if self.currentlyHeldKey and command != "!stop":
                    self.handle_stop_command(event)

                self.execute_command(commands[command], event)
                logging.info(f"Command executed: {command}")

        except Exception as e:
            logging.error(f"Error processing public message: {e}")

    def execute_command(self, command_function, event):
        """
        This function will focus on the retroarch window and execute the command function
        passed in as a parameter.

        :param command_function: The function to execute
        :param message: The message to pass to the command function
        """

        try:
            logging.info("Focusing on window")
            self.windowManagerClient.focus_on_retroarch()
            logging.info("Window focused")

            logging.info(f"Executing command: {command_function.__name__}")
            command_function(event)
            logging.info(f"Command executed: {command_function.__name__}")

        except Exception as e:
            logging.error(f"Error executing command: {e}")

    def handle_up_command(self, event):
        """
        This function will handle the up command by pressing the up arrow key.
        Example message: "up"
        """

        try:
            logging.info("Move up command received")
            pydirectinput.press("up")
            logging.info("Move up command handled")
        except Exception as e:
            logging.error(f"Error handling up command: {e}")

    def handle_down_command(self, event):
        """
        This function will handle the down command by pressing the down arrow key.
        Example message: "down"
        """

        try:
            logging.info("Move down command received")
            pydirectinput.press("down")
            logging.info("Move down command handled")
        except Exception as e:
            logging.error(f"Error handling down command: {e}")

    def handle_left_command(self, event):
        """
        This function will handle the left command by pressing the left arrow key.
        Example message: "left"
        """

        try:
            logging.info("Move left command received")
            pydirectinput.press("left")
            logging.info("Move left command handled")
        except Exception as e:
            logging.error(f"Error handling left command: {e}")

    def handle_right_command(self, event):
        """
        This function will handle the right command by pressing the right arrow key.
        Example message: "right"
        """

        try:
            logging.info("Move right command received")
            pydirectinput.press("right")
            logging.info("Move right command handled")
        except Exception as e:
            logging.error(f"Error handling right command: {e}")

    def handle_a_command(self, event):
        """
        This function will handle the A command by pressing the X key.
        Example message: "a"
        """

        try:
            logging.info("A command received")
            pydirectinput.press("x")
            logging.info("A command handled")
        except Exception as e:
            logging.error(f"Error handling A command: {e}")

    def handle_b_command(self, event):
        """
        This function will handle the B command by pressing the Z key.
        Example message: "b"
        """

        try:
            logging.info("B command received")
            pydirectinput.press("z")
            logging.info("B command handled")
        except Exception as e:
            logging.error(f"Error handling B command: {e}")

    def handle_y_command(self, event):
        """
        This function will handle the Y command by pressing the A key.
        Example message: "y"
        """

        try:
            logging.info("Y command received")
            pydirectinput.press("a")
            logging.info("Y command handled")
        except Exception as e:
            logging.error(f"Error handling Y command: {e}")

    def handle_x_command(self, event):
        """
        This function will handle the X command by pressing the S key.
        Example message: "x"
        """

        try:
            logging.info("X command received")
            pydirectinput.press("s")
            logging.info("X command handled")
        except Exception as e:
            logging.error(f"Error handling X command: {e}")

    def handle_start_command(self, event):
        """
        This function will handle the start command by pressing the enter key.
        Example message: "!start"
        """

        try:
            logging.info("Start command received")
            pydirectinput.press("enter")
            logging.info("Start command handled")
        except Exception as e:
            logging.error(f"Error handling Start command: {e}")

    def handle_select_command(self, event):
        """
        This function will handle the select command by pressing the shift key.
        Example message: "!select"
        """

        try:
            logging.info("Select command received")
            pydirectinput.press("shift")
            logging.info("Select command handled")
        except Exception as e:
            logging.error(f"Error handling Select command: {e}")

    def handle_hold_command(self, event):
        """
        This function will hold a key down until a release command is received or
        the fallback timer of 30 seconds expires. For now this will only allow directional
        keys to be held down.

        Example message: "!hold up"
        """

        def timeout_release():
            logging.info(f"Timeout reached. Releasing key: {self.currentlyHeldKey}")
            self.handle_stop_command(event)

        try:
            if self.currentlyHeldKey:
                self.handle_stop_command(event)

            allowed_keys = ["up", "down", "left", "right"]

            message = event.arguments[0].strip().lower()
            args = message.split()
            key = args[1] if len(args) > 1 else None
            key = key.lower() if key else None

            if key in allowed_keys:
                logging.info(f"Hold command received: {key}")
                pydirectinput.keyDown(key)
                self.currentlyHeldKey = key

                # Set up the timer to automatically release the key after 30 seconds
                self.timer = Timer(30.0, timeout_release)
                self.timer.start()

                logging.info(f"Hold command handled: {key}")
            else:
                logging.error(f"Invalid key received: {key}")

        except Exception as e:
            logging.error(f"Error handling hold command: {e}")

    def handle_stop_command(self, event):
        """
        This function will release the key that is currently being held down.
        Example message: "!stop"
        """

        try:
            if not self.currentlyHeldKey:
                logging.error("No key is currently being held down")
                return

            logging.info("Release command received")
            pydirectinput.keyUp(self.currentlyHeldKey)
            self.currentlyHeldKey = None
            logging.info("Release command handled")

            # Cancel the timer if it is running
            if hasattr(self, "timer"):
                self.timer.cancel()

        except Exception as e:
            logging.error(f"Error handling release command: {e}")

    def handle_fast_forward_toggle_command(self, event):
        """
        This function will handle the fast forward toggle command by pressing the space key.
        Example message: "!fastForwardToggle"
        """

        try:
            logging.info("Fast forward toggle command received")
            pydirectinput.press("space")
            logging.info("Fast forward toggle command handled")
        except Exception as e:
            logging.error(f"Error handling fast forward toggle command: {e}")

    def handle_mod_kill_api_command(self, event):
        """
        This function will handle the mod kill API command by sending a POST request to the API.
        Example message: "!modKillAPI"
        """

        username = irc.strings.lower(event.source.nick)
        user_role = None

        if event.tags:
            tags = {kv["key"]: kv["value"] for kv in event.tags}

            if tags.get("mod") == "1":
                user_role = "moderator"
            elif tags.get("badges") and "broadcaster" in tags.get("badges"):
                user_role = "broadcaster"
            else:
                user_role = "viewer"
        else:
            user_role = "viewer"

        try:
            if user_role != "moderator" and user_role != "broadcaster":
                logging.error(
                    f"User {username} does not have permission to kill the API"
                )
                return

            logging.info(f"Mod kill API command received from: {username}")
            exit()
        except Exception as e:
            logging.error(f"Error handling mod kill API command: {e}")
