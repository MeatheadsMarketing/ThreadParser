import subprocess

COMMIT_MESSAGE = "🎨 Add Streamlit theme + thumbnail preview (v1.1.1)"
TAG = "v1.1.1"

def push_theme_and_assets():
    commands = [
        "git add streamlit_app_settings.json ThreadParserViewer_preview.png",
        f'git commit -m "{COMMIT_MESSAGE}"',
        f"git tag {TAG}",
        "git push origin main --tags"
    ]
    for cmd in commands:
        print(f"Executing: {cmd}")
        subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
    push_theme_and_assets()