import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("api_key"),
    base_url="https://api.groq.com/openai/v1"
)

def get_response(user_input: str) -> str:
    user_chat = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are helpful ai"},
        {"role": "user", "content": user_input}
    ]
    
    )
    response_chat = user_chat.choices[0].message.content
    return response_chat

