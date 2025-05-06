Muhomorda telegram bot by @cha0skvlt
v1.0

INFO:
 - Бот для тг канала [@muhomor_da](https://t.me/muhomor_da)

DONE:

TODO:
- Код бота
- Структура поста
- Контент для постов
- Кронтаб раз в день 

FILES:
  - /var/opt/bot/.env                #ключи
  - /var/opt/bot/persona.yml         #личность
  - /var/opt/bot/bot.py              #сам бот
  - /var/opt/bot/README.md           #этот файл
  - /etc/systemd/system/bot.service  #процесс бота

HOW TO USE:
  - pip install -r requirements.txt  #ставим зависимости
  - cp .env.example .env             #создаем и заполняем файл ключей
  - /version , /reset                #команды