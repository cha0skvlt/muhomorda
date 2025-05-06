import os
import json
import random
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from parser import extract_text

# ───── Init
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
DB_PATH = "mukhomorda.db"
TEMPLATE_PATH = "post.json"

client = OpenAI(api_key=OPENAI_KEY)

def save_post_to_db(title, content):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        print(f"[DB] Сохранён пост: {title}")

def generate_muhomor_post():
    raw_text = extract_text()[:3000]

    # ───── Подгружаем шаблон
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        tpl = json.load(f)

    intro = random.choice(tpl["intros"])
    layout = tpl["layout"]
    footer = tpl["footer"]

    # ───── Промт: просим ответ строго в JSON
    system_prompt = "Ты пишешь структурированные Telegram-посты на тему микродозинга мухомора. Ответ давай строго в JSON с нужными ключами."
    prompt = f"""
Вот выдержка из научного и популярного текста о мухоморе:

{raw_text}

Сгенерируй Telegram-пост, вернув его в формате JSON с такими ключами:

- title
- text_what
- text_effects
- text_week1
- text_week2
- text_week3
- text_dosage
- text_stack
- text_sources
- text_target

Только JSON без пояснений. Стиль — информативно, шамански, вдохновляюще. Без маркетинга.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=900,
        temperature=0.7,
    )

    json_text = response.choices[0].message.content.strip()
    try:
        data = json.loads(json_text)
    except json.JSONDecodeError:
        raise Exception("❌ Ошибка разбора JSON от GPT")

    # ───── Сборка поста
    lines = [intro, ""]

    for block in layout:
        lines.append(block.format(**data))
        lines.append("")

    lines.extend(footer)

    full_text = "\n".join(lines).strip()
    save_post_to_db(data["title"], full_text)

    return {
        "title": data["title"],
        "content": full_text,
        "created_at": datetime.now().isoformat()
    }
