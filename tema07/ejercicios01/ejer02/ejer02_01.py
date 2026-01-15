import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.w3schools.com/html/html_intro.asp")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

title_tag = soup.find('title')
if title_tag:
    print(f"Título de la página: {title_tag.text}")
    
first_paragraph = soup.find('p')
if first_paragraph:
    print(f"Primer párrafo: {first_paragraph.text}")
    
all_paragraphs = soup.find_all('p')
for i in range(3):
    print(f"Párrafo {i + 1}: {all_paragraphs[i].text}")