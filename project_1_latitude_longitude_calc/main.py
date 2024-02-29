import json

import math

from math import radians, cos, sin, asin, sqrt

file_path = "/home/agun34/avel_tech_mentorship/project_1_latitude_longitude_calc/Customer List.txt"
def user_id_to_int(user_id):
     return int (user_id)
    
def search_user_by_id(user_id):
    user_id = user_id_to_int(user_id)
    if user_id in customer_info:
        return customer_info[user_id]
    return {}
##Variable

##index_sorter = []
def sort_by_index(user):
    user = user_id_to_int(user['user_id'])
    return user
    ##return sorted(index_type, key=lambda x: index_type[x]['user_id'])
    





## Reads Index
with open(file_path, 'r') as file:
    index = file.read()
    
new_index = index.split("\n")

##Store Variable
customer_info = {}
sorter_index = []
for lines in new_index:
    if lines:
        lines = lines.split(",")
        record = {}
        sorter = {}
        for inner_lines in lines:
            inner_lines = inner_lines.split(":")
            key = inner_lines[0].replace('{', '')
            key = key.strip()
            value = inner_lines[1].replace('}', '')
            value = value.strip()
            record[key] = value
            
        sorter_index.append(record) 
        customer_info[user_id_to_int(record['user_id'])] = record


##for item in sorter_index:
    ##print(item) 


##print(customer_info)
##for line in data_index:
    ##print(line)

##User input
user_id =  input("Enter a user: ")
user_info = search_user_by_id(user_id)
print("\n")
print(user_info)

sorter_index.sort(key = sort_by_index)

for items in sorter_index:
    print(items)
    print("\n")
##sorting_type = input("Enter a sorting type: ")
##sort_info = sort_by_index(sorting_type)
    
    

    

##data_index = data.append()

##index = file_index.append()
##print(user_info) 

##Distance Calculation

def float_converter(user):
    user = user_id_to_int(user['latitude', 'longitude'])
    return float (user)

def getCoordinates(user):
    user = float_converter(user)
    return user

def getDistance(latitude1, longitude1, latidue2, longitude2):
    
    distance = 2
        # and longitudes
    dLat = (longitude1 - latitude1) * math.pi / 180.0
    dLon = (latidue2 - longitude2) * math.pi / 180.0
 
    # convert to radians
    latitude1 = (latitude1) * math.pi / 180.0
    latidue2 = (latidue2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(latitude1) * math.cos(latidue2))
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c
    return distance
    
    
    