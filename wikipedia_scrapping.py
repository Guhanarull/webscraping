import requests
from bs4 import BeautifulSoup

# Make an HTTP request to the webpage
url = 'https://en.wikipedia.org/wiki/Theropithecus'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
# data = soup.find('table', {'class': 'infobox biota'}).text
# print(data)

data = soup.find_all('td')
for d in data:
    print(d)
    