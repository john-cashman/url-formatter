import streamlit as st

def format_url(url):
    # Remove leading/trailing spaces and unwanted characters
    url = url.strip().replace('[', '').replace(']', '')

    # Normalize URL for comparison (case insensitive)
    url_lower = url.lower()

    # List of prefixes to remove
    prefixes = ['http://', 'https://', 'hxxp://', 'hxxps://', 'hXXp://', 'hXXps://']

    # Remove the matching prefix if it exists
    for prefix in prefixes:
        if url_lower.startswith(prefix):
            url = url[len(prefix):]  # Remove the prefix
            break  # Stop after removing the first matching prefix

    # Ensure the URL starts with 'https://' only once
    if not url.lower().startswith('https://'):
        url = 'https://' + url.lstrip('/')

    return url

st.title("URL Fixer")

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
