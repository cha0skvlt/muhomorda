Muhomorda Telegram Bot by @cha0skvlt  
v1.0

INFO:
- Telegram bot for the channel [@muhomor_da](https://t.me/muhomor_da)
- Automatically generates daily posts about Amanita microdosing 🍄
- Source: `data/mikrodozing.pdf` (compiled by the legendary Baba Masha)
- Posts are well-structured, emoji-rich, and fact-based, without any marketing
- Uses GPT-3.5-turbo and SQLite to generate and store posts
- Runs automatically via `crontab` once per day

DONE:
- ✅ Telegram bot with GPT and OpenAI integration
- ✅ PDF-based text parsing and summarization
- ✅ Post formatting via external template (`post.json`)
- ✅ SQLite-based history of published posts
- ✅ Personality and model config via `persona.yml`
- ✅ Telegram commands: /version and /reset
- ✅ Secure access via `ALLOWED_USERS` in .env
- ✅ Fully automated pipeline

TODO:
- [ ] Add image generation (future)
- [ ] Post analytics and tracking
- [ ] Admin web dashboard (optional)
- [ ] Add more mushrooms (Lion’s Mane, Chaga, etc.)
- [ ] Admin-only Telegram commands (e.g. /preview)

FILES:
- `.env`              — environment variables (tokens, access)
- `bot.py`            — Telegram bot (commands, replies)
- `scheduler.py`      — auto-posting script (used by cron)
- `postgen.py`        — post generation engine (GPT + formatting)
- `parser.py`         — PDF text extractor
- `persona.yml`       — personality and model configuration
- `post.json`         — post layout and style templates
- `mukhomorda.db`     — SQLite DB with table `posts`
- `requirements.txt`  — dependencies
- `README.md`         — this file

HOW TO USE:
```bash
# Install dependencies
pip install -r requirements.txt

# Create and configure environment
cp .env.example .env  # then edit .env with your keys

# Run bot manually (for testing)
python3 bot.py

# Generate & post a message manually
python3 scheduler.py

# Setup cron (example: every day at 08:00):
0 8 * * * /path/to/venv/bin/python3 /var/opt/mbot/scheduler.py >> /var/log/mbot.log 2>&1
