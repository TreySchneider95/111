import requests

URL = "http://127.0.0.1:5000/vehicles/"


def del_vehicle(vehicle_id):
    response = requests.delete(URL+str(vehicle_id))
    if response.status_code == 204:
        print("Success")
    else:
        print('Error deactivating vehicle')


if __name__ == "__main__":
    vehicle_id = input("Enter vehicle id: ")
    del_vehicle(vehicle_id)