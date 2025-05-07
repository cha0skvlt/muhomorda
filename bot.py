#!/usr/bin/env python3

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
import telebot
from postgen import generate_muhomor_post
from db import is_duplicate_post

# ───── Load config
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def post_to_channel():
    post = generate_muhomor_post()
    if is_duplicate_post(post["content"]):
        return
    bot.send_message(CHANNEL_ID, post["content"], parse_mode="Markdown")

if __name__ == "__main__":
    post_to_channel()
