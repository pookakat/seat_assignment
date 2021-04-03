import sys
import xml.etree.ElementTree as ET
import json

xml_doc = str(sys.argv[1])
tree = ET.parse(xml_doc)
root = tree.getroot()
#This section is going to make some assumptions in regards to scalability. The XML documents provided either come from IATA or #Opentravel, and the biggest assumption in regards to this is that IATA follows one format consistently, and Opentravel follows the #other. 
#Here is where we'll find out which file is presented and how it will be handled.
def strip_url_from_tag(child_info):
    entire_tag = str(child_info)
    url_information, unused_portion = entire_tag.split("}")
    url_information += "}"
    return url_information

def get_location_code(location_dict):
    airport_code = str(location_dict.get('LocationCode'))
    return airport_code


def ota_flight_handling(url_information):
    for flight_departure_loc in root.iter('{}DepartureAirport'.format(url_information)):
        flight_departure_loc = get_location_code(flight_departure_loc.attrib)

    for flight_arrival_loc in root.iter('{}ArrivalAirport'.format(url_information)):
        flight_arrival_loc = get_location_code(flight_arrival_loc.attrib)

    for flight_equip_type in root.iter('{}Equipment'.format(url_information)):
        flight_equip_type = (str(flight_equip_type.attrib))

    print("Flight Arrival: " + flight_arrival_loc)
    print("Flight Departure: " + flight_departure_loc)
    print("Flight Equipment: " + flight_equip_type)

def iata_flight_handling(url_information):
    print(str(root.iter('{}Departure[Time]'.format(url_information))))

for child in root[0]:
    if 'IATA' in child.tag:
        print("IATA flight information recieved!")
        url_information = strip_url_from_tag(child.tag)
        iata_flight_handling(url_information)
    elif 'OTA' in child.tag:
        print("OpenTravel flight information received!")
        url_information = strip_url_from_tag(child.tag)
        ota_flight_handling(url_information)
    else:
        print("Invalid File Type")


#These are helpful links to finish this project:
#https://docs.python.org/3/library/xml.etree.elementtree.html is my ElementTree documentation
#https://anenadic.github.io/2014-11-10-manchester/novice/python/06-cmdline-non-interactive.html is running Python from the command line
#https://www.datacamp.com/community/tutorials/dictionary-python?utm_source=adwords_ppc&utm_campaignid=1565261270&utm_adgroupid=67750485268&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=295208661514&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9009680&gclid=CjwKCAjw3pWDBhB3EiwAV1c5rCFSPniwB33l4PLFUr1_wJnwssiPVwmvpVDR_mxjAGd7P1dai_dbzRoC03sQAvD_BwE python dictionaries
class Plane:
    def __init__(self, flight_departure_date_time, flight_arrival_loc, flight_departure_loc, flight_equip_type):
        self.flight_departure_date_time = flight_departure_date_time
        self.flight_arrival_loc = flight_arrival_loc
        self.flight_departure_loc = flight_departure_loc
        self.flight_equip_type = flight_equip_type

class Row:
    def __init__(self, row_class, row_seats):
        self.row_class = row_class
        self.row_seats = row_seats

class Seats:
    def __init__(self, seat_price, seat_availability, seat_type):
        self.seat_price = seat_price
        self.seat_availability = seat_availability
        self.seat_type = seat_type


#print(flight_information)
#This is the basic layout for the command to get the JSON file. For now, we're working on how to get it in the first place. 
#json_file_information = json.dumps(flight_information)
#https://www.w3schools.com/python/python_json.asp describes how to use the built in json function to convert python objects to a json file