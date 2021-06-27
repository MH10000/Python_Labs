'''
Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:
Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)
It is your responsibility to build out the application to handle all menu options above.
'''
import requests
from pprint import pprint

# Define urls
user_url = "http://demo.codingnomads.co:8080/tasks_api/users"
task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

def new_account(first_name, last_name, email):
    new_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    requests.post(user_url, json=new_data)



x = 1
if x == 1:
    first_name = input(f"First name: ")
    last_name = input(f"Last name: ")
    email = input("Email address: ")
    new_account(first_name, last_name, email)

# pprint(requests.get(user_url).json())
