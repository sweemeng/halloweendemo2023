import os

import speech_recognition as sr
from websockets.sync.client import connect
import pyttsx3

from dotenv import load_dotenv

load_dotenv()


def main():
    recognizer = sr.Recognizer()
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 200)

    url = os.getenv("WEBSOCKET_BOT_URL")
    speaker.say("Welcome to our cake shop how may i help you?")
    speaker.runAndWait()
    with connect(url) as websocket, sr.Microphone() as source:
        while True:
            response = websocket.recv()
            print(response)
            if response == "STOP":
                break
            if response != "READY":
                speaker.say(response)
            speaker.runAndWait()
            recognizer.adjust_for_ambient_noise(source)
            print("Speak anything: ")
            audio = recognizer.listen(source)

            text = recognizer.recognize_whisper_api(audio, api_key=os.getenv("OPENAI_API_KEY"))
            print("You said: {}".format(text))
            websocket.send(text)


if __name__ == '__main__':
    main()
