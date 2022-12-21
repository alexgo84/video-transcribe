from fastapi import FastAPI, File, UploadFile

import transcription as transcription
import diarization as diarization
import convert as convert

import shutil
import os
import time

app = FastAPI()

@app.post("/file2text/")
async def transcribe_file(file: UploadFile = File(...)):
    file_location = f"temp/{file.filename}"
    try:
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
        whisperResult = transcribe(file_location)
    finally:
        file.file.close()
        os.remove(file_location)

    return whisperResult

def transcribe(filename: str):
    previousTimestamp = time.time()

    convert.to_flac(filename)
    print(f"converted to flac ({time.time() - previousTimestamp} s)")
    previousTimestamp = time.time()

    speakerTimestamps = diarization.get_speaker_timestamps(filename)
    print(f"got speaker timestamps ({time.time() - previousTimestamp} s)")
    print(f"\n\n{speakerTimestamps}\n\n")

    previousTimestamp = time.time()

    result = ""
    for start, end, speaker in speakerTimestamps:
        segmentTranscription = transcription.transcribeSegment(filename, start, end)
        result += f"{speaker}: {segmentTranscription}" + '\n'
        print(f"transcribed {end - start} seconds of audio to text ({time.time() - previousTimestamp} s)")
        previousTimestamp = time.time()
        

    return result
