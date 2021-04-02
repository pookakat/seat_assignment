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
class Plane:
    def __init__(self, flight_number, flight_departure_date_time, flight_arrival_loc, flight_departure_loc, flight_equip_type):
        self.flight_number = flight_number
        self.flight_departure_date_time = flight_departure_date_time
        self.flight_arrival_loc = flight_arrival_loc
        self.flight_departure_loc = flight_departure_loc
        self.flight_equip_type = flight_equip_type

class Row:
    def __init__(self, row_number, row_class, row_seats):
        self.row_number = row_nuumber
        self.row_class = row_class
        self.row_seats = row_seats

class Seats:
    def __init__(self, seat_id, seat_price, seat_availability, seat_type):
        self.seat_id = seat_id
        self.seat_price = seat_price
        self.seat_availability = seat_availability
        self.seat_type = seat_type

for child in root[0][0][1][0][0]:
    print(child.tag, child.attrib)
    #flight_information[k] = child.attrib[k] for k in child attrib
    #print([(k, child.attrib[k]) for k in child.attrib])
    #for key, value in child.attrib():
    #    flight_information[key] = value

#print(flight_information)
#This is the basic layout for the command to get the JSON file. For now, we're working on how to get it in the first place. 
#json_file_information = json.dumps(flight_information)
#https://www.w3schools.com/python/python_json.asp describes how to use the built in json function to convert python objects to a json file