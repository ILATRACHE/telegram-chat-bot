from io import BytesIO
import qrcode
from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import ConversationHandler


turn_to_qr = 1
async def Qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "please entre the name or the link to turn into Qr code : ?\n\n"
        "Type /cancel to cancel."
    )

    return turn_to_qr



async def create_qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.text

    img = qrcode.make(data)

    bio = BytesIO()
    bio.name = "qrcode.png"
    img.save(bio, "PNG")
    bio.seek(0)

    await update.message.reply_photo(
        photo=bio,
        caption="✅ Here is your QR code!"
    )

    return ConversationHandler.END

async def ccancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ QR code creation cancelled.")
    return ConversationHandler.END


