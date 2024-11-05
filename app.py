"""
This script ensures that the environment variables XAI_API_KEY are set properly.
"""
import os
import requests
import json

# gets the API Key from environment variable XAI_API_KEY
api_key = os.getenv("XAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "messages": [
        {
            "role": "system",
            "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
        },
        {
            "role": "user",
            "content": "What is the meaning of life, the universe, and everything?"
        }
    ],
    "model": "grok-beta",
    "stream": False,
    "temperature": 0
}

response = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, data=json.dumps(data))

print(response.json()['choices'][0]['message']['content'])
