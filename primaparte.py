import json,requests
import streamlit as st
from dictionaryio import DictionaryIO
import vlc
#from dictionaryio import DictionaryIO
from gtts import gTTS
from googletrans import Translator


st.header("Lavoriamo sulla pronuncia inglese")
#prima avevo st.text=tutto il testo in una riga
st.subheader("app per lavorare sulla tua pronuncia inglese. Per iniziare scegli quale azione vuoi fare:") 

welcome = st.radio(
  "Ciao! Scegli cosa vorresti fare:",
  ('scrivi una parola','registra parola', 'traduci parola', 'come si pronuncia?'))
if welcome == 'scrivi una parola':
    st.text_input("scrivi")
if welcome == 'come si pronuncia?':
    word = st.text_input("scrivi")
    if (word):
       dictionaryio = DictionaryIO() 
       #word.dictionaryIO()
       word.phonetics()
       st.write = word.phonetics()    
          
if welcome == 'registra parola':
    st.write("registra")

 
if welcome == 'traduci parola':
    translator = Translator()
    word = st.text_input("cosa vuoi tradurre?")
    lang_code = st.text_input("scegli una lingua: en = inglese, de = tedesco")
    if (word and lang_code):
      translate = translator.translate(word, dest=lang_code)
      tts1=gTTS(text=translate.text, lang=lang_code)
      tts1.save('file.mp3')
      audio_file = open("file.mp3", "rb")
      st.audio(data=audio_file, format="audio/mp3", start_time=0)    
      st.write = tts1
   

#word.meaning()
    
    
else:
   st.write("scegliere un\'azione")
                   
           
                
