import datetime
import os

def log(message, log_file=".streamlit/test_runner.log"):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, "a") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {message}\n")

if __name__ == '__main__':
    log("🧪 Diagnostic runner executed successfully.")