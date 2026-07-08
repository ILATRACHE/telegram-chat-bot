
from telegram.ext import ContextTypes

async def error(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
