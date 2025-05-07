#!/usr/bin/env python3

import os
import json
import random
import yaml
import re
from dotenv import load_dotenv
from openai import OpenAI
from parser import extract_random_text

# ───── Init
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

def finalize_content(text):
    sentences = re.split(r'(?<=[.!?…]) +', text.strip())
    if len(sentences) > 1:
        return " ".join(sentences[:-1])
    return text.strip()

def generate_muhomor_post():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        tpl = json.load(f)
    persona = load_persona()

    theme = random.choice(tpl["themes"])
    footer = "\n\n" + "\n".join(tpl["footer"])
    quote_intro = tpl.get("quote_intro", "")

    text_block = ""
    if "Цитаты" in theme or "Бабы Маши" in theme:
        raw_text = extract_random_text(PDF_PATH)
        text_block = quote_intro.replace("{text}", raw_text)

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

    raw = response.choices[0].message.content.strip()
    content = finalize_content(raw)

    return {
        "title": theme,
        "content": f"{content}{footer}"
    }
