import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.setProperty('voice', voices[12].id)
engine.say("Today is a thursday")
engine.runAndWait()
