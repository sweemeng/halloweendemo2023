import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.say("Today is a friday")
engine.runAndWait()
