# test_bot.py
import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio

async def test_bot():
    load_dotenv()
    
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    topic_id = os.getenv('TELEGRAM_TOPIC_ID')  # Добавляем ID топика
    
    try:
        bot = Bot(token=bot_token)
        
        await bot.send_message(
            chat_id=chat_id,
            message_thread_id=topic_id,
            text="🎉Есть тут что нибудь вкусное! Кс-кс-кскс 🐈!"
        )
        print("Сообщение успешно отправлено в топик!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(test_bot())