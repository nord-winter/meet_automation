# meet_automation/transcription.py
import whisper
from pydub import AudioSegment
import os

class TranscriptionManager:
    def __init__(self):
        # Проверяем наличие модели в кеше
        cache_dir = os.path.expanduser("~/.cache/whisper")
        os.makedirs(cache_dir, exist_ok=True)
        self.model = whisper.load_model("base", download_root=cache_dir)
    
    def transcribe_audio(self, audio_path):
        # Конвертация аудио в формат WAV, если необходимо
        audio = AudioSegment.from_file(audio_path)
        wav_path = audio_path.rsplit('.', 1)[0] + '.wav'
        audio.export(wav_path, format="wav")
        
        # Транскрибация
        result = self.model.transcribe(wav_path)
        
        # Удаляем временный WAV файл
        if wav_path != audio_path:
            os.remove(wav_path)
            
        return result["text"]