import logging
import os

from pyfiglet import Figlet
from colorama import Fore, Style

from database import Configuration, session


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
    try:
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
            print(
                "Find the active virtual environment by running the following command:"
            )
            print("$ poetry env list")
            print("\n")
            print("Remove the virtual environment by running the following command:")
            print("$ poetry env remove <ACTIVE_VIRTUAL_ENVIRONMENT_NAME>")
            print("\n")
            print(
                "Reinitialize the virtual environment by running the following command:"
            )
            print("$ poetry install")
            print("\n")

            exit(1)

        # Verify that the file exists
        poetry_file_path = None

        # If on Windows
        if os.name == "nt":
            poetry_file_path = (
                ".venv\\Lib\\site-packages\\prompt_toolkit\\styles\\from_dict.py"
            )
        # Otherwise, if on Unix
        else:
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
                    "from collections import Mapping",
                    "from collections.abc import Mapping",
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
    except Exception as e:
        logging.error(f"Error fixing the PyInquirer dependency: {e}")
        exit(1)


def start_bot(channel):
    print(
        Fore.GREEN
        + f"\nStarting client to monitor {channel}'s channel for commands...\n"
    )

    # If the system is not windows, exit the program
    if os.name != "nt":
        logging.error(
            "This application is only supported on Windows. Please run the application on a Windows machine."
        )
        exit(1)

    from twitch_bot import TwitchBot

    twitch_bot = TwitchBot(channel)

    def start_twitch_listener():
        try:
            twitch_bot.start()
        except Exception as e:
            logging.error(f"Error starting the bot: {e}")

    start_twitch_listener()


def clear_output():
    os.system("cls" if os.name == "nt" else "clear")


def create_new_configuration():
    # Note: PyInquirer must be fixed before importing prompt
    from PyInquirer import prompt

    questions = [
        {
            "type": "input",
            "name": "channel",
            "message": "Enter your channel name:",
        }
    ]

    answers = prompt(questions)

    channel = answers["channel"]

    # Set all configurations to not be the last used configuration
    session.query(Configuration).update({Configuration.last_used: False})
    session.commit()

    # Create a new configuration
    new_configuration = Configuration(channel=channel, last_used=True)
    session.add(new_configuration)
    session.commit()

    start_bot(channel)


def handle_configuration_selection():
    # Note: PyInquirer must be fixed before importing prompt
    from PyInquirer import prompt

    # Check for existing configuration
    existing_configurations = session.query(Configuration).all()

    # If there are existing configurations
    has_existing_configurations = len(existing_configurations) > 0
    if has_existing_configurations:
        last_used_configuration = [
            config for config in existing_configurations if config.last_used
        ][0]

        questions = [
            {
                "type": "confirm",
                "name": "use_last_used",
                "message": f"Would you like to use your last used configuration for {last_used_configuration.channel}?",
                "default": True,
            }
        ]

        answers = prompt(questions)
        use_last_used = answers["use_last_used"]

        if use_last_used:
            start_bot(last_used_configuration.channel)
            return
        else:
            configuration_choices = [
                {"name": config.channel} for config in existing_configurations
            ]

            configuration_choices.append({"name": "Create a new configuration"})

            questions = [
                {
                    "type": "list",
                    "name": "channel",
                    "message": "Select a channel configuration:",
                    "choices": configuration_choices,
                }
            ]

            answers = prompt(questions)

            selected_channel = answers["channel"]

            if selected_channel != "Create a new configuration":
                # Set all configurations to not be the last used configuration
                session.query(Configuration).update({Configuration.last_used: False})
                session.commit()

                # Set the selected configuration to be the last used configuration
                selected_configuration = session.query(Configuration).filter_by(
                    channel=selected_channel
                )[0]

                selected_configuration.last_used = True
                session.commit()

                start_bot(selected_channel)
                return

    create_new_configuration()


if __name__ == "__main__":
    fix_pyinqurer_dependency()
    clear_output()

    # Print the title
    figlet = Figlet(font="smslant", width=100)
    print(Fore.MAGENTA + Style.BRIGHT + figlet.renderText("Twitch Keyboard API"))

    handle_configuration_selection()
