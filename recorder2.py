import streamlit as st
import json,requests
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
    #st.write(enc)
    headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': "dbcc88b0c1mshcb664b65096f2fcp1238d4jsn2ca60dd6acb5",
    'X-RapidAPI-Host': "pronunciation-assessment1.p.rapidapi.com"

    conn = http.client.HTTPSConnection("pronunciation-assessment1.p.rapidapi.com")

    payload = "{\r
    \"audio_base64\": enc
    ==\",\r
    \"audio_format\": \"wav\",\r
    \"text\": \"hello"\r
    }"


    conn.request("POST", "/pronunciation", payload, headers)

    res = conn.getresponse()
    data = res.read()
