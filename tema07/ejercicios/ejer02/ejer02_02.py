import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.w3schools.com/html/html_links.asp")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

