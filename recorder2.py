import streamlit as st
from audiorecorder import audiorecorder
import base64
import http.client

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())
    
    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())

  
    enc = base64.b64encode(open("audio.mp3", "rb").read())
    st.write(enc)


conn = http.client.HTTPSConnection("pronunciation-assessment1.p.rapidapi.com")

payload =  enc

conn.request("POST", "/pronunciation", payload, headers)

res = conn.getresponse()
data = res.read()
