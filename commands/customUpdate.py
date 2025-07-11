from telegram import Update
from telegram.ext import ContextTypes

TARGET_GROUP_CHAT_ID = -4795892500


async def custom_update_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text or ""
    content_to_send = message_text.removeprefix("/update").strip()

    if not content_to_send:
        await update.message.reply_text("⚠️ Please provide a message to send to the group.")
        return

    # Get the chat title (name of the group or channel where the command was sent)
    chat_title = update.effective_chat.title or "Unknown Group"

    # Add line break and chat title
    content_to_send += f"\n\n— {chat_title}"

    try:
        await context.bot.send_message(chat_id=TARGET_GROUP_CHAT_ID, text=content_to_send)
        await update.message.reply_text("✅ Your Update message has been sent to the custom central update group.")
    except Exception as e:
        await update.message.reply_text(f"❌ Failed to send message: {e}")
