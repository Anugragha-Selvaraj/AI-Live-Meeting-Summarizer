import whisper

model = whisper.load_model("base")

def transcribe_with_segments(audio_path):
    result = model.transcribe(audio_path)

    return result["segments"]
