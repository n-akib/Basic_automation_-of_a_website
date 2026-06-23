import pytest
from utils.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    """Launches Chrome before each test and quits after."""
    driver = get_driver(headless=True)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Provides a driver already logged in as standard_user."""
    from pages.login_page import LoginPage
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    yield driver
