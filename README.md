HEAD
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

# 🧠 ThreadParser System – Modular Export Explorer

This project provides a full visual and backend toolkit for exploring ChatGPT thread exports, managing assistant metadata, and syncing to Notion.

---

## 📁 Folder Structure

```
ThreadParser/
├── app.py                      # Main Streamlit dashboard
├── README.md                   # Project overview
├── .env.template.threadparser  # Safe .env starter
├── /config/                    # Core config files
├── /validators/                # Environment + install checks
├── /sync/                      # Notion sync tools and exports
├── /assets/                    # Visuals and UI previews
├── /scripts/                   # GitHub push automation tools
```

---

## 🛠 Key Utilities

- **app.py** — Launch your visual assistant dashboard
- **thread_FULL_EXPORT_REBUILT.md** — Strict Markdown capture of full GPT thread
- **notion_sync_threadparser.py** — Push version updates to Notion DB
- **project_guard.py** — Prevents cross-project script contamination

---

## 🚀 Setup

```bash
bash reorganize_threadparser.sh
bash scripts/venv_setup.sh
source .venv/bin/activate
python3 validators/validate_env.py
```

---

## ✅ Validated: `v1.1.4`
90f029a (📦 Reorganize ThreadParser structure with modular folders and updated README (v1.1.5))
