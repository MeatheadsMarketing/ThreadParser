import os
import subprocess

REPO_URL = "https://github.com/MeatheadsMarketing/ThreadParser.git"
COMMIT_MESSAGE = "🚀 Initial commit: ThreadParser Viewer v1.1 (Fixed app.py)"
RELEASE_TAG = "v1.1"

def run_git_commands():
    commands = [
        "git init",
        f"git remote add origin {REPO_URL}",
        "git add .",
        f'git commit -m "{COMMIT_MESSAGE}"',
        "git branch -M main",
        f"git tag {RELEASE_TAG}",
        "git push origin main --tags"
    ]
    for cmd in commands:
        print(f"Executing: {cmd}")
        subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
    run_git_commands()