import json,requests
import streamlit as st
import AudioRecorder as 'audio-recorder-polyfill'
window.MediaRecorder = AudioRecorder

if (MediaRecorder.notSupported) {
  noSupport.style.display = 'block'
  dictaphone.style.display = 'none'
}

recordButton.addEventListener('click', () => {
  #Request permissions to record audio
  navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
    recorder = new MediaRecorder(stream)
 
    #Set record to <audio> when recording will be finished
    recorder.addEventListener('data available', e => {
      audio.src = URL.createObjectURL(e.data)
    })
 
    #Start recording
    recorder.start()
  })
})
stopButton.addEventListener('click', () => {
  #Stop recording
  recorder.stop()
  #Remove “recording” icon from browser tab
  recorder.stream.getTracks().forEach(i => i.stop())
})

