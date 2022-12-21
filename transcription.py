import whisper
from pydub import AudioSegment
import uuid
import os

def transcribeSegment(filename: str, start: float, end: float):
    model = whisper.load_model("small")

    audio = AudioSegment.from_file(filename)
    audio_chunk=audio[start * 1000 : end * 1000]
    segmentFilename = f"temp/{str(uuid.uuid4())}.flac"

    try:
        audio_chunk.export(segmentFilename, format="flac")
        transcribedSegment = model.transcribe(segmentFilename, task="transcribe")
    finally:
        os.remove(segmentFilename)

    return transcribedSegment["text"]
