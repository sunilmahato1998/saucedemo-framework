from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_sort_products_by_price_low_to_high(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.wait_until_loaded()

    inventory_page.sort_by("lohi")

    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices)
