# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!
import requests
from bs4 import BeautifulSoup

url = "https://codingnomads.co/"

soup = BeautifulSoup(requests.get(url).text, features="html.parser")

print(soup.find_all())