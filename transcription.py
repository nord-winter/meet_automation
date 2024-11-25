# meet_automation/transcription.py
import whisper
from pydub import AudioSegment

class TranscriptionManager:
    def __init__(self):
        self.model = whisper.load_model("base")
    
    def transcribe_audio(self, audio_path):
        # Конвертация аудио в формат WAV, если необходимо
        audio = AudioSegment.from_file(audio_path)
        wav_path = audio_path.rsplit('.', 1)[0] + '.wav'
        audio.export(wav_path, format="wav")
        
        # Транскрибация
        result = self.model.transcribe(wav_path)
        return result["text"]