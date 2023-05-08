import os
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

if __name__=="__main__":
    print("Hello , and welcome to robo speaker !!!!")
    x = input("Enter what you want to speak: ")
    # command = f'echo "{x}"'
    while(True):
      engine.say(x)
      engine.runAndWait()
    # os.system(command)
    
