
# Hetzner Telegram Bot

A simple Telegram bot to interface with Hetzner cloud servers.

## Setup

### Using Docker

1. Build and run the container:
    ```sh
    docker-compose up --build
    ```

### Using Python

1. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
2. Set your environment variables in a `.env` file.
3. Run the bot:
    ```sh
    python bot.py
    ```

## Commands

- `/start`: Welcome message.
- `/servers`: List all available servers.
- `/reboot <server_id>`: Reboot a server by its ID.
