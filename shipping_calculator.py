import requests
from create_oauth_token import get_oauth_token

# https://developer.usps.com/api/73

oauth_token = get_oauth_token()
url = "https://api.usps.com/prices/v3/base-rates/search"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {oauth_token}"
}

payload = {
    "originZIPCode": "12345",
    "destinationZIPCode": "90210",
    "weight": 1,
    "length": 12,
    "width": 12,
    "height": 12,
    "mailClass": "USPS_GROUND_ADVANTAGE",
    "processingCategory": "MACHINABLE",
    "rateIndicator": "SP",
    "destinationEntryFacilityType": "NONE",
    "priceType": "RETAIL",
}

result = requests.post(url, headers=headers, json=payload)

print(result.json())
