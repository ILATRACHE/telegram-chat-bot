import os
from dotenv import load_dotenv
from typing import Final
from telegram import Update
from telegram.ext import ContextTypes


load_dotenv()


TOKEN: Final = os.getenv('BOT_TOKEN')
BOT_USERNAME: Final = os.getenv('Bot_Username')

#handles 
def handles_response(text : str) -> str :
    Processed : str = text.lower()
    if "hello" in Processed :
        return "hey there!"
    if "how are you" in Processed :
        return"im good thank you"
    if "otman" in Processed :
        return"instagram : https://www.instagram.com/otmanjebbour?igsh=MTZxYm04bmI2eWcx \n tiktok : \n youtoube : https://youtube.com/@otmanjebbour?si=0OyjDEA4skUjzBkn \n "
    return "i dont understand what you wrote"

async def handle_message(update : Update, context : ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
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
