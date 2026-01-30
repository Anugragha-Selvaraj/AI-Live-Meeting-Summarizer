import streamlit as st
import os

from utils.text_cleaner import clean_and_merge_transcript
from utils.summarizer import generate_summary
from utils.action_items import extract_action_items

from utils.audio_utils import record_audio
from utils.diarized_transcript import generate_diarized_transcript

AUDIO_FILE = "meeting.wav"

st.title("🎙️ AI Live Meeting Summarizer")
st.caption("Record a meeting, identify speakers, summarize discussion and extract action items.")
st.divider()

st.markdown("### Controls")

if st.button("🎤 Record 15 Seconds"):
    with st.spinner("Recording..."):
        record_audio(AUDIO_FILE, duration=15)
    st.success("Recording completed!")

if st.button("🧠 Generate Diarized Transcript"):

    if not os.path.exists(AUDIO_FILE):
        st.error("❌ Audio file not found. Please record audio first.")
    else:
        with st.spinner("Processing audio..."):
            diarized_output = generate_diarized_transcript(AUDIO_FILE)
            if not diarized_output:
                st.warning("⚠️ No speech detected in the audio.")
                st.stop()





    st.subheader("👥 Diarized Transcript")
    for line in diarized_output:
        st.markdown(f"- {line}")


    cleaned_lines = clean_and_merge_transcript(diarized_output)
    cleaned_text = " ".join(cleaned_lines)

    st.subheader("📄 Cleaned Transcript")
    st.text_area("Cleaned Output", cleaned_text, height=150)


    if cleaned_text.strip():
        summary = generate_summary(cleaned_text)
    else:
        summary = "No content available to summarize."


    st.subheader("🧠 Meeting Summary")
    st.success(summary)


    actions = extract_action_items(cleaned_text) if cleaned_text.strip() else []


    st.subheader("✅ Action Items")
    for a in actions:
        st.checkbox(a)
