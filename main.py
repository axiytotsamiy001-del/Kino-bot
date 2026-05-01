from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8703304211:AAFU-OPeISDFzWoFvnjOxlcFl1udjH7aSxI"

movies = {
    "avatar": "🎬 Avatar\nLink: https://t.me/example1",
    "batman": "🎬 Batman\nLink: https://t.me/example2"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎥 Kino nomini yozing")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text in movies:
        await update.message.reply_text(movies[text])
    else:
        await update.message.reply_text("❌ Kino topilmadi")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot ishlayapti...")
app.run_polling()
