import os

required_files = [
    ".env",
    "Applet_Matrix.csv",
    "validate_env.py",
    "venv_check.py",
    "notion_sync_threadparser.py"
]

required_dirs = [
    ".venv"
]

print("📦 Verifying scaffold for HeaderMatrix_HEAD-v1...")

# Check files
for file in required_files:
    if os.path.isfile(file):
        print(f"✅ {file} found")
    else:
        print(f"❌ {file} missing")

# Check folders
for directory in required_dirs:
    if os.path.isdir(directory):
        print(f"✅ {directory}/ exists")
    else:
        print(f"❌ {directory}/ not found")

print("\n👉 If any ❌ appear, run setup scripts or re-download missing components.")