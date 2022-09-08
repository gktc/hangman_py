import requests
word_api = 'https://random-word-api.herokuapp.com/word'

def getWord():
  word = requests.get(word_api).json()
  word  = word[0]
  return word
  
