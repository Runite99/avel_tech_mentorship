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
            value = value.replace('"', '')
            value = value.strip()
            record[key] = value
            
        sorter_index.append(record) 
        customer_info[user_id_to_int(record['user_id'])] = record


##User input
user_id =  input("Enter a user: ")
user_info = search_user_by_id(user_id)
print("\n")
print(user_info)
print("\n")

sorter_index.sort(key = sort_by_index)

for items in sorter_index:
    print(items)
    print("\n")

##Distance Calculation

def float_convert(user):
     return float (user)

#Get Coordinates 
def getCoordinates(user_id, keys = ['latitude', 'longitude']):
    user_id = user_id_to_int(user_id)
    keys = ['latitude', 'longitude']
    if user_id in customer_info:
        user_info = customer_info[user_id]
        if keys:
            return {key: user_info.get(key) for key in keys}
        else:
            return user_info
    return{}


user_item =  input("Enter a user: ")
user_coordinates = getCoordinates(user_item)
print("\n")
print(user_coordinates.get('latitude'))
print("\n")



##SF Coodrinates in Method
def getDistance(user_coordinates):
    #SF Coordinates
    latitude1 = 37.789107
    longitude1 = -122.40017
    ##user_coord = getCoordinates(user_coordinates)
    latitude2 = float (user_coordinates.get('latitude'))
    longitude2 = float (user_coordinates.get('longitude'))
        # and longitudes
    dLat = (latitude2 - latitude1) * math.pi / 180.0
    dLon = (longitude2 - longitude1) * math.pi / 180.0

    # Convert latitudes to radians
    latitude1 = latitude1 * math.pi / 180.0
    latitude2 = latitude2 * math.pi / 180.0

    # Haversine formula
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
         math.cos(latitude1) * math.cos(latitude2))
    rad = 6371  # Radius of Earth in kilometers
    c = 2 * math.asin(math.sqrt(a))
    distance = rad * c

    return distance

user_distance = getDistance(user_coordinates)

print("The distance is \n") 
print(user_distance)


userList = {}
userList["invite"] = []
userList["no_invite"] =[]

def output_format(userList, user):
    user_coordinates = getCoordinates(user.get('user_id'))
    user_distance = getDistance(user_coordinates)

    if user_distance <= 100:
        userList["invite"].append(user)
    else:
        userList["no_invite"].append(user)

for item in sorter_index:
    output_format(userList, item)

print("INVITE")
print("\t--------------------")
for item in userList['invite']:
    item_coordinates = getCoordinates(item.get('user_id'))
    item_distance = getDistance(item_coordinates)
    user_info = f"\t{{user_id: {item.get('user_id')}, name: '{item.get('name')}', latitude: '{item.get('latitude')}', longitude: '{item.get('longitude')}', Distance: {item_distance}}}"
    print(user_info)

# Display non-invited users
print("\nNO INVITE")
print("\t--------------------")
for item in userList['no_invite']:
    item_coordinates = getCoordinates(item.get('user_id'))
    item_distance = getDistance(item_coordinates)
    user_info = f"\t{{user_id: {item.get('user_id')}, name: '{item.get('name')}', latitude: '{item.get('latitude')}', longitude: '{item.get('longitude')}', Distance: {item_distance}}}"
    print(user_info)

    
    
    