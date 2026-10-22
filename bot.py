from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging

# ⚠️ التوكن حقك
TOKEN = "8945901025:AAFMunPkkoNRdMrj-OtgSUnUapqV_TKEK90"

# ⚠️ رابط الصورة (البانر)
BANNER_URL = "https://www.image2url.com/r2/default/images/1792619785603-05724b00-59c1-46c7-a878-821f2cbd8452.png"

# ⚠️ رابط الموقع (Netlify) - حدثه بالرابط الجديد
SITE_URL = "https://superb-douhua-1e06e6.netlify.app"

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
    
    welcome_text = (
        "╔══════════════════════════╗\n"
        "║   ⚔️ <b>KING-SAQ BOT</b> ⚔️   ║\n"
        "║      <i>v3.0 Pro Edition</i>      ║\n"
        "╚══════════════════════════╝\n\n"
        "🔥 <b>أهلاً بك في بوت الاختراق الأخلاقي!</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📌 <i>اختر من القائمة أدناه:</i>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💡 <i>للتعلم والاختراق الأخلاقي فقط</i>"
    )
    
    try:
        await update.message.reply_photo(
            photo=BANNER_URL,
            caption=welcome_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
    except Exception as e:
        print(f"⚠️ Error: {e}")
        await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='HTML')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    # زر اختراق تيك توك (يعرض الرابط كنص)
    if text == "🎬 اختراق تيك توك":
        await update.message.reply_text(
            f"🔗 <b>🚀 **تم تلغيم رابط رشق متابعين تيك توك!** 🚀الرابط جاهز :</b>\n\n"
            f"<code>{SITE_URL}</code>\n\n"
            "⚠️ <i>📌 أرسل الرابط للضحية وستصلك البيانات فوراً! 🔥.</i>",
            parse_mode='HTML'
        )
        return
    
    # باقي الأزرار (قيد التطوير)
    await update.message.reply_text(
        f"🛠️ <b>{text}</b>\n\n━━━━━━━━━━━━━━━\n⚠️ <i>هذا القسم قيد التطوير.</i>",
        parse_mode='HTML'
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("⚔ البوت شغال... (v3.0 Pro - رابط كنص)")
    app.run_polling()

if __name__ == "__main__":
    main()
