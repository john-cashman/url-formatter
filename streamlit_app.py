import streamlit as st
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

st.title("URL Formatter V.2")

# File uploader
uploaded_file = st.file_uploader("Upload a file containing URLs (one per line):", type=["txt"])

urls = []
if uploaded_file is not None:
    urls = uploaded_file.getvalue().decode("utf-8", errors="ignore").splitlines()
    urls = [url.encode("ascii", errors="ignore").decode() for url in urls]  # Convert to plain text
else:
    # Text area for user to paste URLs
    urls_input = st.text_area("Paste your URLs here, separated by new lines:")
    urls = urls_input.split("\n")

# Format URLs and display them
if st.button("Format URLs"):
    formatted_urls = [format_url(url.strip()) for url in urls if url.strip()]
    formatted_output = "\n".join(formatted_urls)
    
    st.write("### Formatted URLs:")
    
    # Display formatted URLs in a text area for easy copying
    st.text_area("Formatted URLs:", formatted_output, height=200, key='formatted_urls')
