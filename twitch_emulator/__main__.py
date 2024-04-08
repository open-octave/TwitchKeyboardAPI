import logging
import os

from dotenv import load_dotenv

from twitch_emulator.twitch_bot import TwitchBot

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
load_dotenv()

USERNAME = os.getenv("TWITCH_USERNAME")
PASSWORD = os.getenv("TWITCH_OAUTH_TOKEN")
SERVER = "irc.chat.twitch.tv"
PORT = 6667
CHANNEL = os.getenv("TWITCH_CHANNEL")
CHANNELS = [f"#{CHANNEL}"]

twitch_bot = TwitchBot(USERNAME, PASSWORD, SERVER, PORT, CHANNELS)


def start_twitch_listener():
    try:
        twitch_bot.start()
    except Exception as e:
        logging.error(f"Error starting the bot: {e}")


def stop_twitch_listener():
    try:
        twitch_bot.stop()
    except Exception as e:
        logging.error(f"Error stopping the bot: {e}")


if __name__ == "__main__":
    start_twitch_listener()
