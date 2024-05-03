import logging
import os

from twitch_emulator.twitch_bot import TwitchBot
from twitch_emulator.window_manager import WindowManager
from pyfiglet import Figlet
from colorama import Fore, Style


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def fix_pyinqurer_dependency():
    """
    Fixing the PyInquirer dependency issue with prompt_toolkit. For python version "3.10.5"
    and on "from collections import Mapping" should be replaced with "from collections.abc import Mapping"
    inside of ".venv/Lib/site-packages/prompt_toolkit/styles/from_dict.py"

    xref: https://github.com/CITGuru/PyInquirer/issues/181#issuecomment-1164706118
    """

    # Verify that .venv exists in the current directory
    if not os.path.exists(".venv"):
        logging.error(
            "The .venv directory does not locally exist. Please ensure that your virtual environment is set up to install the dependencies in your current directory."
        )

        print("\n")
        print("To resolve this issue you can try the following...")
        print("\n")
        print(
            "Configure poetry to create virtual environments in the project directory:"
        )
        print("$ poetry config virtualenvs.in-project true")
        print("\n")
        print("Find the active virtual environment by running the following command:")
        print("$ poetry env list")
        print("\n")
        print("Remove the virtual environment by running the following command:")
        print("$ poetry env remove <ACTIVE_VIRTUAL_ENVIRONMENT_NAME>")
        print("\n")
        print("Reinitialize the virtual environment by running the following command:")
        print("$ poetry install")
        print("\n")

        exit(1)

    # Verify that the file exists
    poetry_file_path = (
        ".venv/lib/python3.11/site-packages/prompt_toolkit/styles/from_dict.py"
    )

    if not os.path.exists(poetry_file_path):
        logging.error(
            "The file 'from_dict.py' does not exist in the 'prompt_toolkit/styles' directory within the .venv directory. We need access to this file to fix the dependency issue."
        )
        exit(1)

    # Open the file and read the contents
    with open(poetry_file_path, "r") as file:
        contents = file.read()

        # Fix the dependency issue if it exists
        if "from collections import Mapping" in contents:
            contents = contents.replace(
                "from collections import Mapping", "from collections.abc import Mapping"
            )

            # Write the updated contents back to the file
            with open(poetry_file_path, "w") as file:
                file.write(contents)

            logging.info(
                "The dependency issue with PyInquirer has been fixed. You can now run the application."
            )
        else:
            logging.info(
                "The dependency issue with PyInquirer has already been fixed. You can now run the application."
            )


if __name__ == "__main__":
    # Fix the PyInquirer dependency issue
    try:
        fix_pyinqurer_dependency()
    except Exception as e:
        logging.error(f"Error fixing the PyInquirer dependency: {e}")
        exit(1)

    from PyInquirer import prompt

    # Clear any previous terminal output
    os.system("cls" if os.name == "nt" else "clear")

    figlet = Figlet(font="smslant", width=100)

    print(Fore.MAGENTA + Style.BRIGHT + figlet.renderText("Twitch Keyboard API"))

    questions = [
        {
            "type": "input",
            "name": "channel",
            "message": "Enter your channel name:",
        }
    ]

    answers = prompt(questions)

    channel = answers["channel"]

    print(
        Fore.GREEN
        + f"\nStarting client to monitor {channel}'s channel for commands...\n"
    )

    twitch_bot = TwitchBot(channel)

    def start_twitch_listener():
        try:
            twitch_bot.start()
        except Exception as e:
            logging.error(f"Error starting the bot: {e}")

    start_twitch_listener()
