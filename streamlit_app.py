import streamlit as st
import pandas as pd
import re

def format_url(url):
    # Remove hidden Unicode characters (e.g., zero-width spaces)
    url = url.encode("ascii", "ignore").decode()

    # Remove leading/trailing spaces and unwanted characters
    url = url.strip().replace('[', '').replace(']', '')

    # Remove all occurrences of 'http://' and 'https://' at the beginning
    url = re.sub(r'^(https?://)+', '', url, flags=re.IGNORECASE)

    # Ensure the URL starts with 'https://'
    url = 'https://' + url.lstrip('/')

    return url

st.title("URL Formatter")

# Multiple file uploader
uploaded_files = st.file_uploader("Upload CSV files containing URLs:", type=["csv"], accept_multiple_files=True)

urls = []
if uploaded_files:
    for uploaded_file in uploaded_files:
        # Read only the first column of each CSV
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
    
    # Display formatted URLs in a text area
    st.text_area("Formatted URLs:", formatted_output, height=200, key='formatted_urls')

    # JavaScript-based copy button
    st.markdown(
        f"""
        <button onclick="navigator.clipboard.writeText(document.getElementById('formatted_urls').value); alert('Copied!');">
            Copy to Clipboard
        </button>
        """,
        unsafe_allow_html=True
    )
