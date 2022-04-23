import requests
from pprint import pp, pprint

URL = "http://127.0.0.1:5000/vehicles/"

def update_vehicle(vehicle_data, vehicle_id):
    response = requests.put(URL+str(vehicle_id), json = vehicle_data)
    if response.status_code == 204:
        print('success')
    else:
        print('error')

def get_vehicle(vehicle_id):
    print(URL+str(vehicle_id))
    response = requests.get(URL+str(vehicle_id))
    if response.status_code == 200:
        print('vehicle:')
        pprint(response.json().get('vehicle')[0])
        return response.json().get('vehicle')[0]
    else:
        print('error')
    
if __name__ == "__main__":
    vehicle_id = input("Enter vehicle id: ")
    target_vehicle = get_vehicle(int(vehicle_id))
    color = input("enter color: ")
    license_plate = input("enter license_plate: ")
    v_type = input("enter v_type: ")
    owner_id = input("enter owner_id: ")
    if color:
        target_vehicle["color"] = color
    if license_plate:
        target_vehicle["license_plate"] = license_plate
    if v_type:
        target_vehicle["v_type"] = v_type
    if owner_id:
        target_vehicle["owner_id"] = owner_id
    print(target_vehicle)
    update_vehicle(target_vehicle, vehicle_id)
    option = input('do you want to see the vehicle? (Y/N)')
    if option.lower() == 'y':
        get_vehicle(int(vehicle_id))