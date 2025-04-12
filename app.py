import streamlit as st
import json
from pathlib import Path
import re

st.set_page_config(page_title="ThreadParser Viewer", layout="wide")

# Load thread index and markdown content
index_path = Path("thread_index.json")
markdown_path = Path("thread_FULL_EXPORT_REBUILT.md")

if index_path.exists():
    with open(index_path, "r") as f:
        thread_index = json.load(f)
else:
    st.error("Missing thread_index.json")
    st.stop()

if markdown_path.exists():
    full_markdown = markdown_path.read_text(encoding="utf-8")
else:
    st.error("Missing thread_FULL_EXPORT_REBUILT.md")
    st.stop()

# Extract messages using MSG_### headers
msg_blocks = {}
current_msg = None
buffer = []
for line in full_markdown.splitlines():
    match = re.match(r"### (MSG_\d{3})", line)
    if match:
        if current_msg and buffer:
            msg_blocks[current_msg] = "\n".join(buffer).strip()
        current_msg = match.group(1)
        buffer = [line]
    elif current_msg:
        buffer.append(line)
if current_msg and buffer:
    msg_blocks[current_msg] = "\n".join(buffer).strip()

# Sidebar filters
st.sidebar.title("📌 Filters")
role_filter = st.sidebar.multiselect("Select Roles", ["user", "gpt"], default=["user", "gpt"])
format_filter = st.sidebar.multiselect("Formatting Type", ["flat_text", "table", "code_block"], default=["flat_text"])

st.title("🧠 ThreadParser Visual Viewer")

# Message Timeline Display
st.subheader("📜 Message Timeline")

for entry in thread_index:
    if entry['Role'] in role_filter and entry['FormattingType'] in format_filter:
        msg_id = entry['MsgID']
        if msg_id in msg_blocks:
            st.markdown(f"### {msg_id} – {entry['Role'].upper()}")
            with st.expander("Show Message"):
                st.markdown(msg_blocks[msg_id], unsafe_allow_html=True)
                st.download_button(
                    label="📥 Download as .md",
                    data=msg_blocks[msg_id],
                    file_name=f"{msg_id}.md",
                    mime="text/markdown"
                )

st.markdown("---")
st.success("Viewer loaded: full Markdown rendering + message filters + per-message export")