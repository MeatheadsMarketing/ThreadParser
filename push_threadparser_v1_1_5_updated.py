import subprocess

REPO_URL = "https://github.com/MeatheadsMarketing/ThreadParser.git"
COMMIT_MSG = "📦 Reorganize ThreadParser structure with modular folders and updated README (v1.1.5)"
TAG = "v1.1.5"

def push_threadparser_bundle():
    commands = [
        "git init",
        f"git remote add origin {REPO_URL}",
        "git add .",
        f'git commit -m "{COMMIT_MSG}"',
        "git branch -M main",
        f"git tag {TAG}",
        "git pull origin main --rebase",  # Important for sync
        "git push origin main --tags"
    ]
    for cmd in commands:
        print(f"Running: {cmd}")
        subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
    push_threadparser_bundle()