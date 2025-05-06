import random
from datetime import datetime
from parser import extract_text
from openai import OpenAI
import os
import sqlite3
from dotenv import load_dotenv

# ───── Init
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_KEY)
DB_PATH = "mukhomorda.db"

# ───── Темы (ручные)
TOPICS = [
    "🟥 Мухомор и микродозинг",
    "🟫 Чага: гриб бессмертия",
    "🟨 Кордицепс и энергия",
    "🟩 Ежовик гребенчатый — гриб мозга",
    "🍄 Мифология и духи грибов"
]

# ───── Сохранение в базу
def save_post_to_db(title, content):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        print(f"[DB] Сохранён пост: {title}")

# ───── Пост по шаблону
def generate_post():
    topic = random.choice(TOPICS)
    body = {
        "🟥 Мухомор и микродозинг": (
            "Мухомор — не яд, а союзник. В микродозах он помогает восстановить баланс, "
            "уменьшить тревожность и вернуть контакт с телом.\n\n"
            "#мухомор #микродозинг #грибы"
        ),
        "🟫 Чага: гриб бессмертия": (
            "Чага помогает организму адаптироваться, повышает иммунитет и наполняет энергией. "
            "Используется веками на Севере как лекарство.\n\n"
            "#чага #адаптоген #здоровье"
        ),
        "🟨 Кордицепс и энергия": (
            "Кордицепс — гриб, повышающий выносливость. Его выбирают спортсмены и монахи. "
            "Восточная медицина знает его тысячи лет.\n\n"
            "#кордицепс #энергия #адаптоген"
        ),
        "🟩 Ежовик гребенчатый — гриб мозга": (
            "Ежовик стимулирует рост нейронов. Улучшает память, концентрацию и ясность ума. "
            "Идеален с дыхательными практиками.\n\n"
            "#ежовик #нейропластичность #ноотроп"
        ),
        "🍄 Мифология и духи грибов": (
            "Грибы — проводники между мирами. Шаманы и травники веками "
            "использовали их как духовных союзников.\n\n"
            "#грибноймир #мифология #духилеса"
        ),
    }

    post = {
        "title": topic,
        "content": body[topic],
        "created_at": datetime.now().isoformat()
    }

    save_post_to_db(post["title"], post["content"])
    return post

# ───── Пост из PDF
def generate_from_pdf():
    raw_text = extract_text()[:3000]
    prompt = (
        f"Вот выдержка из текста о микродозинге:\n\n{raw_text}\n\n"
        "На основе этого напиши вдохновляющий Telegram-пост про грибы. "
        "Добавь заголовок, эмодзи, хештеги. Пост должен быть поэтичным и понятным."
    )Ща

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.8,
    )

    content = response.choices[0].message.content.strip()
    title = content.split("\n")[0]
    body = "\n".join(content.split("\n")[1:])

    save_post_to_db(title, body)

    return {
        "title": title,
        "content": body,
        "created_at": datetime.now().isoformat()
    }
