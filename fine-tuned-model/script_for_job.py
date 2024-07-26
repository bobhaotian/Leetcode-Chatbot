from openai import OpenAI
import os

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)
        
api_key = "sk-proj-uKjyAC97XmBIapJG82B0T3BlbkFJlVk68ZKEiRLjTncShWdv"
file_id = "file-ge4Hv4CwsNELyRYP961VHuZ9"
model_name = "gpt-3.5-turbo"
os.environ["OPENAI_API_KEY"] = api_key

client = OpenAI()

response = client.fine_tuning.jobs.create(
  training_file=file_id, 
  model=model_name
)


print(f"Fine-tuning job created successfully with ID: {response}")