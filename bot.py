
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)
from Conversation.feature_request import FEATURE ,newf , receive_feature , cancel , ConversationHandler
from handlers.commands import start_command , help_command , password_generate_command , weather_now , ASK_DEFAULT_CITY , confirm_default_city 
from handlers.messages import handle_message , TOKEN 
from handlers.errors import error
from database.db import create_table
from features.QR_code import turn_to_qr , create_qr , Qr , ccancel


create_table()

#creat app
if __name__ == "__main__":

    print("Starting bot...")

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("password", password_generate_command))
    
    
    weather_conv = ConversationHandler(
        entry_points=[
            CommandHandler("weather", weather_now)
                ],
            states={
            ASK_DEFAULT_CITY: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                confirm_default_city
                )
            ]
            },
            fallbacks=[])

    app.add_handler(weather_conv)

    qr_conv = ConversationHandler(
    entry_points=[CommandHandler("qr", Qr)],
    states={
        turn_to_qr: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, create_qr)
        ],
    },
    fallbacks=[CommandHandler("cancel", ccancel)],
)
    app.add_handler(qr_conv)


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