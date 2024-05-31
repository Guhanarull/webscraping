import json
from bs4 import BeautifulSoup
import requests
import re
url = "https://www.homedepot.com/p/ECHO-21-2-cc-Gas-2-Stroke-Straight-Shaft-String-Trimmer-SRM-225/100675439"

# def clean_json(json_string):
#     cleaned = re.sub(r'[\x00-\x1f\x7f]', '', json_string)
#     return cleaned
def get_data(url: str):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find_all('script', type='application/ld+json')
    # upc_get = soup.select_one(".inlineblock.upcInfo")
    # upc_rem = upc_get.get_text(strip=True)
    mpn = None
    brand = None
    upc= None
    for items in script:
            res = json.loads(items)
            if isinstance(res,dict):
                if res.get('@type') == 'Product':
                    # upc = res.get('gtin13')
                    # mpn = res.get('sku')
                    brand = res.get('brand').get('name')
    return f"mpn :{mpn}" "\n" f"{upc}" "\n" f"brand :{brand}"
print(get_data("https://www.homedepot.com/p/ECHO-21-2-cc-Gas-2-Stroke-Straight-Shaft-String-Trimmer-SRM-225/100675439"))
