import streamlit as st

from Engine import TranslatorEngine

st.set_page_config(page_title="Streamlit App", page_icon="🪢")

st.title('App Translator')

if 'translator' not in st.session_state:
    st.session_state['translator'] = TranslatorEngine()

translaterEngine: TranslatorEngine = st.session_state['translator']

text = st.text_area("Enter text to translate", '')
col1, col2 = st.columns(2)
fromLanguage = col1.selectbox('From Language',
                              ['en', 'hi', 'bn', 'gu', 'mr', 'ta', 'te', 'kn', 'ml', 'ur'])

toLanguage = col2.selectbox('To Language', ['en', 'hi', 'bn', 'gu', 'mr', 'ta', 'te', 'kn', 'ml', 'ur'])

if st.button("Translate", use_container_width=True, type='primary'):
    with st.spinner("Translating..."):
        st.write(translaterEngine.translate(from_lang=fromLanguage, to_lang=toLanguage, text=text))
