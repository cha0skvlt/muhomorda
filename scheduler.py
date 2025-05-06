import os
from dotenv import load_dotenv
from postgen import generate_post  # или generate_from_pdf
import telebot

# ───── Load keys
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # пример: "@muhomor_da"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def post_to_channel():
    post = generate_post()  # или generate_from_pdf()
    text = f"*{post['title']}*\n\n{post['content']}"
    bot.send_message(CHANNEL_ID, text, parse_mode="Markdown")
    print(f"[POST] Отправлено в канал: {post['title']}")

if __name__ == "__main__":
    post_to_channel()
