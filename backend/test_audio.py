from services.audio_generator import generate_audio
import os

try:
    generate_audio('This is a test', 'temp/test.mp3')
    print(f'Audio file created: {os.path.exists("temp/test.mp3")}')
    print('Audio generation successful!')
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
    import traceback
    traceback.print_exc()
