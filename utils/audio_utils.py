import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="output.wav", duration=5, fs=44100):
    print("Recording started...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("Recording saved as", filename)
