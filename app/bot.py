import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
TOKEN = os.getenv("BOT_TOKEN","PUT-YOUR-TOKEN")
app = Flask(__name__)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Quest bot is alive 🚀")
def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
@app.get("/")
def health():
    return "OK"
if __name__ == "__main__":
    run_bot()
