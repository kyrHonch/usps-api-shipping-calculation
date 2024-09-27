import requests
import os
from dotenv import load_dotenv


# https://developer.usps.com/api/81

def get_oauth_token():
    load_dotenv()
    client_secret = os.getenv("CLIENT_SECRET")
    client_id = os.getenv("CLIENT_ID")
    url = "https://api.usps.com/oauth2/v3/token"
    headers = {
        "Content-Type": "application/json",

    }
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "prices payments addresses"
    }
    result = requests.post(url, json=payload, headers=headers)

    json_result = result.json()
    return json_result["access_token"]
