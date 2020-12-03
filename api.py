from uk_covid19 import Cov19API
import requests

england_only = [
    'areaType=nation',
    'areaName=England'
]

new_cases = {
        "newCasesByPublishDate": "newCasesByPublishDate",

}

api = Cov19API(filters=england_only, structure=new_cases)

json_data = api.get_json(as_string=True)
print("JSON:", json_data)

def newest_cases():
    updated = json_data['newCasesByPublishDate']
    print(updated)

print(new_cases())

{
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

