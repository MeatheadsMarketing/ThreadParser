#!/bin/bash

echo "🔧 Creating and activating .venv..."

python3 -m venv .venv
source .venv/bin/activate

echo "✅ Installing required packages..."
pip install --upgrade pip
pip install streamlit pandas matplotlib seaborn

echo "✅ Environment setup complete."
echo "You can now run: streamlit run run_ui.py"