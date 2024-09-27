import requests
from create_payment_token import get_payment_token

# https://developer.usps.com/api/71

payment_token = get_payment_token()

url = "https://api.usps.com/labels/v3/label"

headers = {
    "Content-Type": "application/json",
    "X-Payment-Authorization-Token": payment_token
}

payload = {
    "imageInfo": {
        "imageType": "PDF",
        "labelType": "4X5LABEL",
        "shipInfo": True,
        "receiptOption": "SAME_PAGE",
        "suppressPostage": True,
        "suppressMailDate": True,
        "returnLabel": False,
        "packageNumber": 1,
        "totalPackages": 1
    },
    "toAddress": {
        "streetAddress": "string",
        "secondaryAddress": "string",
        "city": "string",
        "state": "st",
        "ZIPCode": "string",
        "ZIPPlus4": "string",
        "urbanization": "string",
        "firstName": "string",
        "lastName": "string",
        "firm": "string",
        "phone": "string",
        "email": "email@email.com",
        "ignoreBadAddress": False,
        "parcelLockerDelivery": False,
        "holdForPickup": False,
    },
    "fromAddress": {
        "streetAddress": "string",
        "secondaryAddress": "string",
        "city": "string",
        "state": "st",
        "ZIPCode": "string",
        "ZIPPlus4": "string",
        "urbanization": "string",
        "firstName": "string",
        "lastName": "string",
        "firm": "string",
        "phone": "string",
        "email": "user@example.com",
        "ignoreBadAddress": False
    },
    "packageDescription": {
        "weight": 1,
        "length": 12,
        "height": 12,
        "width": 12,
        "mailClass": "USPS_GROUND_ADVANTAGE",
        "processingCategory": "MACHINABLE",
        "destinationEntryFacilityType": "NONE",
        "mailingDate": "2019-08-24",
        "rateIndicator": "SP"
    },
}
