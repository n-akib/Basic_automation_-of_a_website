from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import time

class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def click(self, locator):
        for _ in range(3):
            try:
                self.wait.until(EC.element_to_be_clickable(locator)).click()
                return
            except Exception:
                time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        for _ in range(3):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.clear()
                element.send_keys(text)
                return
            except Exception:
                time.sleep(0.5)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
