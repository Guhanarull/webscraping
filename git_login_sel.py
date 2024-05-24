from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

chrome_path = os.getenv('chrome')
service = Service(chrome_path + "/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = chrome_path + "/chrome.exe"
web_driver = webdriver.Chrome(service=service, options=options)
web_driver.maximize_window()

url = "https://github.com/"
web_driver.get(url)
# time.sleep(30)
login_button = web_driver.find_element(By.CSS_SELECTOR, ".position-relative.mr-lg-3.d-lg-inline-block>a")
login_button.click()
time.sleep(30)
user_name = web_driver.find_element(By.CSS_SELECTOR,".form-control.input-block.js-login-field")
name = "Guhanarull"
user_name.send_keys(name)
user_name.click()
user_password = web_driver.find_element(By.CSS_SELECTOR,"[id='password']")
password = "Guhan@12345"
user_password.send_keys(password)

sign_in = web_driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.btn-block.js-sign-in-button")
sign_in.click()

webscrap_page = web_driver.find_element(By.CSS_SELECTOR,"div[class='wb-break-word'] a[data-hydro-click-hmac='9640db5b634d3affc0c8774aceb4e8610daffa1a73b5d9c5acca87228bbf2d82']")
webscrap_page.click()
time.sleep(30)

# try:
#     # Attempt to find and click the skip button
#     skip_btn = web_driver.find_element(By.CSS_SELECTOR, "#skipEmailerOtp")
#     skip_btn.click()
#     print("done")
# except Exception as e:
#     print(f"An error occurred: {e}")