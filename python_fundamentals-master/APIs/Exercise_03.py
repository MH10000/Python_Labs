'''
Write the necessary code to make a POST request to:
    http://demo.codingnomads.co:8080/tasks_api/users
and create a user with your information.
Make a GET request to confirm that your user information has been saved.
'''

from pprint import pprint
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

#Create user data for upload
data = {
    "first_name": "martin",
    "last_name": "upload",
    "email": "martin.upload@newmail.com"
}

# Post request to update user data
request = requests.post(base_url, json=data)

# Get request to retrieve data
retrieve = requests.get(base_url)
formatted = retrieve.json()

pprint(formatted)