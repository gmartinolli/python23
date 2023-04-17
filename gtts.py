from gtts import gTTS
from googletrans import Translator
import streamlit as st

translator = Translator()
tts1=gTTS (text='hello world')tts1.save('english_hello.mp3')
st.write('audio example')
