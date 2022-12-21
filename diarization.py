from pyannote.audio import Pipeline



def get_speaker_timestamps(filename: str):
    pretrainedPipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token="-")
    diarization = pretrainedPipeline(filename, num_speakers=2)

    segmentStart, segmentEnd = 0.0, 0.0
    segments = []
    previousSpeaker = -1
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"{speaker}: {turn.start} - {turn.end}: {turn}")
        if previousSpeaker == speaker:
            segmentEnd = turn.end
        else:
            if previousSpeaker != -1:
                segments.append((segmentStart, segmentEnd, previousSpeaker))
                print("speaker changed!")
            segmentStart = turn.start
            segmentEnd = turn.end

        previousSpeaker = speaker
    
    segments.append((segmentStart, segmentEnd, previousSpeaker))
    return segments
