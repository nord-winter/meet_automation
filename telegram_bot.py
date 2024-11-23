# meet_automation/telegram_bot.py

import requests

class TelegramNotifier:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{bot_token}"
    
    def send_message(self, text):
        endpoint = f"{self.api_url}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
        response = requests.post(endpoint, data=data)
        return response.json()
    
    def notify_new_meeting(self, meeting_link, summary, start_time):
        message = (
            f"📢 <b>Новая встреча запланирована!</b>\n\n"
            f"📝 Тема: {summary}\n"
            f"🕒 Время: {start_time.strftime('%Y-%m-%d %H:%M')}\n"
            f"🔗 Ссылка: {meeting_link}"
        )
        return self.send_message(message)