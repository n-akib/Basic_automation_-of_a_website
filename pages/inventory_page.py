from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    PAGE_TITLE       = (By.CLASS_NAME, "title")
    CART_ICON        = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE       = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN    = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS  = (By.CLASS_NAME, "inventory_item")

    def _add_to_cart_btn(self, item_name):
        """Returns the Add to Cart button locator for a specific item by name."""
        item_id = item_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        return (By.ID, f"add-to-cart-{item_id}")

    def add_item_to_cart(self, item_name):
        self.click(self._add_to_cart_btn(item_name))
        return self

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_ICON)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def is_on_inventory_page(self):
        return self.URL in self.get_current_url()
