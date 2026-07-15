from telegram import Update
from telegram.ext import ContextTypes
from features.genrate_passord import generate_password
from features.weather import get_weather
from telegram.ext import ConversationHandler
from database.db import save_default_city as save_default_city_db, get_default_city

ASK_DEFAULT_CITY = 1


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
    "/qr - turn any text or link into qr code \n" \
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

    new_city = False

    if context.args:
        city = " ".join(context.args)
        new_city = True

    else:
        user_id = update.message.from_user.id
        city = get_default_city(user_id)

        if not city:
            await update.message.reply_text(
                "❌ You don't have a default city.\n"
                "Use:\n/weather Oujda"
            )
            return

    weather = get_weather(city)

    await update.message.reply_text(weather)

    # Save temporarily only for new city
    if new_city:
        context.user_data["city"] = city

        await update.message.reply_text(
            f"Do you want to make {city} your default city? (yes/no)"
        )

        return ASK_DEFAULT_CITY

async def confirm_default_city(update: Update, context: ContextTypes.DEFAULT_TYPE):

    answer = update.message.text.lower()

    user_id = update.message.from_user.id

    city = context.user_data.get("city")

    if answer in ["yes", "y"]:
        user_id = update.message.from_user.id
        save_default_city_db(user_id, city)

        await update.message.reply_text(
            f"✅ {city} is now your default city."
        )

    elif answer in ["no", "n"]:
        await update.message.reply_text(
            "Okay, I won't save it."
        )

    else:
        await update.message.reply_text(
            "Please answer yes or no."
        )
        return ASK_DEFAULT_CITY

    return ConversationHandler.END







