import streamlit as st
from googletrans import Translator, LANGUAGES

# Translator object initialize karein
translator = Translator()

# App Title
st.set_page_config(page_title="CodeAlpha Language Translator", page_icon="🌐")
st.title("🌐 Language Translation Tool")
st.subheader("CodeAlpha Internship - Task 1")

# User Input
text_to_translate = st.text_area("Type the text here you can translate:", placeholder="Type here...")

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Original Language:", options=list(LANGUAGES.values()), index=list(LANGUAGES.values()).index('english'))

with col2:
    target_lang = st.selectbox("Target Language:", options=list(LANGUAGES.values()), index=list(LANGUAGES.values()).index('urdu'))

# Function to get key from language name
def get_key(val):
    for key, value in LANGUAGES.items():
        if val == value:
            return key
    return "en"

# Translation Button
if st.button("Translate Now"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text first!")
    else:
        try:
            src_key = get_key(source_lang)
            dest_key = get_key(target_lang)
            
            translation = translator.translate(text_to_translate, src=src_key, dest=dest_key)
            
            st.success("### Translated Text:")
            st.write(translation.text)
            
            # Optional: Copy button feature (text-to-speech ke liye space)
            st.info(f"Translated from {source_lang} to {target_lang}")
            
        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Developed by Mahnoor Fatima | CodeAlpha Intern")
