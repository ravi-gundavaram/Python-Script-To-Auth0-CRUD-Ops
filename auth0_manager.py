import os
import sys
import requests
import json
from urllib.parse import quote

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
        data = {}
        if email:
            data['email'] = email
        if password:
            data['password'] = password
        response = requests.patch(url, headers=self.headers, data=json.dumps(data))
        return response.json()

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
