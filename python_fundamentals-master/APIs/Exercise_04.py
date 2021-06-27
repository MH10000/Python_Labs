'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.
Again make a GET request to confirm that your information has been updated.
'''

from pprint import pprint
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

#Create user data for upload
data = {
    "id": 377,
    "first_name": "martinNew",
    "last_name": "uploadNew",
    "email": "martinNew.uploadNew@newmail.com"
}

# Post request to update user data
request = requests.put(base_url, json=data)

# Get request to retrieve data
retrieve = requests.get(base_url)
formatted = retrieve.json()

pprint(formatted)