from pages.login_page import LoginPage


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_login_with_invalid_username(driver):
    login_page = LoginPage(driver).open()
    login_page.login("wrong_user", "secret_sauce")

    assert "Username and password do not match" in login_page.get_error_message()


def test_login_with_invalid_password(driver):
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "wrong_password")

    assert "Username and password do not match" in login_page.get_error_message()


def test_login_with_locked_out_user(driver):
    login_page = LoginPage(driver).open()
    login_page.login("locked_out_user", "secret_sauce")

    assert "Sorry, this user has been locked out" in login_page.get_error_message()


def test_login_without_username(driver):
    login_page = LoginPage(driver).open()
    login_page.login("", "secret_sauce")

    assert "Username is required" in login_page.get_error_message()


def test_login_without_password(driver):
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "")

    assert "Password is required" in login_page.get_error_message()


def test_login_without_username_or_password(driver):
    login_page = LoginPage(driver).open()
    login_page.login("", "")

    assert "Username is required" in login_page.get_error_message()


def test_password_field_is_masked(driver):
    login_page = LoginPage(driver).open()
    password_field = driver.find_element(*login_page.password_input)

    assert password_field.get_attribute("type") == "password"
