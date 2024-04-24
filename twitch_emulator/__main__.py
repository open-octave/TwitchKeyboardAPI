import logging

from twitch_emulator.twitch_bot import TwitchBot


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

CHANNEL = "pcdsandwichman"

twitch_bot = TwitchBot(CHANNEL)


def start_twitch_listener():
    try:
        twitch_bot.start()
    except Exception as e:
        logging.error(f"Error starting the bot: {e}")


if __name__ == "__main__":
    start_twitch_listener()
