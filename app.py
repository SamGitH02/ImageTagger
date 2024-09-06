import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Set page configuration for wider layout and custom theme
st.set_page_config(layout="wide", page_title="Image Captioning and Tagging")

# Custom CSS for advanced styling
st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif;
    color: #333;
}

.title {
    text-align: center;
    font-size: 36px;
    color: #2980b9;
    margin-bottom: 20px;
}

.container {
    padding: 20px;
    border-radius: 10px;
}

.main-content {
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2); /* Subtle gradient background */
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.stButton button {
    background-color: #2980b9;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s; /* Smooth transition on hover */
}

.stButton button:hover {
    background-color: #2471a3;
}

.stExpanderHeader {
    font-weight: bold;
}

.result-card {
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.result-card .icon {
    font-size: 24px;
    margin-right: 10px;
    vertical-align: middle;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Image Captioning and Tagging</p>', unsafe_allow_html=True)

# Wrap content in containers for styling
with st.container():
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    API_KEY = "AIzaSyDi_nEIquKYwJOMsq7WjdkQZPPaC70FBxc"  # Replace with your actual key

    if uploaded_file is not None:
        if st.button('Generate Caption & Tags'):
            with st.spinner('Generating caption and tags...'):
                file_path = os.path.join("temp", uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getvalue())

                img = Image.open(file_path)
                try:
                    genai.configure(api_key=API_KEY)
                    model = genai.GenerativeModel('gemini-1.5-flash') 

                    ai_caption = model.generate_content(["Write a caption for the image in english", img])
                    ai_tags = model.generate_content(["Generate 5 hash tags for the image in a line in english", img])

                    user_caption = st.text_input("Enter your own caption (optional):")
                    user_tags = st.text_input("Enter your own tags (optional):")

                    # Display image with styling
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        st.image(img, use_column_width=True, caption="Uploaded Image")

                    with col2:
                        # AI-Generated Results (collapsible card)
                        with st.expander("AI-Generated"):
                            with st.container():
                                st.markdown(f'<div class="result-card"><span class="icon">📝</span> <b>Caption:</b> {ai_caption.text}</div>', unsafe_allow_html=True)
                                st.markdown(f'<div class="result-card"><span class="icon">#️⃣</span> <b>Tags:</b> {ai_tags.text}</div>', unsafe_allow_html=True)

                        # User Input (collapsible card)
                        if user_caption or user_tags:
                            with st.expander("Your Input"):
                                with st.container():
                                    if user_caption:
                                        st.markdown(f'<div class="result-card"><span class="icon">📝</span> <b>Caption:</b> {user_caption}</div>', unsafe_allow_html=True)
                                    if user_tags:
                                        st.markdown(f'<div class="result-card"><span class="icon">#️⃣</span> <b>Tags:</b> {user_tags}</div>', unsafe_allow_html=True)

                except Exception as e:
                    error_msg = str(e)
                    if "API_KEY_INVALID" in error_msg:
                        st.error("Invalid API Key. Please double-check your API Key.")
                    elif "Quota exceeded" in error_msg:
                        st.error("API Quota Exceeded. Please try again later or contact your API provider.")
                    else:
                        st.error(f"An error occurred: {error_msg}")

        # Add a "Clear" button
        if st.button("Clear"):
            st.experimental_rerun()  # This will reset the app