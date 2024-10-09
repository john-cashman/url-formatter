import streamlit as st

def format_url(url):
    # Remove leading/trailing spaces
    url = url.strip()
    
    # Remove unwanted characters first
    url = url.replace('[', '').replace(']', '')
    
    # Remove hxxp:// from the beginning
    if url.startswith('hxxp://'):
        url = url[7:]  # Remove the first 7 characters
    # Remove hxxps:// from the beginning
    elif url.startswith('hxxps://'):
        url = url[8:]  # Remove the first 8 characters

    # Replace hxxps:// with https://
    url = url.replace('hxxps://', 'https://')

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
    
    # Display formatted URLs in a text area for easy copying
    st.text_area("Here are your formatted URLs:", formatted_output, height=200, key='formatted_urls')

    # Instruction for users
    st.write("You can copy the formatted URLs above by selecting them and pressing Ctrl+C (or Cmd+C on Mac).")

    # Instruction for users
    st.write("You can copy the formatted URLs above by selecting them and pressing Cmd+C on Mac. The copy to clipboard button did not work 🥲")
