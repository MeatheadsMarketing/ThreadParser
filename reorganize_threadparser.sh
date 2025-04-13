#!/bin/bash

echo "🧹 Reorganizing ThreadParser folder..."

# Create folder structure
mkdir -p config validators sync assets scripts

# Move files into correct subfolders
mv streamlit_app_settings.json project_manifest.json project_guard.py config/
mv validate_env.py venv_check.py notion_token_debug.py scaffold_check_header_v1.py validators/
mv notion_sync_threadparser.py thread_index.json thread_FULL_EXPORT_REBUILT.md sync/
mv ThreadParserViewer_preview.png assets/
mv push_*.py scripts/

echo "✅ ThreadParser folder reorganized."