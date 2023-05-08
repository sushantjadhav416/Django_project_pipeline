import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

city = input("Enter the city:")

url = f"http://api.weatherapi.com/v1/current.json?key=ef1b857b521d4ffeb3371740230705&q={city}"

r = requests.get(url)

wth = json.loads(r.text)
d = wth["current"]["temp_c"]
print(f"The current wether in {city} is {d} degree")
engine.say(f"The current wether in {city} is {d} degree")
engine.runAndWait()



