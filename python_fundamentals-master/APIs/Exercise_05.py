'''
Write a program that makes a DELETE request to remove the user your create in a previous example.
Again, make a GET request to confirm that information has been deleted.
'''

from pprint import pprint
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

# Delete request to delete user data
request = requests.delete(base_url + "/377")

# Get request to retrieve data
retrieve = requests.get(base_url)
formatted = retrieve.json()

pprint(formatted)