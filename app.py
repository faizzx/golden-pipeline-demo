from flask import Flask, request
import os

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded API Key (SAST scanners should catch this)
# API_KEY = "12345-abcde-secret-key-do-not-share"

API_KEY = os.getenv('API_KEY', 'default-key-for-dev')


@app.route('/')
def home():
    return "Welcome to the Golden Pipeline Demo!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    # VULNERABILITY 2: This looks like a sensitive log (SAST might flag logging user input)
    print(f"User trying to login: {username}")
    return "Login attempt recorded"

if __name__ == '__main__':
    # VULNERABILITY 3: Running with debug=True in production is unsafe
    app.run(host='0.0.0.0', port=5000, debug=True)