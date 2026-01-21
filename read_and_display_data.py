import json

def load_data(filename):
    with open (filename, "r") as file:
        data = json.load(file)
    return data 

def display_users(data):
    print("users and their connections:\n")
    for user in data['users']:
        print(f"{user['name']} (ID : {user['id']}) - friends: {user['friends']} - Liked Pages: {user['liked_pages']}")  
    print("\nPages:\n")
    for page in data['pages']:
        print(f"{page['id']}: {page['name']}")

data = load_data("codebook_data.json")
display_users(data)
