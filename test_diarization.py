from diarization.diarizer import diarize

segments = diarize("samples/audio/test.wav")

for s in segments:
    print(s)
