from googletrans import Translator
import json

i = input()
trans = Translator()
result = trans.translate(i, dest='en')
print(result.text)
