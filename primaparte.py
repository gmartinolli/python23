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

translator = Translator()

word = st.text_input("Please, insert a word/sentence")



if (word and lang_code):
  translate = translator.translate(word, dest=lang_code)
  tts1=gTTS(text=translate.text, lang=lang_code)
  tts1.save('file.mp3')

  
    
    
if welcome == 'traduci parola':
    translator = Translator()
   
    word = st.text_input("cosa vuoi tradurre?")
    
    #word = st.text_input('Type some text:')
    lang_code = st.text_input("scegli una lingua: en = inglese, de = tedesco")
    if (word and lang_code):
      translation = translator.translate(word, dest=lang_code)
      tts1=gTTS(text=translation.text, lang=language_code)
      tts1.save('file.mp3')
      audio_file = open("file.mp3", "rb")
      st.audio(data=audio_file, format="audio/mp3", start_time=0)    
      st.write = tts1
#else:
   # st.write("scegliere un\'azione")
                   
           
                
