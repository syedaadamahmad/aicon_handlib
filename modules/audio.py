from gtts import gTTS
import os
import base64
from typing import Optional, Dict

class AudioManager:
    def __init__(self):
        self.angka_teks: Dict[int, str] = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
        }
        
        # Setup cache directory
        self.cache_dir = os.path.join(os.getcwd(), "audio_cache")
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def get_text_for_number(self, number: int) -> Optional[str]:
        return self.angka_teks.get(number)

    def get_audio_html(self, text: str) -> str:
        """Generate HTML audio tag with base64 encoded audio"""
        try:
            filename = f"{text}_en.mp3"
            file_path = os.path.join(self.cache_dir, filename)

            # Generate audio if it doesn't exist
            if not os.path.exists(file_path):
                tts = gTTS(text=text, lang='en', tld='com')
                tts.save(file_path)

            # Read file and encode to base64
            with open(file_path, "rb") as f:
                audio_bytes = f.read()
            
            audio_base64 = base64.b64encode(audio_bytes).decode()
            
            # HTML for autoplaying audio
            return f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_base64}">'
        except Exception as e:
            return ""
