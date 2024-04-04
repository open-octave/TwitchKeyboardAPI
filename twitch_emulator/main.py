import irc.client
import irc.events
import pyautogui
import threading


def on_connected(connection, event):
    for channel in CHANNELS:
        connection.join(channel)
    print(f"* Connected to Twitch")


def on_public_message(connection, event):
    message = event.arguments[0].strip().lower()
    args = message.split()

    command = args[0] if args else None
    command = command.lower()

    # Define command functions
    def handle_up_command():
        print("\ninput(handleUpCommand): Move up command received")
        pyautogui.press("up")
        print("input(handleUpCommand): Move up command handled")

    def handle_down_command():
        print("\ninput(handleDownCommand): Move down command received")
        pyautogui.press("down")
        print("input(handleDownCommand): Move down command handled")

    def handle_left_command():
        print("\ninput(handleLeftCommand): Move left command received")
        pyautogui.press("left")
        print("input(handleLeftCommand): Move left command handled")

    def handle_right_command():
        print("\ninput(handleRightCommand): Move right command received")
        pyautogui.press("right")
        print("input(handleRightCommand): Move right command handled")

    def handle_a_command():
        print("\ninput(handleACommand): A command received")
        pyautogui.press("x")
        print("input(handleACommand): A command handled")

    def handle_b_command():
        print("\ninput(handleBCommand): B command received")
        pyautogui.press("z")
        print("input(handleBCommand): B command handled")

    def handle_y_command():
        print("\ninput(handleYCommand): Y command received")
        pyautogui.press("v")
        print("input(handleYCommand): Y command handled")

    def handle_x_command():
        print("\ninput(handleXCommand): X command received")
        pyautogui.press("c")
        print("input(handleXCommand): X command handled")

    # Execute commands
    if command == "up":
        handle_up_command()
    elif command == "down":
        handle_down_command()
    elif command == "left":
        handle_left_command()
    elif command == "right":
        handle_right_command()
    elif command == "a":
        handle_a_command()
    elif command == "b":
        handle_b_command()
    elif command == "y":
        handle_y_command()
    elif command == "x":
        handle_x_command()


"""
Controls: up, down, left, right, a, b, y, x
"""


# Twitch Bot Configuration
USERNAME = "PCDSandwichBot"  # Your Twitch username
PASSWORD = "oauth:h22c4i285dmdszvbkxgvfivi5v3d7q"  # Your Twitch OAuth token
SERVER = "irc.chat.twitch.tv"
PORT = 6667
CHANNELS = ["#pcdsandwichman"]

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
