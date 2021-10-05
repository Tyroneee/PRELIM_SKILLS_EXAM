import xml.etree.ElementTree as ET 
import re

xml = ET.parse("covid_cases_xml.xml")
root = xml.getroot()

ns = re.match('{.*}', root.tag).group(0)
records = root.find("{}record".format(ns))
daterep = records.find("{}dateRep".format(ns))
countter = records.find("{}countriesAndTerritories".format(ns))
numbercases = records.find("{}cases".format(ns))
deaths = records.find("{}deaths".format(ns))

print("The date recorded contains: {}".format(daterep.text))
print("The countries and territories contains: {}".format(countter.text))
print("The number of cases are: {}".format(numbercases.text))
print("The number of deaths are: {}".format(deaths.text))

