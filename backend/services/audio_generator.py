from gtts.lang import tts_langs
from gtts import gTTS
import langdetect

def generate_audio(text: str, filename: str):
    from langdetect import detect
    language = detect(text)
    tts = gTTS(text=text, lang=language)
    tts.save(filename)