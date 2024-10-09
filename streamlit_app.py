# Save this as app.py
import streamlit as st

def format_url(url):
    # Remove unwanted characters
    url = url.replace('[', '').replace(']', '')
    
    # Add https:// if not present
    if not url.startswith('https://'):
        url = 'https://' + url
    
    return url

st.title("URL Formatter")

# Text area for user to paste URLs
urls_input = st.text_area("Paste your URLs here, separated by new lines:")
urls = urls_input.split("\n")

# Format URLs and display them
if st.button("Format URLs"):
    formatted_urls = [format_url(url.strip()) for url in urls if url.strip()]
    st.write("Formatted URLs:")
    for url in formatted_urls:
        st.write(url)
