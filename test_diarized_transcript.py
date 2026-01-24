from utils.diarized_transcript import generate_diarized_transcript

output = generate_diarized_transcript("samples/audio/test.wav")

for line in output:
    print(line)
