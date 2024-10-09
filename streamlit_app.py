# Save this as app.py
import streamlit as st

def format_url(url):
    url = url.strip()
    url = url.replace('xx', 'tt')
    url = url.replace('[', '').replace(']', '')
    if not url.startswith('https://'):
        url = 'https://' + url
    return url

st.title("URL Formatter")

urls_input = st.text_area("Paste your URLs here, separated by new lines:")
urls = urls_input.split("\n")

if st.button("Format URLs"):
    formatted_urls = [format_url(url.strip()) for url in urls if url.strip()]
    formatted_output = "\n".join(formatted_urls)
    
    st.write("Formatted URLs:")
    st.text_area("Here are your formatted URLs:", formatted_output, height=200)

    # Adding a copy button using JavaScript
    st.markdown(
        f"""
        <button onclick="navigator.clipboard.writeText(`{formatted_output}`)">
            Copy to Clipboard
        </button>
        """, 
        unsafe_allow_html=True
    )
