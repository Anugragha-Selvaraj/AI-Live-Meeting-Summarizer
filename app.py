import streamlit as st
from utils.audio_utils import record_audio
from utils.diarized_transcript import generate_diarized_transcript

AUDIO_FILE = "meeting.wav"

st.title("🎙️ AI Live Meeting Summarizer")

st.markdown("### Controls")

if st.button("🎤 Record 15 Seconds"):
    with st.spinner("Recording..."):
        record_audio(AUDIO_FILE, duration=15)
    st.success("Recording completed!")

if st.button("🧠 Generate Diarized Transcript"):
    with st.spinner("Processing audio..."):
        diarized_output = generate_diarized_transcript(AUDIO_FILE)

    st.markdown("## 👥 Diarized Transcript")
    for line in diarized_output:
        st.write(line)
