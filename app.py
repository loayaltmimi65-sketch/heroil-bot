import os
import threading
from flask import Flask
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
import logging

# ⚠️ التوكن (راح نجيبه من Environment Variable في Render)
TOKEN = os.environ.get("BOT_TOKEN", "8945901025:AAFMunPkkoNRdMrj-OtgSUnUapqV_TKEK90")

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/health')
def health():
    return "OK"

# باقي كود البوت (نفس الكود اللي عندك)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🎁 مسابقة الحلم 2026"), KeyboardButton("🎬 اختراق تيك توك")],
        [KeyboardButton("🚀 اختراق انستقرام"), KeyboardButton("🔵 اختراق فيسبوك")],
        [KeyboardButton("✅ اختراق واتساب"), KeyboardButton("👻 اختراق سناب")],
        [KeyboardButton("🔥 اختراق بجي"), KeyboardButton("💎 شحن فري فاير")],
        [KeyboardButton("📱 فحص الجهاز"), KeyboardButton("📍 تحديد الموقع")],
        [KeyboardButton("ℹ️ حول البوت")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text("⚔️ أهلاً بك في بوت KING-SAQ!\nاختر من القائمة:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🎬 اختراق تيك توك":
        await update.message.reply_text(
            f"🔗 <b>انسخ الرابط التالي:</b>\n\n<code>https://superb-douhua-1e06e6.netlify.app</code>",
            parse_mode='HTML'
        )
        return
    await update.message.reply_text(f"🛠️ <b>{text}</b> قيد التطوير.", parse_mode='HTML')

def run_bot():
    app_bot = Application.builder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("⚔️ البوت شغال...")
    app_bot.run_polling()

if __name__ == "__main__":
    # نشغل البوت في Thread منفصل
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # نشغل Flask (عشان Render يعرف إن فيه Web Service)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
