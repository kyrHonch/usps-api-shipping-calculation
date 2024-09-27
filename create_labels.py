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
        "streetAddress": "17 E. Grand Drive,  ",
        "secondaryAddress": "13E",
        "city": "Ocoee",
        "state": "FL",
        "ZIPCode": "34761",
        "firstName": "Quentin",
        "lastName": "Tarantino",
        "email": "email@email.com",
        "ignoreBadAddress": False,
        "parcelLockerDelivery": False,
        "holdForPickup": False,
    },
    "fromAddress": {
        "streetAddress": "7177 Columbia St.",
        "secondaryAddress": "G",
        "city": "Upper Marlboro",
        "state": "MD",
        "ZIPCode": "20772",
        "firstName": "Ted",
        "lastName": "Kaczynski",
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
