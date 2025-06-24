⚠️ **IMPORTANT WARNING** ⚠️

This bot is created solely for **educational purposes** to demonstrate how to interact with the Telegram Bot API for sending messages.

**DO NOT USE THIS BOT FOR ACTUAL SPAMMING!**

*   **Spamming violates Telegram's Terms of Service.**
*   **Your bot will be quickly banned.**
*   **Your personal account used to create the bot may also be restricted or banned.**
*   **It is unethical and annoys users.**

**You are solely responsible for any misuse of this code.**

---
## Description  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python 3.7+"></a>

A simple Telegram bot written in Python using the `python-telegram-bot` library. The bot allows the "owner" to send a specified number of messages to a specific Telegram user by their User ID.

**Key Features:**
*   Send multiple messages via a command.
*   Specify the target user's ID.
*   Specify the number of messages and their text.
*   The command is only available to the bot "owner" (owner's ID is specified in the code).
*   Basic error handling (e.g., if the user has blocked the bot or API limits are exceeded).

## Prerequisites

*   Python 3.7+
*   pip (Python package installer)

## Installation

1.  **Clone the repository (or just download `bot.py`):**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd <YOUR_REPOSITORY_FOLDER_NAME>
    ```

2.  **Install dependencies:**
    ```bash
    pip install python-telegram-bot --upgrade
    ```

## Configuration

Before running the bot, you need to configure two parameters in the `bot.py` file:

1.  **`BOT_TOKEN`**: Your Telegram bot token.
    *   Obtain it from [@BotFather](https://t.me/BotFather) on Telegram by creating a new bot.
    ```python
    # In bot.py
    BOT_TOKEN = "YOUR_BOT_TOKEN" # <-- REPLACE WITH YOUR TOKEN
    ```

2.  **`OWNER_ID`**: Your Telegram User ID (numeric).
    *   You can find your User ID using a bot like [@userinfobot](https://t.me/userinfobot). This ID determines who can use the `/spam` command.
    ```python
    # In bot.py
    OWNER_ID = 123456789 # <-- REPLACE WITH YOUR User ID
    ```

## Running the Bot

After installation and configuration, run the bot with the command:

```bash
python bot.py
```

You should see a message in the console like `INFO:__main__:Бот запущен...` (or the localized equivalent from your Python script's logging, e.g., `INFO:__main__:Bot started...`).

## Usage

1.  **Start the bot:** Find your bot on Telegram and send it the `/start` command.
    ```
    /start
    ```
    The bot will reply with a welcome message and instructions on how to use the `/spam` command.

2.  **Send messages (only for `OWNER_ID`):**
    Use the `/spam` command in the following format:
    ```
    /spam <target_user_id> <number_of_messages> <message_text>
    ```
    *   `<target_user_id>`: The numeric User ID of the user you want to send messages to.
    *   `<number_of_messages>`: The number of messages to send.
    *   `<message_text>`: The text that will be sent.

    **Example:**
    ```
    /spam 987654321 5 Hello, this is a test message!
    ```
    This command will send 5 messages with the text "Hello, this is a test message!" to the user with ID `987654321`.

    **Important:**
    *   The bot can only send a message to a user if that user **has interacted with your bot at least once** (e.g., sent `/start`) or if the user's privacy settings allow receiving messages from bots they haven't added.
    *   A limit on the maximum number of messages per call (e.g., 20) is set in the code for demonstration purposes to reduce the risk of an immediate ban.
    *   A small delay (`asyncio.sleep(1.1)`) is implemented between message sends to try and respect Telegram API limits (no more than 1 message per second to the same chat).

## Telegram API Limits

Telegram has strict limits on how frequently bots can send messages:
*   No more than ~30 messages per minute to different chats.
*   No more than 1 message per second to the same chat.

Exceeding these limits will cause your bot to receive a `Retry after X seconds` error, and message sending will be temporarily unavailable. Excessive and systematic violation of these limits will lead to your bot being banned.

## Disclaimer

This project is provided "as is", without any warranty. The developer is not responsible for any use of this code, especially for violating Telegram's rules or any other illegal activities. Use at your own risk and **only for educational purposes**.
