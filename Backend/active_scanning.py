# This entire file is used for demonstration purposes only.
# I really hope this works for us, cannot confirm nor deny
# if it will or not. Just a serious hope it does cause I 
# cant really test it

import requests
import os
from dotenv import load_dotenv

env_file = 'api.env'

load_dotenv(dotenv_path=env_file)
class AbuseIPDBClient:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.base_url = "https://api.abuseipdb.com/api/v2"

    def query_ip(self, ip_address):
        api_couter = 1000
        headers = {
            "Key": self.api_key,
            "Accept": "application/json"
        }

        endpoint = f"/check?ipAddress={ip_address}"
        url = self.base_url + endpoint
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            #subtract the amount of api tokens we have left
            api_couter = api_couter - 1
            return response.json(), api_couter
        else:
            print(f"Error querying IP: {response.status_code}")
            return None

