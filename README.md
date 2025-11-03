# 📝 Meeting Notes & Action Item Extractor

## 📘 Project Overview
The **Meeting Notes and Action Item Extractor** is a local AI-powered application that converts **meeting audio** into **structured notes and actionable tasks**.  
It uses **Whisper** for speech-to-text transcription and **LLaMA 3 (via Ollama)** for summarization — all running **locally** without internet or API keys.

---

## ⚙️ Requirements

### 🧩 Software & Libraries
| Component | Purpose | Installation |
|------------|----------|--------------|
| Python 3.10+ | Programming Language | [Python.org](https://www.python.org/) |
| Streamlit | Frontend Web Framework | `pip install streamlit` |
| Faster Whisper | Local Speech-to-Text Model | `pip install faster-whisper` |
| Ollama | Local LLM Engine | [Install Ollama](https://ollama.ai/download) |
| Requests | To communicate with Ollama’s local API | `pip install requests` |

### 🖥️ Hardware
- CPU or GPU-supported system (for Whisper processing)
- At least 8 GB RAM recommended
- Disk space: 2–4 GB (for Whisper + LLaMA models)

---

## 🧭 Workflow

### Step 1 — Upload Audio File
User uploads a meeting recording (`.mp3` or `.wav`) through the Streamlit interface.

### Step 2 — Transcription
The **Faster-Whisper model** converts spoken dialogue into text.  
It processes the file locally without cloud services, ensuring privacy.

### Step 3 — Summarization and Extraction
Once the transcript is ready, the **LLaMA 3** model (via **Ollama**) is prompted to extract:  
- ✅ **Meeting summary**  
- 📋 **Key decisions**  
- 🧾 **Action items / next steps**  

### Step 4 — Output Display
The final structured output is shown on the Streamlit UI as a clear list of meeting notes and actions.

---

## 🧩 Solution Architecture

```
        ┌───────────────┐
        │   Streamlit   │  ← Upload audio
        └──────┬────────┘
               │
               ▼
        ┌───────────────┐
        │ Faster-Whisper│  ← Transcribes speech → text
        └──────┬────────┘
               │
               ▼
        ┌───────────────┐
        │   LLaMA 3     │  ← Extracts notes & actions
        │   (Ollama)    │
        └──────┬────────┘
               │
               ▼
        ┌───────────────┐
        │   Streamlit   │  ← Displays structured output
        └───────────────┘
```

---

## 🧰 Setup Instructions

### 1️⃣ Install Dependencies
```bash
pip install streamlit faster-whisper requests
```

### 2️⃣ Install and Run Ollama
```bash
ollama run llama3
```

### 3️⃣ Launch Streamlit App
```bash
streamlit run meeting_notes_app.py
```

---

## ⚠️ Issues Faced & Rectifications

| Issue | Cause | Solution |
|--------|--------|-----------|
| `ModuleNotFoundError: No module named 'whisper'` | Whisper library not installed | Installed `faster-whisper` instead of deprecated `whisper` |
| `TypeError: argument of type 'NoneType' is not iterable` | Audio not saved correctly before transcription | Ensured file is written using binary mode `wb` |
| `ConnectionError: Could not connect to Ollama` | Ollama service not running | Fixed by running `ollama run llama3` before app execution |
| Model takes long to load | Whisper model loaded multiple times | Used `@st.cache_resource` to load once per session |
| Incomplete or missing summary | Input text too short or unclear | Added clear prompt to guide LLaMA for structured extraction |

---

## 🧠 Concepts Involved

| Concept | Description |
|----------|-------------|
| **Automatic Speech Recognition (ASR)** | Converts spoken words into text using Whisper |
| **Transcription** | The process of converting audio to text representation |
| **Summarization** | Condensing long text into key highlights and points |
| **Local LLM (Ollama)** | Runs models like LLaMA 3 locally without external APIs |
| **Prompt Engineering** | Framing clear and specific instructions for LLM output |
| **Streamlit** | Frontend tool for uploading files and displaying results |

---

## 🏁 Outcome
This project demonstrates how meetings can be summarized automatically using **open-source, local AI models**.  
It improves productivity by saving time on manual note-taking and ensures **data privacy** by keeping all processing on the local machine.

---

## 🚀 Future Enhancements
- Integrate speaker diarization (who said what)
- Add action item tracking across sessions
- Support multiple meeting formats (Zoom, MS Teams, etc.)
- Provide voice playback for summaries

---

## 👩‍💻 Author
**Saranya P**  
*SEQATO LLM Awareness & Portfolio Development Program – Phase 2 Project*

---

## 📚 References
- [Streamlit Documentation](https://streamlit.io)
- [Faster Whisper GitHub](https://github.com/guillaumekln/faster-whisper)
- [Ollama Models](https://ollama.ai/library)
- [LLaMA 3 Model Overview](https://ai.meta.com/llama/)
