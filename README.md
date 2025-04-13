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