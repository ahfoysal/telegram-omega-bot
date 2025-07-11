import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from core.config import TELEGRAM_BOT_TOKEN
from commands.timeline import timeline_command
from commands.update import update_command
from commands.wixbuddyupdate import wix_update_command
from commands.customUpdate import custom_update_command
from commands.getChatId import getId_command
from commands.welcome import welcome_message  # Import the new welcome handler
from handlers.error_handler import error_handler

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("timeline", timeline_command))
    app.add_handler(CommandHandler("update", update_command))
    app.add_handler(CommandHandler("cupdate", custom_update_command))
    app.add_handler(CommandHandler("wupdate", wix_update_command))
    app.add_handler(CommandHandler("getid", getId_command))

    # Add a message handler for private chats only
    app.add_handler(MessageHandler(
        filters.TEXT & filters.ChatType.PRIVATE, welcome_message))

    app.add_error_handler(error_handler)

    logger.info("🤖 Bot is running...")
    app.run_polling()
