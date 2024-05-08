#!/bin/bash

# Verify that Python is installed
if ! command -v python &>/dev/null; then
    echo "Python could not be found, please install Python."
    exit
fi

# Verify that Poetry is installed
if ! command -v poetry &>/dev/null; then
    echo "Poetry could not be found, installing Poetry..."
    curl -sSL https://install.python-poetry.org | python -
fi

# Install dependencies using Poetry
poetry install

# Run the Twitch Keyboard API
poetry run python ./twitch_keyboard_api/__main__.py
