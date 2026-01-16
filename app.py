import streamlit as st
from utils.audio_utils import record_audio
from stt.stt_engine import transcribe

st.title("🎙️ AI Live Meeting Summarizer")

if st.button("Record 15 Seconds"):
    record_audio("meeting.wav", duration=15)
    st.success("Recording done!")

if st.button("Transcribe"):
    text = transcribe("meeting.wav")
    st.text_area("Transcription", text, height=200)
