from io import BytesIO
from gtts import gTTS


class TextToSpeech:
    def speak(self, text, lang="en"):
        try:
            cleaned = (text or "").strip()

            if not cleaned:
                return
            
            buffer = BytesIO()

            gTTS(text=cleaned, lang=lang).write_to_fp(buffer)

            buffer.seek(0)

            return buffer.read()
        except Exception as e:
            print(f"Error in tts.py {e}")
    