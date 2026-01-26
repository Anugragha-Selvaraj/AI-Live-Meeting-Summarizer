from stt.stt_engine import transcribe_with_segments
from diarization.diarizer import diarize

def generate_diarized_transcript(audio_path):
    stt_segments = transcribe_with_segments(audio_path)
    diarization_segments = diarize(audio_path)

    diarized_text = []
    last_speaker = None

    for stt in stt_segments:
        stt_start = stt["start"]
        text = stt["text"]

        speaker_label = None

        # 1️⃣ Direct overlap match
        for d in diarization_segments:
            if d["start"] <= stt_start <= d["end"]:
                speaker_label = d["speaker"]
                break

        # 2️⃣ If no overlap, use previous speaker
        if speaker_label is None and last_speaker is not None:
            speaker_label = last_speaker

        # 3️⃣ Cold start: use nearest diarization segment
        if speaker_label is None:
            nearest = min(
                diarization_segments,
                key=lambda d: abs(d["start"] - stt_start)
            )
            speaker_label = nearest["speaker"]

        last_speaker = speaker_label
        diarized_text.append(f"[{speaker_label}]: {text.strip()}")

    return diarized_text
