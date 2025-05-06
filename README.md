Muhomorda telegram bot by @cha0skvlt
v1.0

INFO:
 - Бот для тг канала [@muhomor_da](https://t.me/muhomor_da). Бот генерирует посты на тематику микродозинга Мухомора, Ежовика Гребенчатого, Чаги, Кондицепса и других полезных даров природы. Бот запускается раз в день по crontab и генерирует через бота в telegram пост. Бот берет информацию из mikrodozing.pdf
 В проекте применяется SQLite

DONE:

TODO:
- Код бота
- Структура поста
- Контент для постов
- Кронтаб раз в день 

FILES: |
  mukhomorda/
    ├── bot.py             # Главный скрипт: генерация и отправка
    ├── db.py              # Работа с SQLite
    ├── parser.py          # Парсинг mikrodozing.pdf
    ├── scheduler.py       # Планировщик для crontab
    ├── persona.yml        # Личность бота
    ├── posts.json         # Исторические сгенерированные посты
    ├── requirements.txt   # Зависимости
    ├── schema.sql         # Структура базы
    ├── .env               # Ключи
    ├── .env.example       # Пример ключей
    ├── README.md          # Документация
    └── data/
    └── mikrodozing.pdf

HOW TO USE:
  - pip install -r requirements.txt  #ставим зависимостиНачинае
  - cp .env.example .env             #создаем и заполняем файл ключей
  - /version , /reset                #команды


#6566466182:AAG9YqxioB1ePdH5_2w7yVVQPOveo6I0tjM