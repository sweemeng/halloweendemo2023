from dotenv import load_dotenv
from os import getenv
import speech_recognition as sr


load_dotenv()


def main():
    openai_key = getenv("OPENAI_API_KEY")
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=8) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Speak anything: ")
        audio = recognizer.listen(source)

        text = recognizer.recognize_whisper_api(audio, api_key=openai_key)
        print("You said: {}".format(text))


if __name__ == '__main__':
    main()
