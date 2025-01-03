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

# Text area for user to paste URLs
urls_input = st.text_area("Paste your URLs here, separated by new lines:")
urls = urls_input.split("\n")

# Format URLs and display them
if st.button("Format URLs"):
    # Strip out empty lines and format the URLs
    formatted_urls = [format_url(url.strip()) for url in urls if url.strip()]
    formatted_output = "\n".join(formatted_urls)
    
    st.write("Formatted URLs:")
    
    # Display formatted URLs in a text area for easy copying
    st.text_area("Here are your formatted URLs:", formatted_output, height=200, key='formatted_urls')

    # Provide instructions for users
    st.write("You can copy the formatted URLs above by selecting them and pressing Cmd+C (Mac) or Ctrl+C (Windows).")
    
    # Add copy-to-clipboard functionality using a custom button (with JavaScript)
    st.markdown("""
    <script type="text/javascript">
        function copyToClipboard() {
            const formattedText = document.querySelector("#formatted_urls").value;
            navigator.clipboard.writeText(formattedText).then(function() {
                alert('URLs copied to clipboard!');
            }, function() {
                alert('Failed to copy URLs.');
            });
        }
    </script>
    <button onclick="copyToClipboard()">Copy to Clipboard</button>
    """, unsafe_allow_html=True)
