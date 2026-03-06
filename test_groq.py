import os
from groq import Groq

# Set the API key
os.environ["GROQ_API_KEY"] = "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"

try:
    client = Groq()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Hello, are you working?",
            }
        ],
        model="llama3-8b-8192",
    )
    print("API is working. Response:", chat_completion.choices[0].message.content)
except Exception as e:
    print("API Error:", str(e))
