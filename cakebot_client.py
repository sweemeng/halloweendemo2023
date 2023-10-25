import os

import speech_recognition as sr
from websockets.sync.client import connect
from dotenv import load_dotenv

load_dotenv()


def main():
    recognizer = sr.Recognizer()
    url = os.getenv("WEBSOCKET_BOT_URL")
    with connect(url) as websocket:
        with sr.Microphone(device_index=8) as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Speak anything: ")
            audio = recognizer.listen(source)

            text = recognizer.recognize_whisper_api(audio, api_key=os.getenv("OPENAI_API_KEY"))
            print("You said: {}".format(text))
            websocket.send(text)
            response = websocket.recv()
            print(response)


if __name__ == '__main__':
    main()
