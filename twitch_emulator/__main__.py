import logging
import os


from twitch_emulator.twitch_bot import TwitchBot
from twitch_emulator.window_manager import WindowManager


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    # Clear any previous terminal output
    os.system("cls" if os.name == "nt" else "clear")

    channel = input("Enter your channel name: ")

    twitch_bot = TwitchBot(channel)

    def start_twitch_listener():
        try:
            twitch_bot.start()
        except Exception as e:
            logging.error(f"Error starting the bot: {e}")

    start_twitch_listener()
