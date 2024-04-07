import logging
import os

from dotenv import load_dotenv

from twitch_emulator.twitch_bot import TwitchBot

if __name__ == "__main__":
    try:
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
        twitch_bot.start()
    except Exception as e:
        logging.error(f"Error starting the bot: {e}")
else:
    logging.error("This script should be run as a standalone script")
