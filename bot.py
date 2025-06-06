#!/usr/bin/env python3

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
import telebot
from postgen import generate_muhomor_post

# ───── Load config
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# ───── Run once
def post_to_channel():
    post = generate_muhomor_post()
    bot.send_message(CHANNEL_ID, post["content"], parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    post_to_channel()

