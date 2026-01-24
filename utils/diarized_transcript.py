from stt.stt_engine import transcribe_with_segments
from diarization.diarizer import diarize

def generate_diarized_transcript(audio_path):
    stt_segments = transcribe_with_segments(audio_path)
    diarization_segments = diarize(audio_path)

    diarized_text = []

    for stt in stt_segments:
        stt_start = stt["start"]
        stt_end = stt["end"]
        text = stt["text"]

        speaker_label = "Unknown"

        for d in diarization_segments:
            if d["start"] <= stt_start <= d["end"]:
                speaker_label = d["speaker"]
                break

        diarized_text.append(f"[{speaker_label}]: {text.strip()}")

    return diarized_text
