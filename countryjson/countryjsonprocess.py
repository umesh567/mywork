import json
with open("country.json")as f:
    data=json.load(f)
    print(data)