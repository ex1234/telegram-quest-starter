import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN","PUT-YOUR-TOKEN")
app = Flask(__name__)

@app.get("/")
def health():
    return "OK"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Quest bot is alive")

def run_http():
    # lightweight health server
    app.run(host="0.0.0.0", port=8080)

def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    Thread(target=run_http, daemon=True).start()
    run_bot()
