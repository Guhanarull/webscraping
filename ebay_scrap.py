import os
import time
from bs4 import BeautifulSoup
import logging
import requests

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=52064&_sacat=0"
response = requests.get(url)
if response.status_code==200:
    print("status 200")
else:
    print("error in url")
soup = BeautifulSoup(response.text, "html.parser")

sun_titles = soup.select('.s-item__title>span[role="heading"]')

for item in sun_titles:
    print(item.get_text().strip())
    # return

price = soup.select(".s-item__detail.s-item__detail--primary > span[class='s-item__price']")
for tag in price:
    print((tag.get_text().strip().replace("$","")))

output_file = 'ebay.txt'

with open(output_file,"w")as file:
    file.write("title\tcost\n")
    print("done")

    for title,cost in zip(sun_titles,price):
        title_text = title.get_text().strip().replace("$","")
        price_text = cost.get_text().strip().replace("$","")
        file.write(f"{title_text}\t{price_text}\n")
print("done")