Muhomorda Telegram Bot by @cha0skvlt  
v1.0

INFO:
- Autonomous Telegram bot for [@muhomor_da](https://t.me/muhomor_da)
- Posts daily about Amanita microdosing 🍄
- Source: `data/mikrodozing.pdf` — knowledge of Baba Masha 🧙‍♀️
- Style, structure, and tone controlled via `post.json` and `persona.yml`
- Powered by GPT-3.5-turbo and SQLite
- Fully automatic: runs once a day via `cron`, no commands or interaction

DONE:
- ✅ Auto-posting bot via `bot.py` (no handlers, only scheduled run)
- ✅ PDF text extraction
- ✅ Semantic GPT-based post generation
- ✅ Markdown + emoji formatting via `post.json`
- ✅ Persona config (style, model) in `persona.yml`
- ✅ SQLite post archive (`mukhomorda.db`)
- ✅ Crontab-compatible, stable, silent

TODO:
- [ ] Image generation (optional)
- [ ] Admin stats / analytics
- [ ] Support for other mushrooms (Lion’s Mane, Chaga, etc.)
- [ ] Telegram inline previews / previews queue

FILES:
- `.env`              — API tokens, allowed users, channel ID
- `bot.py`            — main entry point, run by cron
- `postgen.py`        — generates post using GPT + formatting
- `parser.py`         — extracts raw text from PDF
- `persona.yml`       — defines GPT model and tone
- `post.json`         — structure, intros, styles, and footer
- `mukhomorda.db`     — SQLite database for post history
- `requirements.txt`  — Python dependencies
- `README.md`         — project documentation

HOW TO USE:
```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Fill in:
# - TELEGRAM_BOT_TOKEN=
# - OPENAI_API_KEY=
# - TELEGRAM_CHANNEL_ID=@yourchannel or -100XXXXXXXXXX

# Run manually (for testing)
python3 bot.py

# Setup crontab (e.g. every day at 08:00)
0 8 * * * /path/to/venv/bin/python3 /var/opt/mbot/bot.py >> /var/log/mbot.log 2>&1
