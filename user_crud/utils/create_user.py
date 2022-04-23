import requests

URL = "http://127.0.0.1:5000/users/1"
sample_user = {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "something"
}

def create_user(first_name, last_name, hobbies):
    user_data = sample_user
    user_data["first_name"] = first_name
    user_data["last_name"] = last_name
    user_data["hobbies"] = hobbies
    response = requests.post(URL, json = user_data)
    if response.status_code == 204:
        print('success')
    else:
        print('error')
    
if __name__ == "__main__":
    first_name = input("enter first name")
    last_name = input("enter last name")
    hobbies = input("enter hobbies")
    create_user(first_name, last_name, hobbies)

