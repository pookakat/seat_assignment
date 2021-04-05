import sys
import xml.etree.ElementTree as ET
import json

xml_doc = str(sys.argv[1])
tree = ET.parse(xml_doc)
root = tree.getroot()

#This section is going to make some assumptions in regards to scalability. The XML documents provided either come from IATA or #Opentravel, and the biggest assumption in regards to this is that IATA follows one format consistently, and Opentravel follows the #other. 
#Here is where we'll find out which file is presented and how it will be handled.
Rows = []
Seats = []
class FlightObject:
    def __init__ (self, departure_date_time, departure_loc, arrival_loc, equipment_type, row):
        self.departure_date_time = departure_date_time
        self.departure_loc = departure_loc
        self.arrival_loc = arrival_loc
        self.equipment_type = equipment_type
        self.row = row

class RowObject:
    def __init__ (self, class_type, row_numbers, seat):
        self.class_type = class_type
        self.row_numbers = row_numbers
        self.seat = seat

class SeatObject:
    def __init__ (self, seat_id, avail_status, feature, price):
        self.seat_id = seat_id
        self.avail_status = avail_status
        self.feature = feature
        self.price = price

def strip_url_from_tag(child_info):
    entire_tag = str(child_info)
    url_information, unused_portion = entire_tag.split("}")
    url_information += "}"
    return url_information

def get_date_time(date_time_dict):
    date_time = str(date_time_dict.get('DepartureDateTime'))
    return date_time

def get_location_code(location_dict):
    airport_code = str(location_dict.get('LocationCode'))
    return airport_code

def get_equipment(equipment_dict):
    flight_equipment = str(equipment_dict.get('AirEquipType'))
    return flight_equipment

def get_seat_info(seat_dict):
    seat_id = str(seat_dict.get('SeatNumber'))
    avail_status = str(seat_dict.get('AvailableInd'))
    if avail_status == 'false':
        avail_status = 'Unavailable'
    else:
        avail_status = 'Available'
    return seat_id, avail_status

def get_fees_info(fees_dict):
    amount = float(fees_dict.get('Amount'))
    decimal = float(fees_dict.get("DecimalPlaces"))
    currency = str(fees_dict.get('CurrencyCode'))
    places = 10 ** -decimal
    total = amount * places
    price = '{:,.2f} '.format(total) + currency
    return price

def get_class(row_info_dict):
    class_type = str(row_info_dict.get('CabinType'))
    row_number = str(row_info_dict.get('RowNumber'))
    return class_type, row_number

def ota_flight_handling(url_information):
    for flight_departure_date_time in root.iter('{}FlightSegmentInfo'.format(url_information)):
        flight_departure_date_time = get_date_time(flight_departure_date_time.attrib)

    for flight_departure_loc in root.iter('{}DepartureAirport'.format(url_information)):
        flight_departure_loc = get_location_code(flight_departure_loc.attrib)

    for flight_arrival_loc in root.iter('{}ArrivalAirport'.format(url_information)):
        flight_arrival_loc = get_location_code(flight_arrival_loc.attrib)

    for flight_equip_type in root.iter('{}Equipment'.format(url_information)):
        flight_equip_type = (get_equipment(flight_equip_type.attrib))

    for row_info in root.iter('{}RowInfo'.format(url_information)):
        price = ""
        for seat_info in row_info.iter('{}SeatInfo'.format(url_information)):
            for seat in seat_info.iter('{}Summary'.format(url_information)):
                seat = seat.attrib
                seat_id, avail_status = get_seat_info(seat)
            for features in seat_info.iter('{}Features'.format(url_information)):
                feature_check = features.text
                if feature_check != "Other_":
                    feature = feature_check
            for service in seat_info.iter('{}Service'.format(url_information)):
                for fees in service.iter('{}Fee'.format(url_information)):
                    fees = fees.attrib
                    price = get_fees_info(fees)
            seat_object = SeatObject(seat_id, avail_status, feature, price)
            seat = seat_object.__dict__
            Seats.append(seat)
        row_info = row_info.attrib
        class_type, row_number = get_class(row_info)
        row_object = RowObject(class_type, row_number, Seats)
        row = row_object.__dict__
        Rows.append(row)
    flight_obect = FlightObject(flight_departure_date_time, flight_departure_loc, flight_arrival_loc, flight_equip_type, Rows)
    return flight_obect

def iata_flight_handling(url_information):
    print('No programming yet to handle {}. Please try again later'.format(url_information))

for child in root[0]:
    if 'IATA' in child.tag:
        print("IATA flight information recieved!")
        url_information = strip_url_from_tag(child.tag)
        iata_flight_handling(url_information)
#       No code yet for this type, so I'm just going to leave this line in for later
#         flight = iata_flight_handling(url_information)     
    elif 'OTA' in child.tag:
        print("OpenTravel flight information received!")
        url_information = strip_url_from_tag(child.tag)
        flight = ota_flight_handling(url_information)
    else:
        print("Invalid File Type")


file_name = xml_doc.replace(".xml", "_parsed.json")
flight_info = flight.__dict__
with open(file_name, 'w') as outfile:
    json.dump(flight_info, outfile)
#These are helpful links to finish this project:
#https://docs.python.org/3/library/xml.etree.elementtree.html is my ElementTree documentation
#https://anenadic.github.io/2014-11-10-manchester/novice/python/06-cmdline-non-interactive.html is running Python from the command line
#https://www.datacamp.com/community/tutorials/dictionary-python?utm_source=adwords_ppc&utm_campaignid=1565261270&utm_adgroupid=67750485268&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=295208661514&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9009680&gclid=CjwKCAjw3pWDBhB3EiwAV1c5rCFSPniwB33l4PLFUr1_wJnwssiPVwmvpVDR_mxjAGd7P1dai_dbzRoC03sQAvD_BwE python dictionaries

#print(flight_information)
#This is the basic layout for the command to get the JSON file. For now, we're working on how to get it in the first place. 
#json_file_information = json.dumps(flight_information)
#https://www.w3schools.com/python/python_json.asp describes how to use the built in json function to convert python objects to a json file