import requests
from create_oauth_token import get_oauth_token

# https://developer.usps.com/api/93

oauth_token = get_oauth_token()

url = "https://api.usps.com/addresses/v3/address"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {oauth_token}",
}
query_parameters = {
    "streetAddress": "Address",
    "secondaryAddress": "Apartment Number",
    "city": "City",  # Says Optional, yet it is required
    "state": "ST"
}
result = requests.get(url, headers=headers, params=query_parameters)
data = result.json()
if result.status_code != 200:
    print(f"Error ({result.status_code}:{data['error']['message']}")
else:
    print("Address")
    for field in data['address']:
        if data['address'][field] is not None:
            print(f"{field}: {data['address'][field]}")

    print(f"Matches: {data['matches']}")
