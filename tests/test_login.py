import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:

    def test_valid_login_redirects_to_inventory(self, driver):
        """Standard user should land on inventory page after login."""
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        inventory = InventoryPage(driver)
        assert inventory.is_on_inventory_page(), "Expected to be on inventory page after login"
        assert inventory.get_page_title() == "Products"

    def test_invalid_password_shows_error(self, driver):
        """Wrong password should show an error message."""
        login = LoginPage(driver).open().login("standard_user", "wrong_password")
        assert login.is_error_displayed(), "Expected an error message"
        assert "Username and password do not match" in login.get_error_message()

    def test_locked_out_user_shows_error(self, driver):
        """Locked-out user should see a specific error."""
        login = LoginPage(driver).open().login("locked_out_user", "secret_sauce")
        assert login.is_error_displayed()
        assert "locked out" in login.get_error_message().lower()

    def test_empty_username_shows_error(self, driver):
        """Empty username should prompt an error."""
        login = LoginPage(driver).open().login("", "secret_sauce")
        assert login.is_error_displayed()
        assert "Username is required" in login.get_error_message()

    def test_url_on_login_page(self, driver):
        """Verify the login page URL is correct."""
        login = LoginPage(driver).open()
        assert login.get_current_url() == LoginPage.URL
