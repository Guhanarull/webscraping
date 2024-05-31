from bs4 import BeautifulSoup
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_path = os.getenv('chrome')
service = Service(chrome_path + "/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = chrome_path + "/chrome.exe"
web_driver = webdriver.Chrome(service = service,options = options)
web_driver.maximize_window()

def get_data(url: str):
    web_driver.get(url)
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    brand = web_driver.find_element(By.CSS_SELECTOR,"#get-mfr-name")
    mpn = web_driver.find_element(By.CSS_SELECTOR,".product-mfrsku.getMfrId")
    upc = "none"
    return f"mpn :{mpn.text}" "\n"  f"upc :{upc}" "\n" f"brand :{brand.text}"
    

print(get_data("https://www.neobits.com/chargepoint_cph50_nema6_50_l23_home_point_electric_p16052610.html"))