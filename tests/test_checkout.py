import pytest
from pages.inventory_page import InventoryPage


class TestCheckout:

    def test_complete_order_shows_confirmation(self, logged_in_driver):
        """Full happy-path: add 2 items, checkout, verify confirmation."""
        inventory = InventoryPage(logged_in_driver)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.add_item_to_cart("Sauce Labs Bike Light")

        cart = inventory.go_to_cart()
        assert cart.get_item_count() == 2

        checkout = cart.proceed_to_checkout()
        checkout.fill_customer_info("Akib", "Hasan", "1216")
        checkout.continue_to_summary()

        # Verify order summary has correct items
        order_items = checkout.get_order_item_names()
        assert "Sauce Labs Backpack" in order_items
        assert "Sauce Labs Bike Light" in order_items

        checkout.finish_order()

        assert checkout.is_order_confirmed(), "Order confirmation not displayed"
        assert "Thank you" in checkout.get_confirmation_message()

    def test_checkout_without_customer_info_shows_error(self, logged_in_driver):
        """Submitting checkout with empty fields should show error."""
        inventory = InventoryPage(logged_in_driver)
        inventory.add_item_to_cart("Sauce Labs Backpack")

        cart = inventory.go_to_cart()
        checkout = cart.proceed_to_checkout()
        checkout.continue_to_summary()  # skip filling info

        assert "First Name is required" in checkout.get_error_message()

    def test_order_total_is_displayed(self, logged_in_driver):
        """Order summary should display a total price."""
        inventory = InventoryPage(logged_in_driver)
        inventory.add_item_to_cart("Sauce Labs Backpack")

        cart = inventory.go_to_cart()
        checkout = cart.proceed_to_checkout()
        checkout.fill_customer_info("Akib", "Hasan", "1216")
        checkout.continue_to_summary()

        total = checkout.get_total_price()
        assert "Total:" in total
        assert "$" in total
