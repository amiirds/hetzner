
import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from hcloud import Client

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
HETZNER_API_TOKEN = os.getenv('HETZNER_API_TOKEN')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Hetzner Client
hetzner_client = Client(token=HETZNER_API_TOKEN)

# Command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to Hetzner Bot! Use /servers to list servers.')

def list_servers(update: Update, context: CallbackContext) -> None:
    try:
        servers = hetzner_client.servers.get_all()
        if servers:
            server_list = "\n".join([f"{server.name}: {server.server_type.name}" for server in servers])
            update.message.reply_text(f"Available Servers:\n{server_list}")
        else:
            update.message.reply_text("No servers found.")
    except Exception as e:
        logger.error(e)
        update.message.reply_text("Failed to fetch servers.")

def reboot_server(update: Update, context: CallbackContext) -> None:
    try:
        server_id = context.args[0]
        server = hetzner_client.servers.get_by_id(server_id)
        action = server.reboot()
        update.message.reply_text(f"Rebooting server {server.name}. Action ID: {action.id}")
    except IndexError:
        update.message.reply_text("Please provide a server ID.")
    except Exception as e:
        logger.error(e)
        update.message.reply_text("Failed to reboot server.")

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("servers", list_servers))
    dispatcher.add_handler(CommandHandler("reboot", reboot_server))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
