# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

BASE_URL = "https://pokeapi.co/api/v2/pokemon/?limit=6"
type_url = "https://pokeapi.co/api/v2/pokemon/"

import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

data = requests.get(BASE_URL).json()


name_list = []
x = 0
for name in data["results"]:
    name = {"name": data["results"][x]["name"], "id": data["results"][x]["url"][-2]}
    name_list.append(name)
    x += 1

char_dets = []
y = 1
for type_ in name_list:
    type_ = requests.get(type_url+name_list[y]["id"]).json()["types"][1]["type"]["name"]
    char_dets.append(type_)
    y += 1

print(char_dets)

