import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="المختبر الافتراضي للمغناطيسية",
    page_icon="🧲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    [data-testid="stDecoration"] {display: none;}
    .block-container {padding: 0 !important; margin: 0 !important;}
    header {display: none !important;}
</style>
""", unsafe_allow_html=True)

with open("magnetism_lab.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=850, scrolling=True)