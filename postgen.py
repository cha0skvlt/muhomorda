import random
import json
from pathlib import Path
from openai import OpenAI
from parser import extract_random_text

TEMPLATE_PATH = "post.json"
PDF_PATH = "data/mikrodozing.pdf"

client = OpenAI()

def generate_muhomor_post():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        tpl = json.load(f)

    intro = random.choice(tpl["intros"])
    style = random.choice(tpl["styles"])
    theme = random.choice(tpl["themes"])
    footer = "\n\n" + "\n".join(tpl["footer"])
    system_prompt = tpl["system_prompt"]

    raw_text = extract_random_text(PDF_PATH)

    prompt = f"""
{system_prompt}

Вот выдержка из текста:
\"\"\"{raw_text}\"\"\"

Тема поста: {theme}  
Стиль подачи: {style}

Сгенерируй Telegram-пост в соответствии с описанием. Используй эмодзи, структуру и голос шаманского духа Мухоморды. Не используй хэштеги, ссылки и рекламу.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=700
    )

    content = response.choices[0].message.content.strip()
    return {
        "title": f"{intro}",
        "content": f"{intro}\n\n{content}{footer}"
    }
