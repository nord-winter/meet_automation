# meet_automation/config.py
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GOOGLE_CREDENTIALS_PATH = os.getenv('GOOGLE_CREDENTIALS_PATH')

# meet_automation/google_meet.py
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime

class GoogleMeetManager:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    def __init__(self, credentials_path):
        self.credentials = self._get_credentials(credentials_path)
        self.service = build('calendar', 'v3', credentials=self.credentials)
    
    def _get_credentials(self, credentials_path):
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_path, self.SCOPES)
        return flow.run_local_server(port=0)
    
    def create_meeting(self, summary, start_time, duration_minutes=60):
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': (start_time + datetime.timedelta(minutes=duration_minutes)).isoformat(),
                'timeZone': 'UTC',
            },
            'conferenceData': {
                'createRequest': {
                    'requestId': f"meeting_{datetime.datetime.now().timestamp()}",
                    'conferenceSolutionKey': {'type': 'hangoutsMeet'}
                }
            }
        }
        
        event = self.service.events().insert(
            calendarId='primary',
            conferenceDataVersion=1,
            body=event
        ).execute()
        
        return event.get('conferenceData', {}).get('entryPoints', [{}])[0].get('uri', '')
