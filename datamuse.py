import json,requests
from pprint import pprint
keyword=input('Please, insert a keyword ')
url= 'https://api.datamuse.com/words?sl=' + keyword
response = requests.get(url)  
dataFromDatamuse = json.loads(response.text)
st.write(dataFromDatamuse)
