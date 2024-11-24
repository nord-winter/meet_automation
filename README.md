# 🤖 Google Meet Automation Bot

Телеграм-бот для автоматизации групповых звонков в Google Meet с функциями записи, транскрибации и создания резюме встреч.

## 🌟 Возможности

- 📅 Автоматическое создание встреч в Google Meet
- 🔔 Уведомления участников через Telegram
- 🎥 Запись групповых звонков
- 📝 Транскрибация разговоров с помощью Whisper
- 📋 Автоматическое создание резюме встреч через GPT
- 📨 Публикация результатов в Telegram

## 🛠 Технологии

- Python 3.10+
- Google Calendar API
- Telegram Bot API
- OpenAI Whisper
- ChatGPT API
- Google Cloud Platform

## 📋 Требования

- Python 3.10 или выше
- Google Cloud аккаунт
- Telegram Bot Token
- OpenAI API ключ

## 🚀 Установка

1. **Клонирование репозитория:**
```bash
git clone <repository-url>
cd meet_automation
```

2. **Создание виртуального окружения:**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
# или
.\venv\Scripts\activate   # Windows
```

3. **Установка зависимостей:**
```bash
pip install -r requirements.txt
```

4. **Настройка переменных окружения:**
```bash
cp .env.example .env
# Отредактируйте .env файл, добавив необходимые ключи
```

## ⚙️ Конфигурация

1. **Настройка Google Cloud:**
   - Создайте проект в Google Cloud Console
   - Включите Calendar API и Meet API
   - Создайте Service Account и скачайте credentials.json

2. **Настройка Telegram бота:**
   - Создайте бота через @BotFather
   - Получите TELEGRAM_BOT_TOKEN
   - Добавьте бота в нужную группу
   - Получите CHAT_ID группы

3. **Переменные окружения:**
```env
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
OPENAI_API_KEY=your_openai_key
GOOGLE_CREDENTIALS_PATH=path/to/credentials.json
```

## 🚀 Запуск

### Локальный запуск

```bash
python main.py
```

### Запуск на сервере

```bash
sudo systemctl start meet-bot
```

### Проверка статуса

```bash
sudo systemctl status meet-bot
```

### Просмотр логов

```bash
sudo journalctl -u meet-bot -f
```

## 📝 Использование

1. **Создание встречи:**
   - Бот автоматически создает Google Meet встречу
   - Отправляет уведомление в указанный Telegram чат
   - Участники получают ссылку на встречу

2. **Во время встречи:**
   - Бот записывает разговор
   - Создает транскрипцию в реальном времени

3. **После встречи:**
   - Генерирует краткое резюме
   - Публикует результаты в Telegram

## 👥 Вклад в проект

Если вы хотите внести свой вклад в проект:
1. Создайте форк репозитория
2. Создайте ветку для вашей функции (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте изменения в ваш форк (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Распространяется под лицензией MIT. Смотрите `LICENSE` для получения дополнительной информации.

## 🤝 Поддержка

При возникновении проблем создавайте issue в репозитории проекта.

## 🔗 Полезные ссылки

- [Google Calendar API Documentation](https://developers.google.com/calendar)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [Python-Telegram-Bot](https://python-telegram-bot.org/)