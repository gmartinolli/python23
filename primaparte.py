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
    st.text_input("scrivi")
else:
    st.write("scegliere un\'azione")
                   
           
                
