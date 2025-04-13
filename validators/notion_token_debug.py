import os
from dotenv import load_dotenv, find_dotenv

print("🔍 Notion Token Debugger Starting...")

env_path = find_dotenv()
print(f"✅ .env path detected: {env_path if env_path else '❌ Not found'}")

load_dotenv(dotenv_path=env_path)
notion_token = os.getenv("NOTION_API_KEY")
database_id = os.getenv("NOTION_DATABASE_ID")

if notion_token:
    print(f"✅ NOTION_API_KEY loaded: {notion_token[:10]}...{notion_token[-5:]}")
else:
    print("❌ NOTION_API_KEY not loaded.")

if database_id:
    print(f"✅ NOTION_DATABASE_ID: {database_id}")
else:
    print("❌ NOTION_DATABASE_ID not loaded.")

print("""\n📡 Request headers preview:
Authorization: Bearer <token>
Notion-Version: 2022-06-28
Content-Type: application/json
""")