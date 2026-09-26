import streamlit as st

st.title("AudioSep — Text-Guided Audio Separation")

uploaded = st.file_uploader("Upload a mixed audio file", type=["wav", "mp3"])
prompt = st.text_input("Describe the sound to extract", placeholder="e.g. human speech")
