import os
import requests
import json

# === CONFIG ===
NOTION_API_KEY = os.getenv("NOTION_API_KEY")  # Set this in your .env
DATABASE_ID = os.getenv("NOTION_THREADPARSER_DB")  # Notion DB for version logs

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_notion_page(version, description, files, tags):
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Version": {"title": [{"text": {"content": version}}]},
            "Description": {"rich_text": [{"text": {"content": description}}]},
            "Files": {"rich_text": [{"text": {"content": ', '.join(files)}}]},
            "Tags": {"multi_select": [{"name": tag} for tag in tags]}
        }
    }
    response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
    if response.status_code == 200:
        print("✅ Synced to Notion successfully.")
    else:
        print(f"❌ Notion sync failed: {response.status_code}", response.text)

# === USAGE EXAMPLE ===
if __name__ == '__main__':
    create_notion_page(
        version="v1.1.1",
        description="Add Streamlit preview + theme support",
        files=["app.py", "thread_index.json", "thread_FULL_EXPORT_REBUILT.md", "ThreadParserViewer_preview.png"],
        tags=["viewer", "markdown", "streamlit", "demo"]
    )