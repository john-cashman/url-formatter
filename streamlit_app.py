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

# Function to display the confetti effect
def confetti():
    st.components.v1.html("""
        <script src="https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.4.0/confetti.browser.min.js"></script>
        <script>
            const launchConfetti = () => {
                var end = Date.now() + (5 * 1000);
                var colors = ['#bb0000', '#ffffff', '#00bb00', '#0000bb'];
                (function frame() {
                    confetti({
                        particleCount: 5,
                        angle: 60,
                        spread: 55,
                        origin: { x: 0, y: 1 },
                        colors: colors
                    });
                    confetti({
                        particleCount: 5,
                        angle: 120,
                        spread: 55,
                        origin: { x: 1, y: 1 },
                        colors: colors
                    });
                    if (Date.now() < end) {
                        requestAnimationFrame(frame);
                    }
                })();
            };
            launchConfetti();
        </script>
    """, height=0)

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

    # Display confetti effect
    confetti()

    # Instruction for users
    st.write("You can copy the formatted URLs above by selecting them and pressing Ctrl+C (or Cmd+C on Mac).")
