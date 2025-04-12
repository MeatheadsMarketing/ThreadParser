# 🧠 ThreadParser Viewer

ThreadParser is a Streamlit-powered tool that allows you to visually navigate and analyze long GPT conversation threads. It helps you validate, export, and interact with messages extracted from ChatGPT threads in strict Markdown format.

## 🔍 Features
- Full message timeline (MSG_001–MSG_100+)
- Role + formatting filters (user/GPT, tables, code, etc.)
- Raw vs. rebuilt Markdown block display
- Export individual messages to `.md` or `.txt`
- Ready for Notion, GitHub, and Streamlit deployment

## 📂 Files Included
- `app.py` — main Streamlit app
- `thread_index.json` — maps message metadata
- `thread_FULL_EXPORT_REBUILT.md` — the full message export from ChatGPT
- `README.md` — this file

## 🚀 Deployment Instructions
To run locally:
```bash
streamlit run app.py
```

Or deploy on [Streamlit Cloud](https://streamlit.io/cloud) using this repo.

## 📦 Generated with GPT + Thread Intelligence Export Pipeline