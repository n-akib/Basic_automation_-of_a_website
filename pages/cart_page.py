from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    # Locators
    CART_ITEMS       = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES       = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON  = (By.ID, "checkout")
    CONTINUE_BUTTON  = (By.ID, "continue-shopping")

    def get_item_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in elements]

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait.until(lambda d: "checkout-step-one" in d.current_url)
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)

    def is_on_cart_page(self):
        return self.URL in self.get_current_url()
