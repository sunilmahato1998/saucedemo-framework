import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--guest")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.get(LoginPage.URL)
    yield browser
    browser.quit()
