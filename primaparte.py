from gtts import gTTS
from googletrans import Translator

import streamlit as st

st.header("Lavoriamo sulla pronuncia inglese")
st.write("App per lavorare sulla tua pronuncia inglese. Per iniziare scegli quale azione vuoi fare:") 

welcome = st.radio(
  "Scegli un\'azione",
  ('scrivi una parola','registra parola', 'traduci parola'))
if welcome == 'scrivi una parola':
    st.text_input("scrivi")
    
if welcome == 'registra parola':
    st.write("registra")
    
if welcome == 'traduci parola':
    word = st.text_input("scrivi")
    translator = Translator()
    #word = st.text_input('Type some text:')
    language = st.text_input('scegli lingua')
    if language:
      translation = translator.translate(word,dest=language)
    
      tts1=gTTS(word=translation.text, lang=language)
      st.write(tts1)
#else:
   # st.write("scegliere un\'azione")
                   
           
                
