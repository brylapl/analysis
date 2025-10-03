import streamlit as st

# Ustawienia strony
st.set_page_config(page_title="Match Preview", layout="wide")

# Wczytaj plik HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Renderuj HTML
st.components.v1.html(html_content, height=2000, scrolling=True)
