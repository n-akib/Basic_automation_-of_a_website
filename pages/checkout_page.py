from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Step 1 — customer info
    FIRST_NAME_INPUT  = (By.ID, "first-name")
    LAST_NAME_INPUT   = (By.ID, "last-name")
    ZIP_INPUT         = (By.ID, "postal-code")
    CONTINUE_BUTTON   = (By.ID, "continue")
    ERROR_MESSAGE     = (By.CSS_SELECTOR, "[data-test='error']")

    # Step 2 — order summary
    FINISH_BUTTON     = (By.ID, "finish")
    ITEM_NAMES        = (By.CLASS_NAME, "inventory_item_name")
    SUMMARY_TOTAL     = (By.CLASS_NAME, "summary_total_label")

    # Confirmation
    CONFIRMATION_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_customer_info(self, first_name, last_name, zip_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.ZIP_INPUT, zip_code)
        return self

    def continue_to_summary(self):
        self.click(self.CONTINUE_BUTTON)
        return self

    def get_order_item_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in elements]

    def get_total_price(self):
        return self.get_text(self.SUMMARY_TOTAL)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)
        return self

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_HEADER)

    def is_order_confirmed(self):
        return self.is_visible(self.CONFIRMATION_HEADER)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
