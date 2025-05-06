import os
from datetime import datetime
from parser import extract_text
from openai import OpenAI
from dotenv import load_dotenv
import sqlite3

# ───── Init
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
DB_PATH = "mukhomorda.db"
client = OpenAI(api_key=OPENAI_KEY)

# ───── Сохраняем пост
def save_post_to_db(title, content):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        print(f"[DB] Сохранён пост: {title}")

# ───── Генерация по PDF (только мухомор)
def generate_muhomor_post():
    raw_text = extract_text()[:3000]  # Ограничим контекст
    prompt = f"""
Вот выдержка из научно-популярного текста о микродозинге мухомора:

{raw_text}

На основе этих данных, сгенерируй красиво оформленный Telegram-пост о микродозинге мухомора в структуре:

🧠 Краткое название и идея  
🍄 Что это (о мухоморе)  
🔬 Подтверждённые эффекты  
📊 Влияние по неделям (1–6)  
💊 Как принимать (дозировки, курс)  
⚙️ С чем сочетается (чага, родиола, etc)  
📚 Научные источники  
🧩 Кому подойдёт  

Добавь эмодзи, буллеты, структурирование. Не используй маркетинговые слова, ссылки или "пиши сюда".  
Пиши как лесной шаман, но грамотно.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
        temperature=0.7,
    )

    content = response.choices[0].message.content.strip()
    title = content.split("\n")[0].strip()
    body = "\n".join(content.split("\n")[1:]).strip()

    # ───── Добавим блок ссылок
    links_block = """
📱 Для заказа писать сюда
(https://t.me/NitrousIgor)
💬 Чат единомышленников (https://t.me/muhomordachat)
🍄 О нашей лавке (https://telegra.ph/Muhomor-DA-12-30)
""".strip()

    full_content = f"{body}\n\n{links_block}"

    save_post_to_db(title, full_content)

    return {
        "title": title,
        "content": full_content,
        "created_at": datetime.now().isoformat()
    }
