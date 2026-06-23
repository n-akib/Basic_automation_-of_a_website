import pytest
from pages.inventory_page import InventoryPage


class TestCart:

    def test_add_single_item_updates_cart_badge(self, logged_in_driver):
        """Adding one item should show badge count of 1."""
        inventory = InventoryPage(logged_in_driver)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        assert inventory.get_cart_count() == 1

    def test_add_two_items_updates_cart_badge(self, logged_in_driver):
        """Adding two items should show badge count of 2."""
        inventory = InventoryPage(logged_in_driver)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.add_item_to_cart("Sauce Labs Bike Light")
        assert inventory.get_cart_count() == 2

    def test_cart_contains_added_items(self, logged_in_driver):
        """Cart page should list all added item names."""
        inventory = InventoryPage(logged_in_driver)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.add_item_to_cart("Sauce Labs Bike Light")

        cart = inventory.go_to_cart()
        assert cart.is_on_cart_page()
        item_names = cart.get_item_names()
        assert "Sauce Labs Backpack" in item_names
        assert "Sauce Labs Bike Light" in item_names
        assert cart.get_item_count() == 2
