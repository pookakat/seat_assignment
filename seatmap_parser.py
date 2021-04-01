import sys
import xml.etree.ElementTree as ET
import json

xml_doc = str(sys.argv[1])
tree = ET.parse(xml_doc)
root = tree.getroot()
flight_information = {}
#These are helpful links to finish this project:
#https://docs.python.org/3/library/xml.etree.elementtree.html is my ElementTree documentation
#https://anenadic.github.io/2014-11-10-manchester/novice/python/06-cmdline-non-interactive.html is running Python from the command line
#https://www.datacamp.com/community/tutorials/dictionary-python?utm_source=adwords_ppc&utm_campaignid=1565261270&utm_adgroupid=67750485268&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=295208661514&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9009680&gclid=CjwKCAjw3pWDBhB3EiwAV1c5rCFSPniwB33l4PLFUr1_wJnwssiPVwmvpVDR_mxjAGd7P1dai_dbzRoC03sQAvD_BwE python dictionaries

for child in root[0][0][1][0][0]:
    print(child.tag, child.attrib)
    #flight_information[k] = child.attrib[k] for k in child attrib
    #print([(k, child.attrib[k]) for k in child.attrib])
    #for key, value in child.attrib():
    #    flight_information[key] = value

#print(flight_information)
json_file_information = json.dumps(flight_information)
#https://www.w3schools.com/python/python_json.asp describes how to use the built in json function to convert python objects to a json file