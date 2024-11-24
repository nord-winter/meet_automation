# meet_automation/google_meet.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

class GoogleMeetManager:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    def __init__(self, credentials_path):
        self.credentials = self._get_credentials(credentials_path)
        self.service = build('calendar', 'v3', credentials=self.credentials)
    
    def _get_credentials(self, credentials_path):
        return service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=self.SCOPES
        )
    
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