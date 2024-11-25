# meet_automation/google_meet.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

class GoogleMeetManager:
    SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events'
    ]
    
    def __init__(self, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=self.SCOPES
        )
        self.service = build('calendar', 'v3', credentials=self.credentials)
    
    def create_meeting(self, summary, start_time, duration_minutes=60):
        event = {
            'summary': summary,
            'description': 'Meeting created by Meet Bot',
            'start': {
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': 'Asia/Bangkok',
            },
            'end': {
                'dateTime': (start_time + datetime.timedelta(minutes=duration_minutes)).strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': 'Asia/Bangkok',
            },
            'conferenceData': {
                'createRequest': {
                    'requestId': f"meet_{int(datetime.datetime.now().timestamp())}",
                    'conferenceSolutionKey': {
                        'type': 'hangoutsMeet'
                    }
                }
            },
            'reminders': {
                'useDefault': True
            }
        }
        
        try:
            print("Creating event with the following data:")
            print(f"Summary: {summary}")
            print(f"Start time: {start_time}")
            print(f"Duration: {duration_minutes} minutes")
            
            event = self.service.events().insert(
                calendarId='primary',
                conferenceDataVersion=1,
                body=event,
                sendNotifications=True
            ).execute()
            
            print("Event created successfully!")
            print("Full response:", event)
            
            # Получаем ссылку на встречу
            meet_link = ''
            if 'conferenceData' in event:
                print("Conference data found in response")
                print("Conference data:", event['conferenceData'])
                if 'entryPoints' in event['conferenceData']:
                    for entryPoint in event['conferenceData']['entryPoints']:
                        if entryPoint.get('entryPointType') == 'video':
                            meet_link = entryPoint.get('uri', '')
                            print(f"Found meet link: {meet_link}")
                            break
            
            return meet_link
            
        except Exception as e:
            print(f"❌ Ошибка при создании встречи: {str(e)}")
            print("Полное событие:")
            print(event)
            raise