import json,requests
import streamlit as st
#from pprint import pprint
keyword=input('Please, insert a keyword ')
option = st.selectbox("Choose one option",
                       ('similar meaning', 'sounds like', 'rhymes with')
if option == 'similar meaning':
                      key = 'rel_syn='
elif option == 'sounds like':
                      key = 'sl='
elif option == 'rhymes with':
                      key = 'rel_rhy='
else:
                      pass
                      
url= 'https://api.datamuse.com/words?'+key + keyword
response = requests.get(url)  
dataFromDatamuse = json.loads(response.text)
st.header('Datamuse')
st.write(dataFromDatamuse)
