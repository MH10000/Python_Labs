'''
Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:
    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query
BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!
'''

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:Bioplus1%%@localhost/new_testDB')

connection = engine.connect()
metadata = sqlalchemy.MetaData()

#Create new table

newTable = sqlalchemy.Table('newTable', metadata,
                       sqlalchemy.Column('Id', sqlalchemy.Integer()),
                       sqlalchemy.Column('first_name', sqlalchemy.String(100), nullable=False),
                       sqlalchemy.Column('last_name', sqlalchemy.String(100), nullable=False),
                       sqlalchemy.Column('age', sqlalchemy.Integer(), default=25),
                       sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)
              )

classesTable = sqlalchemy.Table('classes', metadata,
                       sqlalchemy.Column('class_id', sqlalchemy.Integer()),
                       sqlalchemy.Column('class_name', sqlalchemy.String(100), nullable=False),
                       sqlalchemy.Column('class_duration', sqlalchemy.Float(), nullable=False),
                       sqlalchemy.Column('class_difficulty', sqlalchemy.String(50), default='Intermediate'),
                       sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)
              )

new_classTable = sqlalchemy.Table('new_class', metadata,
                       sqlalchemy.Column('class_id', sqlalchemy.Integer(), nullable=False),
                       sqlalchemy.Column('Id', sqlalchemy.Integer(), nullable=False),
                       )




metadata.create_all(engine)

newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)
classesTable = sqlalchemy.Table('classes', metadata, autoload=True, autoload_with=engine)
new_classTable = sqlalchemy.Table('new_class', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.insert(classesTable)

new_records = [{'first_name': 'Peter', 'last_name': 'Bones', 'age': 30,'active':True},
               {'first_name': 'Luke', 'last_name': 'White', 'age': 25,'active':True},
               {'first_name': 'Susan', 'last_name': 'Black', 'age': 20,'active':True}
               ]

result_proxy = connection.execute(query,new_records)



query = sqlalchemy.insert(classesTable)
new_records = [{'class_id':1, 'class_name': 'Easy does it', 'class_duration': 30, 'class_difficulty': 'Beginner','active':True},
               {'class_id':2, 'class_name': 'Movin up', 'class_duration': 45, 'class_difficulty': 'Intermediate','active':True},
               {'class_id':3, 'class_name': 'Now we cookin', 'class_duration': 60, 'class_difficulty': 'Advanced','active':True}
               ]

result_proxy = connection.execute(query,new_records)

query_2 = sqlalchemy.insert(new_classTable)
new_records_2 = [{'class_id':1, 'Id': 1},
               {'class_id':1, 'Id': 2},
               {'class_id':3, 'Id': 3}
               ]

result_proxy_2 = connection.execute(query_2, new_records_2)

query_3 = sqlalchemy.update(newTable).values(Id=1).where(newTable.columns.first_name == 'Peter')
query_4 = sqlalchemy.update(newTable).values(Id=2).where(newTable.columns.first_name == 'Luke')
query_5 = sqlalchemy.update(newTable).values(Id=3).where(newTable.columns.first_name == 'Susan')
query_6 = sqlalchemy.update(classesTable).values(class_name='Lets get started').where(classesTable.columns.class_id == 1)
query_7 = sqlalchemy.update(new_classTable).values(class_id=2).where(new_classTable.columns.Id == 1)

result_proxy_3 = connection.execute(query_3), connection.execute(query_4), connection.execute(query_5), connection.execute(query_6), connection.execute(query_7)

query_8 = sqlalchemy.delete(newTable).where(newTable.columns.first_name == 'Luke')
query_9 = sqlalchemy.delete(classesTable).where(classesTable.columns.class_id == 2)
query_10 = sqlalchemy.delete(new_classTable).where(new_classTable.columns.class_id == 2)

results = connection.execute(query_8), connection.execute(query_9), connection.execute(query_10)

join_1 = newTable.join(new_classTable, newTable.columns.Id == new_classTable.columns.Id).join(classesTable, new_classTable.columns.class_id == classesTable.columns.class_id)
query_11 = sqlalchemy.select([newTable.columns.first_name, newTable.columns.last_name, classesTable.columns.class_name]).select_from(join_1)
join_result = connection.execute(query_11)
join_result_set = join_result.fetchall()
pprint(join_result_set)
