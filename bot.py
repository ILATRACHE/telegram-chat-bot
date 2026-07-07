from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
import os
from dotenv import load_dotenv


load_dotenv()


TOKEN: Final = os.getenv('BOT_TOKEN')
BOT_USERNAME: Final = os.getenv('Bot_Username')
#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello! Thank for chating with me!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello! what can i help you")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("custom message ")



#handles 
def handles_response(text : str) -> str :
    Processed : str = text.lower()
    if "hello" in Processed :
        return "hey there!"
    if "how are you" in Processed :
        return"im good thank you"
    return "i dont understand what you wrote"

async def handle_message(update : Update, context : ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type 
    text : str = update.message.text

    print(f'user {update.message.chat_id} in {message_type} : "{text}"')
    if message_type == 'group' :
        if BOT_USERNAME in text :
            new_text : str = text.replace(BOT_USERNAME , '').strip()
            respanses = handles_response(new_text)
        else :
            return
    else :
        respanses = handles_response(text)
    
    await update.message.reply_text(respanses)

#error
async def error(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

#creat app
if __name__ == "__main__":

    print("Starting bot...")

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling()