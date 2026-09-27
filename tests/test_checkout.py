from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_checkout_order(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    inventory_page.wait_until_loaded()
    products = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    for product in products:
        inventory_page.add_product_to_cart(product)

    assert inventory_page.get_cart_count() == "2"
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_item_names() == products
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_information("Ajay", "Singh", "110001")
    checkout_page.continue_to_overview()
    checkout_page.finish_order()

    assert checkout_page.get_confirmation_message() == "Thank you for your order!"
