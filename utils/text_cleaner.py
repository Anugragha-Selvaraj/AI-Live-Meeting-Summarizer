def clean_and_merge_transcript(lines):
    cleaned = []
    last_speaker = None
    buffer = []

    for line in lines:
        if ":" not in line:
            continue

        speaker, text = line.split(":", 1)
        speaker = speaker.strip()
        text = text.strip()

        # skip Unknown speakers
        if speaker.lower() == "unknown":
            continue

        # remove fillers (basic)
        fillers = ["um", "uh", "yeah", "hmm"]
        for f in fillers:
            text = text.replace(f, "").strip()

        if speaker == last_speaker:
            buffer.append(text)
        else:
            if buffer:
                cleaned.append(f"{last_speaker}: {' '.join(buffer)}")
            buffer = [text]
            last_speaker = speaker

    if buffer:
        cleaned.append(f"{last_speaker}: {' '.join(buffer)}")

    return cleaned
