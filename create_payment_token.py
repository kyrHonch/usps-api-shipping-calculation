import requests
from dotenv import load_dotenv
from create_oauth_token import get_oauth_token


# https://developer.usps.com/api/83

def get_payment_token():
    oauth_token = get_oauth_token()
    url = "https://api.usps.com/payments/v3/payment-authorization"
    headers = {
        "Content-Type": "application/json",
        "X-Payment-Authorization-Token": f"Bearer {oauth_token}"
    }
    payload = {
        # "roles": [
        #     {
        #         "roleName": "SHIPPER",
        #         "CRID": "12345678",
        #         "MID": "12345678",
        #         "manifestMID": "12345678",
        #         "accountType": "EPS",
        #         "accountNumber": "string",
        #         "permitNumber": "string",
        #         "permitZIP": "12345"
        #     }
        # ]
    }
    result = requests.post(url, headers=headers, json=payload)
    print(result.status_code)
