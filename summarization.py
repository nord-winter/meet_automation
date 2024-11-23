# meet_automation/summarization.py
import openai

class SummarizationManager:
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def create_summary(self, transcription):
        prompt = f"""
        Создайте краткое и информативное резюме следующей встречи.
        Включите основные обсуждаемые темы, принятые решения и следующие шаги.
        Избегайте несущественной информации.
        
        Транскрипция встречи:
        {transcription}
        """
        
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Вы - профессиональный ассистент, создающий четкие и структурированные резюме деловых встреч."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content