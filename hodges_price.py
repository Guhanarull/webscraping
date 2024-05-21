import requests
from bs4 import BeautifulSoup
url ="https://www.hodgesmarine.com/acr1951-acr-rcl100-led-searchlight-wired-kit-wmaster-c.html"
def func(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    # price = soup.select_one("meta[property='product:price:amount']").attrs['content']

    # price = soup.select_one("//*[@id="product-price-5703"]/span")
    price = soup.select_one("#product-price-5703")
    # for item in price:
    print(price.text.replace("$","").replace(",",""))
func(url)