from googletrans import Translator
translator = Translator()
while True:
  word = input("Write a word: ")
  if word == "quit":
    print('tschuuus!')
    break
  else:
    target_language = input("Choose a language: ")
    transToGerman = translator.translate (word, dest=target_language)
    print(transToGerman.text) 
