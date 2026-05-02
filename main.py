from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8703304211:AAFU-OPeISDFzWoFvnjOxlcFl1udjH7aSxI"

movies = {}

# 🎬 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🎬 Kino qidirish"],
        ["➕ Kino qo‘shish"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🎥 Botga xush kelibsiz!",
        reply_markup=reply_markup
    )

# 🧠 STATE
user_state = {}

# 📩 MESSAGE
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    # 🎬 Qidirish
    if text == "🎬 Kino qidirish":
        user_state[user_id] = "search"
        await update.message.reply_text("🔎 Kino nomini yozing")
        return

    # ➕ Qo‘shish
    if text == "➕ Kino qo‘shish":
        user_state[user_id] = "add_name"
        await update.message.reply_text("🎬 Kino nomini yozing")
        return

    # ➕ Nom yozildi
    if user_state.get(user_id) == "add_name":
        user_state[user_id] = {"name": text}
        await update.message.reply_text("🔗 Endi link yuboring")
        return

    # ➕ Link yozildi
    if isinstance(user_state.get(user_id), dict):
        movie_name = user_state[user_id]["name"]
        movies[movie_name.lower()] = text

        user_state[user_id] = None
        await update.message.reply_text("✅ Kino qo‘shildi")
        return

    # 🔎 Qidiruv
    if user_state.get(user_id) == "search":
        movie = movies.get(text.lower())

        if movie:
            await update.message.reply_text(f"🎬 {text}\n🔗 {movie}")
        else:
            await update.message.reply_text("❌ Topilmadi")

        return

# 🤖 APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("🔥 Buttonli bot ishlayapti...")
app.run_polling()
