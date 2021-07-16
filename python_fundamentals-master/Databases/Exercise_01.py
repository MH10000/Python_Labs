'''
All of the following exercises should be done using sqlalchemy.
Using the provided database schema, write the necessary code to print information about the film and category table.
'''
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:Bioplus1%%@localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([film])
result_proxy = connection.execute(query)

query_2 = sqlalchemy.select([category])
result_proxy_2 = connection.execute(query_2)

result_set = result_proxy.fetchmany(5)
result_set_2 = result_proxy_2.fetchmany(5)

pprint(result_set)
pprint(result_set_2)

