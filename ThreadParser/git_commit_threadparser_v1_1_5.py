import subprocess

COMMIT_MSG = "📦 Reorganize ThreadParser structure with modular folders and updated README (v1.1.5)"
TAG = "v1.1.5"

def push_threadparser_structure_update():
    commands = [
        "git add .",
        f'git commit -m "{COMMIT_MSG}"',
        f"git tag {TAG}",
        "git push origin main --tags"
    ]
    for cmd in commands:
        print(f"Running: {cmd}")
        subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
    push_threadparser_structure_update()