
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)
from Conversation.feature_request import FEATURE ,newf , receive_feature , cancel , ConversationHandler
from handlers.commands import start_command , help_command , password_generate_command , weather_now
from handlers.messages import handle_message , TOKEN 
from handlers.errors import error

#creat app
if __name__ == "__main__":

    print("Starting bot...")

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("password", password_generate_command))
    app.add_handler(CommandHandler("weather", weather_now))
    feature_handler = ConversationHandler(
    entry_points=[
        CommandHandler("newf", newf)
    ],
    states={
        FEATURE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                receive_feature,
            )
        ]
    },
    fallbacks=[
        CommandHandler("cancel", cancel)
    ],
)
    app.add_handler(feature_handler)


    # Messages
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling()