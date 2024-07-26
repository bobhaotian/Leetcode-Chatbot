from openai import OpenAI
import os
api_key = "sk-proj-uKjyAC97XmBIapJG82B0T3BlbkFJlVk68ZKEiRLjTncShWdv"
os.environ["OPENAI_API_KEY"] = api_key

client = OpenAI()

completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0125:personal::9mYhAokC",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)
print(completion.choices[0].message)

