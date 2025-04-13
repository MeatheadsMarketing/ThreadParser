import importlib.util

required = ['requests', 'dotenv']
missing = []

for pkg in required:
    if importlib.util.find_spec(pkg) is None:
        missing.append(pkg)

if not missing:
    print('✅ All required packages are installed inside the virtual environment.')
else:
    print('❌ Missing packages detected:')
    for pkg in missing:
        print(f'   - {pkg}')
    print('\nTo install them, activate your .venv and run:')
    print(f'   pip install {" ".join(missing)}')