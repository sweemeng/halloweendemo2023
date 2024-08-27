import os
from textwrap import dedent

from dotenv import load_dotenv
import openai
load_dotenv()


openai.api_key = openai_key = os.getenv("OPENAI_KEY")
MODEL = "gpt-4o-mini"


def main():
    system_prompt = "You're a scary assistant, you tell scary story to scare people for entertainment. "
    user_prompt = "Please tell me a scary story about a pontianak"
    print(os.getenv("OPENAI_KEY"))
    client = openai.OpenAI(
        api_key=os.getenv("OPENAI_KEY")
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0
    )
    print(response.choices[0].message.content)


if __name__ == '__main__':
    main()
