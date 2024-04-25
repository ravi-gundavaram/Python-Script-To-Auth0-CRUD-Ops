import os
import sys
import requests
import json
from urllib.parse import quote
from flask import Flask, request, jsonify

app = Flask(__name__)

class Auth0Manager:
    def __init__(self, domain, token):
        self.base_url = f'https://{domain}/api/v2'
        self.headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    def create_user(self, email, password):
        url = f"{self.base_url}/users"
        data = {
            "user_metadata": {},
            "connection": "Username-Password-Authentication",
            "email": email,
            "password": password,
            "email_verified": False
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        return response.json()

    def get_user(self, user_id):
        url = f"{self.base_url}/users/{quote(user_id)}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{quote(user_id)}"
        response = requests.delete(url, headers=self.headers)
        return response.status_code

    def update_user(self, user_id, email=None, password=None):
        url = f"{self.base_url}/users/{quote(user_id)}"
        if email and password:
            print("Updating email and password separately.")
        # Update email first
            email_data = {'email': email}
            response = requests.patch(url, headers=self.headers, data=json.dumps(email_data))
            if response.status_code == 200:
                print("Email updated successfully.")
            # Now update password
                password_data = {'password': password}
                response = requests.patch(url, headers=self.headers, data=json.dumps(password_data))
                if response.status_code == 200:
                    print("Password updated successfully.")
                else:
                    print(f"Failed to update password: {response.json()}")
            else:
                print(f"Failed to update email: {response.json()}")
            return response.json()
        elif email:
            data = {'email': email}
        elif password:
            data = {'password': password}
        else:
            return {"error": "No data provided for update"}

        response = requests.patch(url, headers=self.headers, data=json.dumps(data))
        return response.json()

@app.route('/')
def home():
    return "Welcome to Auth0 Manager API! Use the documented endpoints to interact with the API."

# Flask routes for API access
@app.route('/create_user', methods=['POST'])
def api_create_user():
    data = request.json
    return jsonify(manager.create_user(data['email'], data['password']))

@app.route('/get_user/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(manager.get_user(user_id))

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    return jsonify(manager.delete_user(user_id))

@app.route('/update_user/<user_id>', methods=['PUT'])
def api_update_user(user_id):
    data = request.json
    return jsonify(manager.update_user(user_id, data.get('email'), data.get('password')))

if __name__ == '__main__':
    domain = os.getenv('AUTH0_DOMAIN')
    token = os.getenv('AUTH0_TOKEN')
    print(f"Domain: {domain}, Token: {token}")
    manager = Auth0Manager(domain, token)
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == 'create' and len(sys.argv) == 4:
            print(manager.create_user(sys.argv[2], sys.argv[3]))
        elif action == 'get' and len(sys.argv) == 3:
            print(manager.get_user(sys.argv[2]))
        elif action == 'delete' and len(sys.argv) == 3:
            print(manager.delete_user(sys.argv[2]))
        elif action == 'update' and len(sys.argv) == 5:
            print(manager.update_user(sys.argv[2], sys.argv[3], sys.argv[4]))
        else:
            print("Invalid arguments")
    else:
        app.run(host='0.0.0.0', port=5001)