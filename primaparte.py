import st as streamlit
from gtts import gTTS
from googletrans import Translator

st.header("Lavoriamo sulla pronuncia inglese")
st.write("App per lavorare sulla tua pronuncia inglese.")    
welcome = st.radio("Scegli un\'azione",('scrivi una parola','registra parola', 'traduci parola')
                   if welcome == 'scrivi una parola'
                      st.write("scrivi")
                   if welcome == 'registra parola'
                       st.write("registra")
                   if welcome == 'traduci parola'
                       st.write("traduci")
                   else:
                       st.write("scegliere un\'azione")
                   
           
                
