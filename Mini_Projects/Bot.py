import pyttsx3
import datetime
import speech_recognition as myvc
import wikipedia

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
		speak("Good morning !")

	elif hour>=12 and hour<=18:
		print(hour)
		speak("Good Afternoon !")
	
	elif hour>=19:
		print(hour)
		speak("Good evening !")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = myvc.Recognizer()
    with myvc.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query




if __name__ == "__main__":
    wishme()
    speak("Hi handsome i am friday your personal assistent")
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


            




    
       