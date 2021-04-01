import sys
import xml.etree.ElementTree as ET
import json

xml_doc = str(sys.argv[1])
tree = ET.parse(xml_doc)
root = tree.getroot()
flight_information = {}


for child in root[0][0][1][0][0]:
    print(child.tag, child.attrib)
    #flight_information[k] = child.attrib[k] for k in child attrib
    #print([(k, child.attrib[k]) for k in child.attrib])
    #for key, value in child.attrib():
    #    flight_information[key] = value

#print(flight_information)
json_file_information = json.dumps(flight_information)
#https://www.w3schools.com/python/python_json.asp describes how to use the built in json function to convert python objects to a json file