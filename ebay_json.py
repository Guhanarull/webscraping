import json
import requests
from bs4 import BeautifulSoup
url = "https://www.ebay.com/itm/204275338902"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

price_tag = soup.find_all("script", {"type": "application/ld+json"})

for item in price_tag:
    script_text = item.string
    json_data = json.loads(script_text)
    if json_data.get('@type') == 'Product' and 'offers' in json_data:
            price = json_data['offers']['price']
            print("Price:", price)
