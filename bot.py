import os
import yaml
import telebot
from openai import OpenAI
from dotenv import load_dotenv

# ───── Load .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
ALLOWED_USERS = os.getenv("ALLOWED_USERS", "").split(",")

# ───── Load persona.yml
with open("persona.yml", "r", encoding="utf-8") as f:
    persona = yaml.safe_load(f)

OPENAI_MODEL = persona.get("model", "gpt-3.5-turbo")
SYSTEM_PROMPT = persona.get("system_prompt", "")

settings = persona.get("settings", {})
HISTORY_DEPTH = int(settings.get("history_depth", 3))
MAX_TOKENS = int(settings.get("max_tokens", 200))
TEMPERATURE = float(settings.get("temperature", 0.5))

# ───── Init
bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_KEY)
sessions = {}

# ───── Commands
@bot.message_handler(commands=['version'])
def version(message):
    user_id = str(message.from_user.id)
    if user_id not in ALLOWED_USERS:
        return
    bot.reply_to(
        message,
        f"✅ Model: {OPENAI_MODEL}, tokens: {MAX_TOKENS}, temp: {TEMPERATURE}, depth: {HISTORY_DEPTH}"
    )

@bot.message_handler(commands=['reset'])
def reset_session(message):
    user_id = str(message.from_user.id)
    if user_id not in ALLOWED_USERS:
        return
    sessions[user_id] = []
    bot.reply_to(message, "♻️ Context reset.")

# ───── Messages
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    user_id = str(message.from_user.id)
    if user_id not in ALLOWED_USERS:
        bot.reply_to(message, "⛔ Access denied.")
        return

    bot.send_chat_action(message.chat.id, "typing")
    sessions.setdefault(user_id, [])
    sessions[user_id].append({"role": "user", "content": message.text})

    try:
        chat_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + sessions[user_id][-HISTORY_DEPTH:]

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=chat_messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )

        reply = response.choices[0].message.content.strip()
        sessions[user_id].append({"role": "assistant", "content": reply})
        bot.reply_to(message, reply)

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {e}")

# ───── Start
bot.infinity_polling()
