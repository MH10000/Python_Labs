'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.
'''


import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

# Get request to retrieve data from API and create Json format
request = requests.get(base_url)
data = request.json()

# Create new list and loop through, while appending the email each time to the list
email_list = []
x = 0
for email in data["data"]:
    email_list.append(data["data"][x]["email"])
    x += 1


print(email_list)