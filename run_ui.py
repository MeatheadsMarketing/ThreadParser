import streamlit as st
from tabs import tab_tiles

def run():
    st.set_page_config(page_title="ThreadParser", layout="wide")
    tab_tiles

if __name__ == '__main__':
    run()