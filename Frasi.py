import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "API-KEY"
print("testo:")
testo=input()
response = openai.Completion.create(
        model="text-davinci-003",
        prompt=testo,
        temperature=0,
        max_tokens=2000

)
print(response["choices"][0]["text"])
