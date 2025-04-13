import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

print("🔍 Validating .env values...")
if not NOTION_API_KEY:
    print("❌ NOTION_API_KEY is missing or not set.")
else:
    print("✅ NOTION_API_KEY loaded.")

if not NOTION_DATABASE_ID:
    print("❌ NOTION_DATABASE_ID is missing or not set.")
else:
    print("✅ NOTION_DATABASE_ID loaded.")

print("\n🌐 Testing API access...")
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28"
}

# Correct endpoint to validate database access
url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ API access confirmed. Database is reachable.")
else:
    print(f"❌ API access failed. Status {response.status_code}")
    print("Details:", response.text)