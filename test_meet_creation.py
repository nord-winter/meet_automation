from dotenv import load_dotenv
import os
import datetime
from google_meet import GoogleMeetManager

def test_meet_creation():
    load_dotenv()
    
    credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')
    print(f"Using credentials from: {credentials_path}")
    
    try:
        # Создаем экземпляр менеджера
        meet_manager = GoogleMeetManager(credentials_path)
        print("✅ GoogleMeetManager initialized successfully")
        
        # Создаем тестовую встречу
        start_time = datetime.datetime.now() + datetime.timedelta(hours=1)
        meeting_link = meet_manager.create_meeting(
            "Test Meeting",
            start_time,
            duration_minutes=30
        )
        
        if meeting_link:
            print(f"✅ Meeting created successfully!")
            print(f"Meeting link: {meeting_link}")
        else:
            print("❌ No meeting link returned")
            
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")

if __name__ == "__main__":
    test_meet_creation()