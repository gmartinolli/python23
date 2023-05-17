import json,requests
import streamlit as st
from audio_recorder_streamlit import audio_recorder
#APIkey = dbcc88b0c1mshcb664b65096f2fcp1238d4jsn2ca60dd6acb5
#url = 'https://rapidapi.com/developer/security/default-application_7420963' + '&appid=' + APIkey

registratore = audio_recorder()
audio_recorder = st.audio(registratore, format="audio/mp3")
if registratore:
  avvia_registrazione = st.write("avvia")
  avvia_registrazione.save("my_audio.mp3")
  
 
