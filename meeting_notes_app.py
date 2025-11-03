import streamlit as st
from faster_whisper import WhisperModel
import requests

# Load Whisper model only once
@st.cache_resource
def load_model():
    return WhisperModel("base")

model = load_model()

# Streamlit UI
st.title("📝 Local Meeting Notes & Action Item Extractor (No API Key)")

uploaded_file = st.file_uploader("Upload a meeting audio file (.mp3/.wav)", type=["mp3", "wav"])

if uploaded_file:
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Transcribing with Whisper...")
    segments, _ = model.transcribe("temp_audio.wav")
    full_text = "".join([segment.text for segment in segments])

    st.subheader("🗣️ Transcribed Text:")
    st.write(full_text)

    st.info("Analyzing locally using LLaMA3...")

    # Call Ollama
    prompt = f"Extract key meeting notes and action items from the following transcript:\n\n{full_text}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    if response.ok:
        result = response.json()["response"]
        st.subheader("🧾 Summary & ✅ Action Items:")
        st.write(result)
    else:
        st.error("Failed to generate response from local LLM. Is Ollama running?")
