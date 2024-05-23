from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

chrome_path = os.getenv('CHROME_DRIVER')
service = Service(chrome_path + "/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = chrome_path + "/chrome.exe"
web_driver = webdriver.Chrome(service=service, options=options)
web_driver.maximize_window()

url = "https://www.tutorialspoint.com/index.htm"
web_driver.get(url)
login_button = web_driver.find_element(By.CSS_SELECTOR, ".button.nav__signup-link.fw-600")
login_button.click()
user_name = web_driver.find_element(By.CSS_SELECTOR,"#login_email")
name = "7395956089"
user_name.send_keys(name)
# user_name.click()
user_password = web_driver.find_element(By.CSS_SELECTOR,"#login_password")
password = "Guhan@123"
user_password.send_keys(password)

sign_in = web_driver.find_element(By.CSS_SELECTOR,"#sign_in_btn")
sign_in.click()

try:
    # Attempt to find and click the skip button
    skip_btn = web_driver.find_element(By.CSS_SELECTOR, "#skipEmailerOtp")
    skip_btn.click()
    print("done")
except Exception as e:
    print(f"An error occurred: {e}")
