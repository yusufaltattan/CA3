from uk_covid19 import Cov19API
import requests

england_only = [
    'areaType=nation',
    'areaName=England'
]

def newest_cases():
    '''Function for cases per day in England'''
    new_cases = {"newCasesByPublishDate": "newCasesByPublishDate",}
    api = Cov19API(filters=england_only, structure=new_cases)
    json_data = api.get_json(as_string=True)
    latest_data = json_data[34:39]
    return latest_data

def total_cases():
    '''Function for total cases in England'''
    total_cases = {"cumCasesByPublishDate": "cumCasesByPublishDate",}
    api = Cov19API(filters=england_only, structure=total_cases)
    json_data = api.get_json(as_string=True)
    latest_data = json_data[34:41]
    return latest_data

def newest_deaths():
    '''Function for deaths per day in England'''
    new_deaths = {"newDeathsByDeathDate": "newDeathsByDeathDate",}
    api = Cov19API(filters=england_only, structure=new_deaths)
    json_data = api.get_json(as_string=True)
    latest_data = json_data[33:36]
    return latest_data

def total_deaths():
    '''Function for total deaths in England'''
    tot_deaths = {"cumDeathsByDeathDate": "cumDeathsByDeathDate"}
    api = Cov19API(filters=england_only, structure=tot_deaths)
    json_data = api.get_json(as_string=True)
    latest_data = json_data[33:38]
    return latest_data

def covid():
    case_per_day = newest_cases()
    total_cases_covid = total_cases()
    death_per_day = newest_deaths()
    total_deaths_covid = total_deaths()
    description = "There have been " + case_per_day + " cases today, raising the total cases to " + total_cases_covid + ". There have been " + death_per_day+ " deaths per day from COVID-19, raising the total to " + total_deaths_covid+ " deaths."
    covid_dict =  {"title" :"Corona News", "content": description}
    return covid_dict

print(covid())

