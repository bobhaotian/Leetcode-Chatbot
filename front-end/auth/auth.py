from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Load users from CSV
def load_users():
    users = {}
    with open('Login.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            username = row[0]  # Assume the first column is the username
            password = row[1]  # Assume the second column is the password
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

if __name__ == '__main__':
    app.run(debug=True)
