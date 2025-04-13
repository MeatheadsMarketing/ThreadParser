import os
import importlib.util
import pandas as pd
import json

REQUIRED_FILES = [
    'Applet_Matrix.csv',
    'sync/thread_index.json',
    'tabs/tab_tiles.py',
    'tabs/tile_expander.py',
    'tabs/tile_heatmap.py',
    'validators/tile_status_engine.py',
    'sync/applet_matrix_loader.py'
]

def check_files():
    print("\n📁 File Structure Check")
    for path in REQUIRED_FILES:
        status = "✅" if os.path.exists(path) else "❌"
        print(f"{status} {path}")

def check_import(module_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    try:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"✅ Import test passed: {module_name}")
    except Exception as e:
        print(f"❌ Import test failed: {module_name}")
        print(f"   ↳ {e}")

def test_csv_parsing():
    print("\n📄 CSV + JSON Parsing Test")
    try:
        df = pd.read_csv("Applet_Matrix.csv")
        print(f"✅ Applet_Matrix.csv loaded — {len(df)} rows")
    except Exception as e:
        print(f"❌ Failed to load Applet_Matrix.csv — {e}")

    try:
        with open("sync/thread_index.json") as f:
            data = json.load(f)
            print(f"✅ thread_index.json loaded — {len(data)} entries")
    except Exception as e:
        print(f"❌ Failed to load thread_index.json — {e}")

def suggest_fixes():
    print("\n🛠 Suggested Fixes")
    if not os.path.exists("tabs/__init__.py"):
        print("🔧 Add __init__.py inside /tabs/ to fix module import")
    if not os.path.exists("sync/__init__.py"):
        print("🔧 Add __init__.py inside /sync/ to enable imports")
    if not os.path.exists("validators/__init__.py"):
        print("🔧 Add __init__.py inside /validators/ for safety")

if __name__ == '__main__':
    print("\n🧪 Running ThreadParser Dashboard Diagnostic")
    check_files()
    test_csv_parsing()
    check_import("tabs/tab_tiles.py", "tab_tiles")
    check_import("sync/applet_matrix_loader.py", "applet_matrix_loader")
    check_import("validators/tile_status_engine.py", "tile_status_engine")
    suggest_fixes()