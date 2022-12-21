from pydub import AudioSegment

def to_flac(filename: str):
    audio = AudioSegment.from_file(filename)
    audio.export(filename, format="flac")
