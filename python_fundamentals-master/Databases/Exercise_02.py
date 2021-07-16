'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:
- Select all the actors with the first name of your choice
- Select all the actors and the films they have been in
- Select all the actors that have appeared in a category of a comedy of your choice
- Select all the comedic films and sort them by rental rate
- Using one of the statements above, add a GROUP BY statement of your choice
- Using one of the statements above, add a ORDER BY statement of your choice
'''
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:Bioplus1%%@localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

# query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'JOHNNY').order_by(sqlalchemy.desc(actor.columns.last_name))
# result_proxy = connection.execute(query)

join_statement = actor.join(film_actor, actor.columns.actor_id == film_actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
query_2 = sqlalchemy.select([film.columns.film_id, film.columns.title, actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)
result_proxy_2 = connection.execute(query_2)

# join_statement_2 = actor.join(film_actor, actor.columns.actor_id == film_actor.columns.actor_id).join(film, film_actor.columns.film_id == film.columns.film_id).join(film_category, film.columns.film_id == film_category.columns.film_id)
# query_3 = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name]).where(film_category.columns.category_id == 5, film.columns.rating == 'PG').select_from(join_statement_2)
# result_proxy_3 = connection.execute(query_3)

# join_statement_3 = film_category.join(film, film_category.columns.film_id == film.columns.film_id)
# query_4 = sqlalchemy.select([film.columns.film_id, film.columns.title, film.columns.rental_rate]).where(film_category.columns.category_id == 5).select_from(join_statement_3).order_by(sqlalchemy.asc(film.columns.rental_rate))
# result_proxy_4 = connection.execute(query_4)

# result_set = result_proxy.fetchall()
result_set_2 = result_proxy_2.fetchall()
# result_set_3 = result_proxy_3.fetchall()
# result_set_4 = result_proxy_4.fetchall()

# pprint(result_set)
pprint(result_set_2)
# pprint(result_set_3)
# pprint(result_set_4)

