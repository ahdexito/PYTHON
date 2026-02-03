import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.w3schools.com/html/html_links.asp")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

all_links = soup.find_all('a')

for link in all_links:
    href = link.get('href')
    if href:
        print(f"- {link.text.strip()}: {href}")