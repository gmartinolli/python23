import streamlit as st
import json,requests
from audiorecorder import audiorecorder
import base64
#import http.client
#url = "https://pronunciation-assessment1.p.rapidapi.com/pronunciation"
st.title("Controllo della pronuncia")
st.text_input("cosa vuoi dire?")
text = st.text_input
audio = audiorecorder("Registra", "in registrazione...")
if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())
    
    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())

  
    enc = base64.b64encode(open("audio.mp3", "rb").read())
    st.write(enc)
  


    #url = "https://pronunciation-assessment1.p.rapidapi.com/pronunciation"

   # payload = {
	#"audio_base64": enc,
	#"audio_format": "wav",
	#"text": text
	#}
  #  headers = {
	#"content-type": "application/json",
	#"X-RapidAPI-Key": "dbcc88b0c1mshcb664b65096f2fcp1238d4jsn2ca60dd6acb5",
	#"X-RapidAPI-Host": "pronunciation-assessment1.p.rapidapi.com"
      #}

   # response = requests.post(url, json=payload, headers=headers)
   # st.write(response)

#print(response.json())

    #st.write(response)
