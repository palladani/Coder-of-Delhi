import json

def clean_data(data):

    # Remove the user with missing name
    data['users'] = [user for user in data['users'] if user['name'].strip()]

    #Remove duplicate friends

    for user in data['users']:
        user['friends'] = list(set(user['friends']))

    # Remove inactive user

    data['users'] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]

    # Remove duplicate pages

    unique_pages = {}

    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())

    return data

data = json.load(open("codebook_data_with_missing_value.json"))
data = clean_data(data)
json.dump(data, open("cleaned_codebook_data_with_missing_value.json", "w"))

print("Data cleaned successfully!")