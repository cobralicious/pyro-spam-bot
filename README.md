# 🤖 Pyro Spam Bot

Телеграм-бот на Pyrogram, позволяющий владельцу отправлять серию сообщений выбранному пользователю.

## 📦 Возможности

- Команда `/spam <user_id> <кол-во> <текст>`
- Ограничение до 20 сообщений
- Только владелец (по Telegram ID) имеет доступ к команде
- Обработка ошибок: блокировка, не найденный чат, лимиты Telegram API

---

## 🚀 Быстрый старт

### 1. Установи зависимости

```bash
pip install pyrogram tgcrypto
```
2. Настрой .env или укажи переменные в main.py
BOT_TOKEN — токен бота от @BotFather

API_ID и API_HASH — получи на my.telegram.org

OWNER_ID — твой Telegram ID (можно узнать у @userinfobot)

3. Запусти бота
bash
Copy
Edit
python main.py
🛠 Пример использования
После запуска бота в Telegram:

plaintext
Copy
Edit
/start
/spam 123456789 5 Привет, как дела?
⚠️ Важно
Бот может писать только тем, кто:

Либо написал боту первым

Либо разрешил сообщения от ботов в настройках приватности

Злоупотребление приведёт к блоку или бану со стороны Telegram

🗂 Пример .env
Создай файл .env в корне проекта и добавь туда:

env
Copy
Edit
BOT_TOKEN=your_bot_token
API_ID=123456
API_HASH=your_api_hash
OWNER_ID=123456789
📄 Лицензия
MIT — делай что хочешь, но помни о лимитах Telegram 😉

markdown
Copy
Edit

---

Если хочешь, могу:

- ✅ Добавить `.env.example`  
- ✅ Добавить `.gitignore`  
- ✅ Сгенерировать иконку `.png` или `.ico`  
- ✅ Оформить `pyproject.toml` или `requirements.txt`  

Скажи что нужно — сделаю.
