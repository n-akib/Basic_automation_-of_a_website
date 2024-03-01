import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#chroemdriver.exe file needs to be in the same folder
service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(3)

userName = driver.find_element(By.ID, "user-name")
userName.click()
userName.send_keys("standard_user")
time.sleep(2)

password = driver.find_element(By.ID, "password")
password.click()
password.send_keys("secret_sauce")
time.sleep(2)

login = driver.find_element(By.ID, "login-button")
login.click()

item1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
item1.click()

item2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
item2.click()
time.sleep(2)

bucket = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
bucket.click()
time.sleep(2)

checkout = driver.find_element(By.NAME, "checkout")
checkout.click()
time.sleep(3)

firstName = driver.find_element(By.ID, "first-name")
firstName.click()
firstName.send_keys("Roronoa")
time.sleep(2)

lastName = driver.find_element(By.ID, "last-name")
lastName.click()
lastName.send_keys("Zoro")
time.sleep(2)

zipCode = driver.find_element(By.ID, "postal-code")
zipCode.click()
zipCode.send_keys("2660")
time.sleep(2)

submit = driver.find_element(By.XPATH, "//input[@id='continue']")
submit.click()
time.sleep(2)

finish = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]")
finish.click()

time.sleep(5)
driver.close()