import json
import yaml
from openai import OpenAI
from parser import extract_random_text
import random

client = OpenAI()

PDF_PATH = "data/mikrodozing.pdf"
TEMPLATE_PATH = "post.json"
PERSONA_PATH = "persona.yml"

def load_persona():
    with open(PERSONA_PATH, "r", encoding="utf-8") as f:
        p = yaml.safe_load(f)
    return {
        "system_prompt": p["system_prompt"],
        "user_prompt": p["user_prompt"],
        "model": p.get("model", "gpt-3.5-turbo"),
        "temperature": p["settings"].get("temperature", 0.8),
        "max_tokens": p["settings"].get("max_tokens", 600)
    }

def generate_muhomor_post():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        tpl = json.load(f)
    persona = load_persona()

    theme = random.choice(tpl["themes"])
    footer = "\n\n" + "\n".join(tpl["footer"])

    # Используем PDF только если тема — цитаты из книги
    if "Цитаты" in theme or "Бабы Маши" in theme:
        raw_text = extract_random_text(PDF_PATH)
        text_block = f"Вот выдержка из книги Бабы Маши:\n\"\"\"{raw_text}\"\"\"\n\n"
    else:
        text_block = ""

    prompt = persona["user_prompt"].replace("{theme}", theme)
    final_prompt = text_block + prompt

    response = client.chat.completions.create(
        model=persona["model"],
        messages=[
            {"role": "system", "content": persona["system_prompt"]},
            {"role": "user", "content": final_prompt}
        ],
        temperature=persona["temperature"],
        max_tokens=persona["max_tokens"]
    )

    content = response.choices[0].message.content.strip()
    return {
        "title": theme,
        "content": f"{content}{footer}"
    }
