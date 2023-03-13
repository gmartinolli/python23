import streamlit as st
#st.text("hello world")
#st.header("hello world")  
#st.text("from Brixen") 
title = st.text_input('Please insert a movie title', '')
st.write('The current movie title is', title)
