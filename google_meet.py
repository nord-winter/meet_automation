# meet_automation/google_meet.py
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime

class GoogleMeetManager:
    SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events'
    ]
    
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
                'timeZone': 'Asia/Bangkok',  # Используем правильный часовой пояс
            },
            'end': {
                'dateTime': (start_time + datetime.timedelta(minutes=duration_minutes)).isoformat(),
                'timeZone': 'Asia/Bangkok',
            },
            'conferenceData': {
                'createRequest': {
                    'requestId': f"meet_{datetime.datetime.now().timestamp()}",
                    'conferenceSolutionKey': {
                        'type': 'hangoutsMeet'
                    }
                }
            }
        }
        
        try:
            event = self.service.events().insert(
                calendarId='primary',
                conferenceDataVersion=1,
                body=event
            ).execute()
            
            # Получаем ссылку на встречу
            meet_link = ''
            if 'conferenceData' in event and 'entryPoints' in event['conferenceData']:
                for entryPoint in event['conferenceData']['entryPoints']:
                    if entryPoint.get('entryPointType') == 'video':
                        meet_link = entryPoint.get('uri', '')
                        break
            
            return meet_link
        except Exception as e:
            print(f"❌ Ошибка при создании встречи: {str(e)}")
            raise