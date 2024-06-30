
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from hcloud import Client

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Hetzner Client
hetzner_client = Client(token='vedLUPTTuIJHgaA1Q6SaqfWiqdftFXb1icEmcNvmXcnCabZ0WIRmInqPOiMoVgnc')

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to Hetzner Bot! Use /servers to list servers.')

def list_servers(update: Update, context: CallbackContext) -> None:
    servers = hetzner_client.servers.get_all()
    if servers:
        server_list = "\n".join([f"{server.name}: {server.server_type.name}" for server in servers])
        update.message.reply_text(f"Available Servers:\n{server_list}")
    else:
        update.message.reply_text("No servers found.")

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("7088808732:AAEShKRVWDdmHk1JFiy2SjvQj2ySAl3YVM8")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("servers", list_servers))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
