# ⚠️ WARNING ⚠️

> This bot is intended for **educational purposes only**. It is **not guaranteed to work** as intended, and its use may violate the terms of service of Rainbow Six Siege. By using this tool, you acknowledge and accept **full responsibility** for any consequences. The author **is not responsible** for any misuse or issues arising from the use of this bot. This tool is provided "as-is" without warranty of any kind.

# Clusternown Renown Bot

This bot is designed to automate actions in Rainbow Six Siege to help users gain renown while AFK (away from keyboard). It performs automated tasks such as launching the game, entering matches, configuring settings, and retrying games to maximize renown earnings.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [Customization](#customization)
- [License](#license)

## Features

- **Automated Renown Farming**: Automates the process of joining and rejoining matches to accumulate renown while the user is AFK.
- **Automated Game Launch**: Detects and launches Rainbow Six Siege through Steam or Ubisoft.
- **In-Match Actions**: Automates entering training matches, setting locations, and selecting operators.
- **Auto-Retry**: Automatically retries after match completion.
- **HWID Whitelisting**: Only authorized users can run the bot (checked against a remote HWID list).
- **Console Interface**: Uses `rich` for styled console output with success, error, and process messages.

## Requirements

This app requires Python 3.10 and the following libraries:

- `pydirectinput`
- `pyautogui`
- `rich`
- `Pillow`
- `requests`
- `psutil`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mhmdxsadk/Clusternown.git
   ```
2. Navigate to the directory:
   ```bash
   cd Clusternown
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script to start the bot:
   ```bash
   python main.py
   ```
2. If you’re whitelisted, the bot will launch Rainbow Six Siege based on your platform (Steam or Ubisoft) and enter a match.
3. The bot will automatically configure match settings, including:
   - Selecting the game mode and operator.
   - Setting up loadouts and other configurations.
   - Automatically retrying a new match after completion.

### Command Line Interface

- **Welcome Screen**: Displays the bot’s logo, author, and version.
- **Status Messages**: Uses color-coded messages to display the status of each process (e.g., locating images, starting matches).
- **Elapsed Time**: Calculates and displays the total time the bot was running upon exit.

### Keyboard Interrupt

- Press `Ctrl + C` to safely exit the bot during runtime.

## Disclaimer

This bot is intended for **educational purposes only** and is not guaranteed to work as intended. Use of this bot may violate the terms of service of Rainbow Six Siege, and by using this tool, you acknowledge and accept full responsibility for any consequences. The author **is not responsible** for any misuse or issues arising from the use of this bot. This tool is provided "as-is" without warranty of any kind.

## Customization

- Modify image assets or paths if you have different images for the bot's UI interactions.
- Customize the theme colors for console messages in the `Theme` configuration within `theme = Theme({...})`.
- Adjust the image confidence level for screen detection if you encounter issues with image recognition.

## License

This project is licensed under a custom license. Please review the [LICENSE](LICENSE) file for terms and conditions.
