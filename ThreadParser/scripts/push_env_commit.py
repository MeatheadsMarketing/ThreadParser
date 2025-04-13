import subprocess

COMMIT_MESSAGE = "🔐 Add .env.example + update Notion sync for dotenv (v1.1.2)"
TAG = "v1.1.2"

def push_env_files():
    commands = [
        "git add .env.example notion_sync_threadparser.py",
        f'git commit -m "{COMMIT_MESSAGE}"',
        f"git tag {TAG}",
        "git push origin main --tags"
    ]
    for cmd in commands:
        print(f"Executing: {cmd}")
        subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
    push_env_files()