import os
import sys
from pathlib import Path

def assert_project(expected_project_name: str):
    current_project = os.getenv("PROJECT_ID")
    cwd_name = Path.cwd().name

    print(f"🔒 Project Context Check")
    print(f"📁 Current Folder: {cwd_name}")
    print(f"📦 PROJECT_ID from .env: {current_project}")

    if not current_project:
        print("❌ PROJECT_ID is missing from .env.")
        sys.exit(1)

    if expected_project_name.lower() not in cwd_name.lower():
        print(f"❌ Misalignment Detected: Script expects '{expected_project_name}', but folder is '{cwd_name}'")
        sys.exit(1)

    print("✅ Project context is aligned and safe to proceed.")

if __name__ == '__main__':
    # Example: Replace with 'ThreadParser' or 'HeaderMatrix' depending on your folder
    assert_project("HeaderMatrix")