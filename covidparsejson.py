import json
import yaml


with open('covid_cases.json','r') as json_file:
    covidtest = json.load(json_file)
#f = open("covid_cases.json")
#covidtest= json.load(f)

print(covidtest)

print("The date recorded contains: {}".format(covidtest['dateRep']))
print("The countries and territories contains: {}".format(covidtest['countriesAndTerritories']))
print("The number of cases are: {}".format(covidtest['cases']))
print("The number of deaths are: {}".format(covidtest['deaths']))
print("\n\n---")
print(yaml.dump(covidtest))

#for x in 