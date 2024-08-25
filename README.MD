# Selfbot README

## Disclaimer

**Use of selfbots is against Discord's Terms of Service (ToS)**, and using this selfbot may result in your account being banned or terminated. Proceed at your own risk.

## Requirements

- **Python 3.8 or higher**: Ensure Python is installed on your system.

## Installation

### 1. Download and Install Python

1. Go to the [official Python website](https://www.python.org/downloads/).
2. Download the latest version of Python (3.8 or higher).
3. During installation, ensure you check the box that says "Add Python to PATH".

### 2. Clone the Repository

Clone this repository to your local machine using:
bash
git clone <repository_url>
Alternatively, download the ZIP file and extract it.

## 3. Install Required Packages

Navigate to the directory where you cloned or extracted the repository and run:

bash

```py
pip install -r requirements.txt
```

## Configuration

Open the `config.json` file in a text editor.
Replace the placeholders with your actual values

```json
{
    "token": "your_token_here",
    "prefix": "the_prefix_you_want_here (e.g., ?, !, , etc.)",
    "user_id": "your_user_id_here",
    "delay": "time_between_sending_messages_in_seconds (e.g., 2)"
}
```

1. token: Your Discord token. You can get this from your Discord client (note: this is against Discord's ToS).
2. prefix: The prefix for your commands (e.g., !, ?, ,).
3. user_id: Your Discord user ID. You can get this by enabling Developer Mode in Discord and right-clicking your profile.
4. delay: The time (in seconds) between sending and clearing messages.

## Running the Selfbot

Once you've configured everything, you can run the selfbot with:
python `main.py`

## Commands

1. ping: Responds with "pong"
2. send [text]: Sends the specified text repeatedly or random characters if no text is specified.
3. Stops the repeated message sending
4. restart: Restarts the bot.
5. clear [limit]: Deletes up to 1000 of your previous messages in the channel.

Note: Only the user with the specified user ID can use these commands.

## Legal Disclaimer

This selfbot is for educational purposes only. The use of selfbots violates Discord's Terms of Service, and by using this software, you assume full responsibility for any actions taken.
