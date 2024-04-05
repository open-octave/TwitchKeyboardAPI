# Emulator API for Twitch (EAT)

EAT is an API that will monitor incoming commands from a Twitch chat and send them to a game emulator.

<img src="./.github/images//example.png">

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Poetry

### Step 1: Emulator Installation

1. Download the DeSmuME emulator from the [official website](https://www.desmume.com/download.htm).
2. Download the `.nds` ROM of the game you want to play. You can find a list of games [here](https://www.emulatorgames.net/roms/nintendo-ds/).

### Step 2: API Configuration

1. Create a `.env` file in the root of the project and add the following environment variables:

```bash
TWITCH_USERNAME="your_twitch_username"
TWITCH_OAUTH_TOKEN="your_twitch_oauth_token"
```

_**Note:** You can get your Twitch OAuth token [here](https://twitchapps.com/tmi/)._

### Step 3: API Initialization

1. Clone the repository

```bash
git clone git@github.com:open-octave/emulator-api-for-twitch.git
```

2. Install the dependencies

```bash
poetry install
```

3. Run the API

```bash
poetry run python twitch_emulator
```

### Step 4: Emulator Initialization

1. Open the DeSmuME emulator.
2. Go to `File > Open ROM` and select the `.nds` ROM of the game you want to play.

### Step 5: Twitch Chat

1. Open the Twitch chat and type the following command:

```bash
start
```

2. From here you should automatically start receiving commands from the Twitch chat to the emulator. The API will auto focus on to use the command whenever a command is received.

## License

Distributed under the GNU General Public License. See `LICENSE` for more information.
