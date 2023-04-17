#from gtts import gTTS
from googletrans import Translator
import streamlit as st
#import IPython.display as ipd

translator = Translator()
tts1=gTTS(text='hello world')
tts1.save('english_hello.mp3')
#ipd.display(ipd.Audio('english_hello.mp3'))
st.write('english text')
