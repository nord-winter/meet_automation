from config import *
from google_meet import GoogleMeetManager
from telegram_bot import TelegramNotifier
import datetime

def main():
    # Инициализация только необходимых компонентов
    meet_manager = GoogleMeetManager(GOOGLE_CREDENTIALS_PATH)
    telegram = TelegramNotifier(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
    
    try:
        # Создание встречи
        start_time = datetime.datetime.now() + datetime.timedelta(hours=1)
        meeting_link = meet_manager.create_meeting(
            "Тестовая встреча",
            start_time
        )
        
        # Отправка уведомления
        telegram.notify_new_meeting(
            meeting_link,
            "Тестовая встреча",
            start_time
        )
        print("✅ Встреча успешно создана и уведомление отправлено!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()