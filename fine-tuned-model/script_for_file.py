from openai import OpenAI
import os

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        output.write(content)

api_key = "sk-XPUVztCs2_ywqbgpwFqkgA"
os.environ["OPENAI_API_KEY"] = api_key

client = OpenAI()

response = client.files.create(
  file=open("data.jsonl", "rb"),
  purpose="fine-tune"
)


#file_id = response['id']
print(f"File uploaded successfully with ID: {response}")
