import os
import telebot
from flask import Flask, request

# توکن ربات
API_TOKEN = '7174774942:AAGaPSfnHdN21Vv85yxSRX13Th5jd29-wMA'
bot = telebot.TeleBot(API_TOKEN)

# اپلیکیشن Flask برای Webhook
app = Flask(__name__)

# تنظیم وبهوک
def set_webhook():
    webhook_url = "https://sabtenamrobat-rik4vd4p7-00989901243254s-projects.vercel.app/" + API_TOKEN
    bot.remove_webhook()  # حذف وبهوک قبلی
    bot.set_webhook(url=webhook_url)  # تنظیم وبهوک جدید

@app.route('/' + API_TOKEN, methods=['POST'])
def get_message():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    return "Webhook is live!", 200

if __name__ == "__main__":
    set_webhook()  # تنظیم وبهوک یک بار در زمان شروع برنامه
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
