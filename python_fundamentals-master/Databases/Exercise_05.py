'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.
Create tables in a new local database to model this data.
Think about what tables are required to model this data. Do you need two tables? Three?
Persist the data returned from the API to your database.
NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.
'''
#Import dependencies
import requests
import sqlalchemy
from pprint import pprint


# Define API url's
users_url = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

# Establish database connection
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/codingNomads')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Create variables to store data from the API
user_request = requests.get(users_url).json()
task_request = requests.get(tasks_url).json()
# pprint(user_request)
# pprint(task_request)

# Function to return table info in a list
def data_table_user(table_name):
    query = sqlalchemy.select([table_name.columns.user_id])
    result_proxy = connection.execute(query)
    return result_proxy.fetchall()

def data_table_task(table_name):
    query = sqlalchemy.select([table_name.columns.task_id])
    result_proxy = connection.execute(query)
    return result_proxy.fetchall()

# Create database tables
userTable = sqlalchemy.Table('users', metadata,
                       sqlalchemy.Column('user_id', sqlalchemy.Integer(), nullable=False),
                       sqlalchemy.Column('first_name', sqlalchemy.String(100), nullable=False),
                       sqlalchemy.Column('last_name', sqlalchemy.String(100), nullable=False),
                       sqlalchemy.Column('email', sqlalchemy.String(100), nullable=False),
                       sqlalchemy.Column('createdAt', sqlalchemy.BigInteger(), nullable=False),
                       sqlalchemy.Column('updatedAt', sqlalchemy.BigInteger())
              )

taskTable = sqlalchemy.Table('tasks', metadata,
                       sqlalchemy.Column('task_id', sqlalchemy.Integer(), nullable=False),
                       sqlalchemy.Column('task_name', sqlalchemy.String(100), nullable=False),
                       sqlalchemy.Column('task_description', sqlalchemy.String(200), nullable=False),
                       sqlalchemy.Column('createdAt', sqlalchemy.BigInteger(), nullable=False),
                       sqlalchemy.Column('updatedAt', sqlalchemy.BigInteger()),
                       sqlalchemy.Column('completed', sqlalchemy.Boolean(), default=True)
              )

user_taskTable = sqlalchemy.Table('users_tasks', metadata,
                       sqlalchemy.Column('task_id', sqlalchemy.Integer(), nullable=False),
                       sqlalchemy.Column('user_id', sqlalchemy.Integer(), nullable=False)
              )

metadata.create_all(engine)

# Load tables
userTable = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)
taskTable = sqlalchemy.Table('tasks', metadata, autoload=True, autoload_with=engine)
user_taskTable = sqlalchemy.Table('users_tasks', metadata, autoload=True, autoload_with=engine)

# Populate user table
x = 0
for items in user_request["data"]:
    if user_request["data"][x]["id"] not in data_table_user(userTable):
        query = sqlalchemy.insert(userTable).values(user_id=user_request["data"][x]["id"], first_name=user_request["data"][x]["first_name"], last_name=user_request["data"][x]["last_name"], email=user_request["data"][x]["email"], createdAt=user_request["data"][x]["createdAt"], updatedAt=user_request["data"][x]["updatedAt"])
        result_proxy = connection.execute(query)
    x += 1

# Populate task table
y = 0
for items in task_request["data"]:
    if user_request["data"][y]["id"] not in data_table_task(taskTable):
        query_2 = sqlalchemy.insert(taskTable).values(task_id=task_request["data"][y]["id"], task_name=task_request["data"][y]["name"], task_description=task_request["data"][y]["description"], createdAt=task_request["data"][y]["createdAt"], updatedAt=task_request["data"][y]["updatedAt"], completed=task_request["data"][y]["completed"])
        result_proxy = connection.execute(query_2)
    y += 1

# Populate user_task table
z = 0
for items in task_request["data"]:
    if user_request["data"][z]["id"] not in data_table_user(user_taskTable):
        query_3 = sqlalchemy.insert(user_taskTable).values(task_id=task_request["data"][z]["id"], user_id=task_request["data"][z]["userId"])
        result_proxy = connection.execute(query_3)
    z += 1








print("Martin, it is true:")
print("You are a genius!")