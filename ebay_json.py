import json
import requests
from bs4 import BeautifulSoup

url = "https://anchorexpress.com/products/furuno-infolink-bbwx4-satellite-weather-receiver"
# url = "https://www.ebay.com/itm/204275338902"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all scripts of type "application/ld+json"
data_types = soup.find_all("script", {"type": "application/ld+json"})

for item in data_types:
    data_types = json.loads(item.string)
    if data_types.get("@type") == "Product":
            hi = data_types['offers']
            for offer in hi:
                price = offer.get('price')
                print("Price:", price)

