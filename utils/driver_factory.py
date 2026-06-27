import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(headless=False):
    options = webdriver.ChromeOptions()
    
    # Detect standard Chrome path, or fallback to Brave Browser on macOS
    binary_path = None
    for path in [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    ]:
        if os.path.exists(path):
            binary_path = path
            options.binary_location = path
            break

    driver_version = None
    if binary_path:
        try:
            # Query the browser version dynamically (e.g. "Brave Browser 149.1.91.178")
            version_out = subprocess.check_output([binary_path, "--version"]).decode("utf-8").strip()
            driver_version = version_out.split()[-1].split('.')[0]
        except Exception:
            pass

    if headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    manager = ChromeDriverManager(driver_version=driver_version) if driver_version else ChromeDriverManager()
    driver = webdriver.Chrome(service=ChromeService(manager.install()), options=options)
    driver.implicitly_wait(5)
    return driver
