# 🍄 Muhomorda Telegram Bot by @cha0skvlt  
**Version: v2**

## INFO
- 🤖 Telegram bot for [@muhomor_da](https://t.me/muhomor_da)
- 🧙‍♀️ Posts daily about Amanita and other mushrooms microdosing, based on the teachings of Baba Masha
- 📄 Uses `data/mikrodozing.pdf` for inspiration every few days
- ✨ Style, structure, themes and footer managed via `post.json` and `persona.yml`
- ⚙️ Powered by GPT-3.5-turbo (OpenAI) + SQLite for history
- 🕒 No interaction, no commands — runs silently via `cron`

## TODO
- [ ] Image generation (optional)
- [ ] Admin dashboard or stats
- [ ] Inline preview queue for approval


## FILES
| File            | Description                              |
|-----------------|------------------------------------------|
| `.env`          | API keys and bot/channel configuration   |
| `bot.py`        | Main cron-run script (silent mode)       |
| `postgen.py`    | GPT-based post generation logic          |
| `parser.py`     | Extracts random text from Baba Masha PDF |
| `persona.yml`   | Persona, tone, temperature, prompt       |
| `post.json`     | Themes, footer, quote intro template     |
| `mukhomorda.db` | SQLite DB for published post history     |
| `requirements.txt` | Python dependencies                   |
| `README.md`     | You're reading it                        |

## HOW TO USE

```bash
# Install dependencies
pip install -r requirements.txt

# Prepare environment
cp .env.example .env
# Then edit .env:
# TELEGRAM_BOT_TOKEN=xxxxx
# OPENAI_API_KEY=xxxxx
# TELEGRAM_CHANNEL_ID=@yourchannel or -100XXXXXXXXXX

# Run manually (for debug)
python3 bot.py

# Setup cron (recommended time: 08:00 with delay logic)
0 8 * * * /usr/bin/python3 /var/opt/mbot/bot.py > /dev/null 2>&1
