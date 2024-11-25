# Создайте файл test_auth.py
import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

def test_auth():
    load_dotenv()
    
    # Получаем путь к файлу с учетными данными
    creds_path = os.getenv('GOOGLE_CREDENTIALS_PATH')
    print(f"Проверяем файл: {creds_path}")
    
    try:
        # Создаем учетные данные
        credentials = service_account.Credentials.from_service_account_file(
            creds_path,
            scopes=['https://www.googleapis.com/auth/calendar']
        )
        
        # Пробуем создать сервис
        service = build('calendar', 'v3', credentials=credentials)
        
        # Делаем тестовый запрос
        calendars = service.calendarList().list().execute()
        print("✅ Успешно подключились к Google Calendar!")
        print(f"Найдено календарей: {len(calendars.get('items', []))}")
        
    except Exception as e:
        print(f"❌ Ошибка: {str(e)}")

if __name__ == "__main__":
    test_auth()