import streamlit as st
import pandas as pd
import re
from streamlit_copy_to_clipboard import copy_to_clipboard

def format_url(url):
    """Formats a URL by removing unwanted characters and ensuring it starts with https://."""
    url = url.encode("ascii", "ignore").decode()
    url = url.strip().replace('[', '').replace(']', '')
    url = re.sub(r'^(https?://)+', '', url, flags=re.IGNORECASE)
    url = 'https://' + url.lstrip('/')
    return url

st.title("URL Formatter")

# Multiple file uploader
uploaded_files = st.file_uploader("Upload CSV files containing URLs:", type=["csv"], accept_multiple_files=True)

urls = []
if uploaded_files:
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file, encoding='utf-8', dtype=str, usecols=[0])
        file_urls = df.iloc[:, 0].dropna().astype(str).tolist()
        urls.extend(file_urls)

# Manual text input
urls_input = st.text_area("Or paste URLs here, separated by new lines:")
if urls_input.strip():
    urls.extend(urls_input.split("\n"))

# Format URLs and display them
if st.button("Format URLs"):
    formatted_urls = [format_url(url.strip()) for url in urls if url.strip()]
    formatted_output = "\n".join(formatted_urls)

    st.write("### Formatted URLs:")
    st.text_area("Formatted URLs:", formatted_output, height=200, key='formatted_urls')

    # Copy to clipboard functionality
    copy_to_clipboard(formatted_output)
