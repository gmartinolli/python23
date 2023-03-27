import json, requests 
import streamlit as st
#to run on github only
#switch print to st.write

APIkey = '07d40238fc934d79750916acad944490'
location = st.text('Insert a location', )

if location:
  url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid='+ APIkey + '&units=metric'
  #url = 'http://api.openweathermap.org/data/2.5/weather?q=Bolzano&appid=07d40238fc934d79750916acad944490&units=metric'

response = requests.get(url)

weatherData = json.loads(response.text)

st.header("Weather forecast")
st.write("Temperature:", weatherData['main']['temp_max'], "°C")
