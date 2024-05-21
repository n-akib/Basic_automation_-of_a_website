import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#path of chroemdriver.exe file
service = Service(executable_path="C:/Program Files (x86)/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://www.saucedemo.com/")

url = driver.current_url

if url == "https://www.saucedemo.com/":
    print("URL Verified")
else:
    print("URL Verification Failed")

assert "https://www.saucedemo.com/" in driver.current_url


time.sleep(5)

driver.close()
