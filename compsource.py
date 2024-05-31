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
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    web_driver.get(url)
    
    time.sleep(10)
    brand = web_driver.find_element(By.CSS_SELECTOR,'div#ccs-inline-content')
    if brand:
        brand_lines = brand.text.split("MANUFACTURER NAME:")[1].strip().replace("LANGUAGE: EN","").replace("MARKET:US","")
    
    return f"brand :{brand_lines}"
    

print(get_data("https://www.compsource.com/buy/E850591/Elo-Touch-Systems-Inc-1213/Elo-i3-ISeries-POS-Terminal--Intel-Core-i5-210-GHz--8-GB-DDR4-SDRAM--128-GB-SSD-M2SATA--Wind/"))