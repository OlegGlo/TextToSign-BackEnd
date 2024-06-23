import os

from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv('./env/secrets.env')

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', None)

def get_lyrics_from_gpt(song_name: str, artist_name: str):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    prompt = f"Give me the full complete whole lyrics of the song {song_name} \
    By {artist_name} \
    Please only return the lyrics and nothing else. \
    Do not include the song title or any other text. \
    Do not even say 'Sure here are the lyrics...' \
    Do not include any other text in the response such as (chorus, verse, etc.)."
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
        # stream=True
    )

    print(chat_completion.choices[0].message.content)
    return(chat_completion.choices[0].message.content)