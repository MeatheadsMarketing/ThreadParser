import subprocess

COMMIT_MSG = "🧠 Project lock-in, validation tools, and manifest scaffolding (v1.1.4)"
TAG = "v1.1.4"

def push_bundle():
    commands = [
        "cd ThreadParser_FINAL/ThreadParser_FINAL_BUNDLE_v1.1.4",
        "git init",
        "git remote add origin https://github.com/MeatheadsMarketing/ThreadParser.git",
        "git add .",
        f'git commit -m "{COMMIT_MSG}"',
        "git branch -M main",
        f"git tag {TAG}",
        "git push origin main --tags"
    ]
    for cmd in commands:
        print(f"Running: {cmd}")
        subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
    push_bundle()