# Emulator API for Twitch (EAT) - For Windows

EAT is an API that will monitor incoming commands from a Twitch chat and send them to a game emulator.

<img src="./.github/images/example.png">

## Table of Contents

- [Emulator API for Twitch (EAT) - For Windows](#emulator-api-for-twitch-eat---for-windows)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Step 1: Emulator Installation](#step-1-emulator-installation)
    - [Step 2: API Initialization](#step-2-api-initialization)
    - [Step 3: Using the API](#step-3-using-the-api)
  - [Commands](#commands)
  - [License](#license)

## Getting Started

### Prerequisites

- Python 3.11.9
- Poetry
- Windows 10 / Windows 11

### Step 1: Emulator Installation

_**Note:** For the sake of this example, assume you are downloading a Nintendo DS game but the process is similar for other consoles._

1. Download the RetroArch game emulator from the [official website](https://www.retroarch.com/?page=platforms).
2. Open the RetroArch emulator.
3. Go to `Load Core`.
   <div><img width="500" src="./.github/images/step-load-core.png"></div>
4. Select `Download a Core`.
   <div><img width="500" src="./.github/images/step-download-core.png"></div>
5. Select the `Nintendo - Nintendo DS (melonDS)` core.
   <div><img width="500" src="./.github/images/step-core-select.png"></div>
6. Download the `.nds` ROM of the game you want to play. You can find a list of
games. [here](https://www.emulatorgames.net/roms/nintendo-ds/).
   <div><img width="500" src="./.github/images/step-download-rom.png"></div>
7. Go to `Load Content`.
   <div><img width="500" src="./.github/images/step-load-content.png"></div>
8. Select `Start Directory`.
   <div><img width="500" src="./.github/images/step-start-directory.png"></div>
9. Find and select the folder where the `.nds` ROM is located.
   <div><img width="500" src="./.github/images/step-select-the-rom.png"></div>
10. You should now be able to play the game using the emulator.
<div><img width="500" src="./.github/images/step-game-preview.png"></div>

### Step 2: API Initialization

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
poetry run python ./twitch_emulator/__main__.py
```

### Step 3: Using the API

1. Go to the Twitch chat and type a command
2. The API will receive the command and send it to the emulator

| On Start Example                                                                 | Command Example                                                                   |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| <div><img width="500" src="./.github/images/step-example-pre-message.png"></div> | <div><img width="500" src="./.github/images/step-example-post-message.png"></div> |

## Commands

_**Note:** The command mapping is designed based on the default key bindings of the RetroArch emulator._

| Command | Description                       |
| ------- | --------------------------------- |
| `up`    | Simulates a up arrow key press    |
| `down`  | Simulates a down arrow key press  |
| `left`  | Simulates a left arrow key press  |
| `right` | Simulates a right arrow key press |
| `a`     | Simulates an X key press          |
| `b`     | Simulates a Z key press           |
| `x`     | Simulates an S key press          |
| `y`     | Simulates an A key press          |

## License

Distributed under the GNU General Public License. See `LICENSE` for more information.
