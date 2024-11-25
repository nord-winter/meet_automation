from config import *
from google_meet import GoogleMeetManager
from telegram_bot import TelegramNotifier
import datetime

def main():
    try:
        # Инициализация компонентов
        meet_manager = GoogleMeetManager(GOOGLE_CREDENTIALS_PATH)
        telegram = TelegramNotifier(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
        
        # Создание встречи
        start_time = datetime.datetime.now() + datetime.timedelta(hours=1)
        meeting_link = meet_manager.create_meeting(
            "Тестовая встреча",
            start_time
        )
        
        if meeting_link:
            # Отправка уведомления
            telegram.notify_new_meeting(
                meeting_link,
                "Тестовая встреча",
                start_time
            )
            print("✅ Встреча успешно создана и уведомление отправлено!")
        else:
            print("❌ Не удалось получить ссылку на встречу")
            
    except Exception as e:
        print(f"❌ Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()