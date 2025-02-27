import streamlit as st

def format_url(url):
    # Remove leading/trailing spaces
    url = url.strip()
    
    # Remove unwanted characters like '[' and ']'
    url = url.replace('[', '').replace(']', '')
    
    # List of prefixes to remove
    prefixes = ['http://', 'https://', 'hxxp://', 'hxxps://', 'hXXp://', 'hXXps://']
    
    # Remove the matching prefix if it exists
    for prefix in prefixes:
        if url.lower().startswith(prefix):
            url = url[len(prefix):]  # Remove the prefix
    
    # Ensure the URL starts with 'https://'
    if not url.lower().startswith('https://'):
        url = 'https://' + url
    
    return url

st.title("URL Formatter")

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
