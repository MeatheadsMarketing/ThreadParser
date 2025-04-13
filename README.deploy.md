# 🚀 ThreadParser – Deployment Instructions

This guide covers how to deploy the current folder (`ThreadParser/`) to GitHub cleanly and version it for system-level automation.

---

## ✅ Prerequisites

- A GitHub repo at: https://github.com/MeatheadsMarketing/ThreadParser
- Git installed locally
- A virtualenv initialized via:
  ```bash
  bash venv_setup.sh
  ```

---

## 🔄 Commit + Push Workflow

```bash
cd ThreadParser
python3 push_threadparser_v1_1_5_updated.py
```

This script will:
- Initialize Git if needed
- Add the remote ThreadParser repo
- Commit all files
- Pull `main` to avoid fast-forward errors
- Push your commit with `v1.1.5` tag

---

## 🔖 Tags + Logs

Every commit should be tagged like:
- `v1.1.4` = Sync + validation
- `v1.1.5` = Modular folder structure

All future releases should increment and log changes in `project_manifest.json`.

---

## 🧠 Tip

Use `project_guard.py` to ensure no cross-project scripts run inside ThreadParser.