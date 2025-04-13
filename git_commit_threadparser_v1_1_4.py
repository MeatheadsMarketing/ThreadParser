import subprocess

COMMIT_MSG = "🔒 Project isolation and manifest setup for ThreadParser (v1.1.4)"
TAG = "v1.1.4"

def push_threadparser_guarded_files():
    files = [
        "project_guard.py",
        "project_manifest.json",
        ".env.template.threadparser",
        
    ]
    commands = [
        "git add " + " ".join(files),
        f'git commit -m "{COMMIT_MSG}"',
        f"git tag {TAG}",
        "git push origin main --tags"
    ]
    for cmd in commands:
        print(f"Running: {cmd}")
        subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
    push_threadparser_guarded_files()