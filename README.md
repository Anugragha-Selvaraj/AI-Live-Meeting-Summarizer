# 🎙️ AI Live Meeting Summarizer

An AI-powered web application that records or uploads meeting audio, identifies speakers, transcribes speech, generates a cleaned transcript, summarizes the discussion, and extracts action items.

---

## 🚀 Features

- 🎤 Record meeting audio or upload WAV files
- 👥 Speaker diarization (who spoke when)
- 📝 Speech-to-text transcription
- 📄 Cleaned transcript generation
- 🧠 Meeting summary generation
- ✅ Action item extraction
- 🖥️ Interactive Streamlit UI
- 🛡️ Basic error handling for better user experience

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – Web UI
- **Whisper** – Speech-to-text
- **pyannote.audio** – Speaker diarization
- **Transformers (Hugging Face)** – Text processing
- **PyTorch**
- **Git & GitHub**

---

## ⚙️ How It Works

1. User records or uploads a meeting audio file
2. Audio is transcribed using Whisper
3. Speaker diarization separates speakers
4. Transcript is cleaned and merged
5. Summary and action items are generated
6. Results are displayed in the Streamlit UI

---

## ▶️ How to Run

```bash
# Activate virtual environment
venv\Scripts\activate

# Run the app
streamlit run app.py
