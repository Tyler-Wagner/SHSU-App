# This entire file is used for demonstration purposes only.
# We will need ot look into an API key
# I will also store our API key in an .env file so no one
# other than us can access it
# this code isn't going to production
# so we don't need a key

import requests
import os
from dotenv import load_dotenv

env_file = 'api.env'

load_dotenv(dotenv_path=env_file)
class AbuseIPDBClient:
    def __init__(self, api_key):
        self.api_key = os.getenv('API_KEY')
        self.base_url = "https://api.abuseipdb.com/api/v2"

    def query_ip(self, ip_address):
        headers = {
            "Key": self.api_key,
            "Accept": "application/json"
        }

        endpoint = f"/check?ipAddress={ip_address}"
        url = self.base_url + endpoint
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error querying IP: {response.status_code}")
            return None

