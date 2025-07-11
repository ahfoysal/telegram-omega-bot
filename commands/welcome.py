# commands/welcome.py

async def welcome_message(update, context):
    """
    Sends a welcome message when a user messages the bot DM.
    """
    await update.message.reply_text(
        "👋 Welcome to Softvence Omega KAM Bot!\n\n"
        "Here’s what I can do:\n\n"
        "/timeline [Client Name] - Get the timeline information for a specific client.\n"
        "/update <message> - Send a message to the central update group.\n\n"
        "/cupdate <message> - Send a message to the custom central update group.\n\n"
        "/wupdate <message> - Send a message to the central update group.\n\n"
        "Just send a command to get started!\n\n"
        "Made by Foysal 😉 "
    )
