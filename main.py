import json

addData = {
    'add': [],
}
removeData = {
    'remove': []
}

for i in range(1000):
    i = str(i)
    email = "13-monitor-dummy-" + i + '@gmail.com'
    add = {
        "email": email,
        "givenName":"Johny" + i,
        "familyName":"noseed" + i ,
        "dob":"1993-01-03",
        "requiresSeedPackage": True,
        "currentAddress": {
            "address": "126 Fake St",
            "city": "Denver",
            "state": "CO",
            "postalCode": 80012,
            "country": "USA",
            "current": True
        },
        "driversLicense": {
            "licenseNumber": "123456789",
            "state": "TN"
        }
    }
    remove = {
        "email": email
    }
    addData['add'].append(add)
    removeData['remove'].append(remove)

with open('add.json', 'w') as outfile:
    outfile.write(json.dumps(addData))


with open('remove.json', 'w') as outfile:
    outfile.write(json.dumps(removeData))


    