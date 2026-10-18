from dotenv import load_dotenv
load_dotenv()   # MUST be before any core/ imports

from utils.audio_processor import process_input
from Core.transcriber import transcribe_all



source = "https://www.youtube.com/watch?v=z3Df2tlvUHY"
language = "hinglish"   # "english" → Whisper, "hinglish" → Sarvam



chunks = process_input(source)


transcript = transcribe_all(chunks, language=language)
print("\n===========Transcript==========\n")
print(transcript)