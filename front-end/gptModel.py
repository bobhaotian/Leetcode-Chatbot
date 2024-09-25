from flask import Flask, request, jsonify
import openai
import json
import os
from flask_cors import CORS
import csv

#set openai key
api_key = "sk-proj-uKjyAC97XmBIapJG82B0T3BlbkFJlVk68ZKEiRLjTncShWdv"
#os.environ["OPENAI_API_KEY"] = api_key

client = openai.OpenAI(api_key="sk-proj-uKjyAC97XmBIapJG82B0T3BlbkFJlVk68ZKEiRLjTncShWdv")

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load users from CSV
def load_users():
    users = {}
    with open('./auth/Login.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            username = row[1]  # Assume the first column is the username
            password = row[2]  # Assume the second column is the password
            users[username] = password
           
    return users

users = load_users()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})


@app.route('/api/generate', methods=['POST'])
def generate_response():
    # Define the constant system message
    system_message = {"role": "system", "content": "You are a programmer who needs to answer programming questions in Python, with only the code, without any explanation"}

    # Function to get user input and create the messages list
    def create_messages(user_input):
        user_message = {"role": "user", "content": user_input}
        return [system_message, user_message]
    
    data = request.json
    user_input = data.get('prompt') #where we need the input
    messages = create_messages(user_input) #we have the whole combined message

    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::9mYhAokC",
        messages=messages,
        max_tokens=300  # Adjust as needed
    )
    content_string = response.choices[0].message.content

    # Wrap the content string in a JSON-compatible structure
    json_structure = {
        "code": content_string
    }
    # Convert the structure to a JSON string
    json_string = json.dumps(json_structure)
    # Parse the JSON string to get a JSON object
    content_json = json.loads(json_string)
    return content_json

if __name__ == '__main__':
    app.run(debug=True)


