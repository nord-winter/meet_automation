# meet_automation/main.py
from config import *
from google_meet import GoogleMeetManager
from telegram_bot import TelegramNotifier
from transcription import TranscriptionManager
from summarization import SummarizationManager
import datetime

def main():
    # Инициализация компонентов
    meet_manager = GoogleMeetManager(GOOGLE_CREDENTIALS_PATH)
    telegram = TelegramNotifier(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
    transcriber = TranscriptionManager()
    summarizer = SummarizationManager(OPENAI_API_KEY)
    
    # Создание встречи
    start_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    meeting_link = meet_manager.create_meeting(
        "Еженедельная командная встреча",
        start_time
    )
    
    # Отправка уведомления
    telegram.notify_new_meeting(
        meeting_link,
        "Еженедельная командная встреча",
        start_time
    )
    
    # После записи встречи:
    audio_path = "path/to/recording.mp3"  # Здесь должен быть путь к записи
    
    # Транскрибация
    transcription = transcriber.transcribe_audio(audio_path)
    
    # Создание резюме
    summary = summarizer.create_summary(transcription)
    
    # Публикация резюме
    telegram.send_message(f"📋 <b>Резюме встречи:</b>\n\n{summary}")

if __name__ == "__main__":
    main()