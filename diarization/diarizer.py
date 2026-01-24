from pyannote.audio import Pipeline

# load pipeline once
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=True
)

def diarize(audio_path):
    """
    Perform speaker diarization on an audio file
    """
    diarization = pipeline(audio_path)

    segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "speaker": speaker,
            "start": turn.start,
            "end": turn.end
        })

    return segments
