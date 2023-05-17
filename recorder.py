import json,requests
import streamlit as st
from audio_recorder_streamlit import audio_recorder

registratore = audio_recorder()
audio_recorder = st.audio(registratore, format="audio/wav")
if registratore:
  avvia_registrazione = st.write("avvia")
  avvia_registrazione.save("my_audio.mp3")
  
 
