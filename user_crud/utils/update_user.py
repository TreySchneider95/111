import requests
from pprint import pp, pprint

URL = "http://127.0.0.1:5000/users/"

def update_user(user_data, user_id):
    response = requests.put(URL+str(user_id), json = user_data)
    if response.status_code == 204:
        print('success')
    else:
        print('error')

def get_user(user_id):
    print(URL+str(user_id))
    response = requests.get(URL+str(user_id))
    if response.status_code == 200:
        print('user:')
        pprint(response.json().get('user')[0])
        return response.json().get('user')[0]
    else:
        print('error')
    
if __name__ == "__main__":
    user_id = input("Enter user id: ")
    target_user = get_user(int(user_id))
    first_name = input("enter new first name (or leave blank)")
    last_name = input("enter new last name (or leave blank)")
    hobbies = input("enter new hobbies (or leave blank)")
    if first_name:
        target_user["first_name"] = first_name
    if last_name:
        target_user["last_name"] = last_name
    if hobbies:
        target_user["hobbies"] = hobbies
    print(target_user)
    update_user(target_user, user_id)
    option = input('do you want to see the user? (Y/N)')
    if option.lower() == 'y':
        get_user(int(user_id))