# Save this as app.py
import streamlit as st

def format_url(url):
    # Remove leading/trailing spaces
    url = url.strip()
    
    # Replace 'xx' with 'tt'
    url = url.replace('xx', 'tt')
    
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
    formatted_output = "\n".join(formatted_urls)
    
    st.write("Formatted URLs:")
    st.text_area("Here are your formatted URLs:", formatted_output, height=200)

    # Add a copy button using HTML and JavaScript
    copy_button_html = f"""
    <button id="copy-button" onclick="navigator.clipboard.writeText(`{formatted_output}`)">Copy to Clipboard</button>
    <script>
    document.getElementById("copy-button").onclick = function() {{
        alert("Formatted URLs copied to clipboard!");
    }};
    </script>
    """

    st.markdown(copy_button_html, unsafe_allow_html=True)
