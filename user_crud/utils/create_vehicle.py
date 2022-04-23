import requests

URL = "http://127.0.0.1:5000/vehicles/1"

def create_vehicle(color, license_plate, v_type, owner_id):
    vehicle_data = dict()
    vehicle_data["color"] = color
    vehicle_data["license_plate"] = license_plate
    vehicle_data["v_type"] = v_type
    vehicle_data["owner_id"] = owner_id
    response = requests.post(URL, json = vehicle_data)
    if response.status_code == 204:
        print('success')
    else:
        print('error')
    
if __name__ == "__main__":
    color = input("enter color: ")
    license_plate = input("enter license_plate: ")
    v_type = input("enter v_type: ")
    owner_id = input("enter owner_id: ")
    create_vehicle(color, license_plate, v_type, owner_id)