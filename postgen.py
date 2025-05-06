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

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        tpl = json.load(f)

    intro = random.choice(tpl["intros"])
    styles = tpl.get("styles", [])
    footer = tpl["footer"]
    style_prompt = "\n".join([f"- {s}" for s in styles])
    prompt_suffix = tpl["prompt_suffix"].replace("{styles}", style_prompt)

    prompt = f"""
Вот выдержка из научного и популярного текста о мухоморе:

{raw_text}

{prompt_suffix}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты пишешь Telegram-посты по PDF о мухоморе. Стиль — шаман и эксперт."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=900,
        temperature=0.85,
    )

    body = response.choices[0].message.content.strip()
    title_line = body.split("\n")[0].strip(" *")

    lines = [intro, "", body, "", *footer]
    full_post = "\n".join(lines).strip()

    save_post_to_db(title_line, full_post)

    return {
        "title": title_line,
        "content": full_post,
        "created_at": datetime.now().isoformat()
    }
