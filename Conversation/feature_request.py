import os
from dotenv import load_dotenv
from typing import Final
from telegram import Update
from telegram.ext import ContextTypes ,ConversationHandler


load_dotenv()
ADMIN_CHAT_ID : Final = int(os.getenv("ADMIN_CHAT_ID"))

FEATURE = 1
async def newf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "What feature would you like to suggest ?\n\n"
        "Type /cancel to cancel."
    )

    return FEATURE

async def receive_feature(update: Update, context: ContextTypes.DEFAULT_TYPE):

    suggestion = update.message.text

    user = update.effective_user

    message = (
        "📩 New Feature Suggestion\n\n"
        f"👤 Name: {user.full_name}\n"
        f"🆔 ID: {user.id}\n"
        f"📛 Username: @{user.username}\n\n"
        f"💡 Suggestion:\n<< {suggestion} >>"
    )

    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=message,
    )

    await update.message.reply_text(
        "✅ Thank you! Your suggestion has been sent."
    )

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Suggestion cancelled."
    )

    return ConversationHandler.END