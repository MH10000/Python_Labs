# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests
import json

BASE_URL = "https://ghibliapi.herokuapp.com/people"

data = requests.get(BASE_URL).json()

print("Studio Gibli cat list:")

for x in data:
    name = x["name"]
    gender = x["gender"]
    hair = x["hair_color"]
    eyes = x["eye_color"]
    print(f"name: {name}, gender: {gender}, hair color: {hair}, eye color: {eyes}")



