import pyttsx3
import datetime

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def wishme():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		print(hour)
		speak("Good morning sir!")

	elif hour>=12 and hour<=18:
		print(hour)
		speak("Good Afternoon sir!")
	
	elif hour>=19:
		print(hour)
		speak("Good evening sir!")

if __name__ == "__main__":
  wishme()
  speak("Hello handsome, i'm FRIDAY !,How can i help you!")
	 