from telegram import Update
from telegram.ext import ContextTypes
from features.genrate_passord import generate_password
from features.weather import get_weather

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello! Thank for chating with me!\n" \
    "if you need any help send : \n"
    "/help")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Telegram Assistant Bot \n" \
    "Available commands:\n"\
    "/start - Start the bot \n"\
    "/help - Show this help menu\n"\
    "/password - Generate a secure password \n"\
    "/weather city - Current weather\n" \
    "🚧 Coming soon:\n" \
    "/weather_alert - Automatic weather alerts\n" \
    "/remind - Create reminders\n" \
    "/timer - Stopwatch and timer\n" \
    "💡 Have an idea? \n" \
    "Use /newf to suggest a feature!\n")


async def password_generate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = generate_password()

    await update.message.reply_text(f'your password is :')
    await update.message.reply_text(password)

async def weather_now(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message or update.edited_message

    if not message:
        return

    if not context.args:
        await message.reply_text(
            "Please provide a city.\nExample:\n/weather Oujda"
        )
        return

    city = " ".join(context.args)

    weather = get_weather(city)

    await message.reply_text(weather)






