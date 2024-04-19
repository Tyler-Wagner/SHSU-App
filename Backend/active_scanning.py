import requests
from dotenv import load_dotenv

env_file = 'api.env'

load_dotenv(dotenv_path=env_file)
class AbuseIPDBClient:
    def __init__(self):
        self.api_key = '018a5ab5061a29b7e85c01b75511caf5e5070768f0b89442b576000838611e3e0e83b78605bdeabd'
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
            # print(f"Error querying IP: {response.status_code}")
            return None