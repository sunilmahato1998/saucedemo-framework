from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.inventory_container = (By.ID, "inventory_container")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.product_names = (By.CLASS_NAME, "inventory_item_name")
        self.product_prices = (By.CLASS_NAME, "inventory_item_price")

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.inventory_container))

    def add_product_to_cart(self, product_name):
        product_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        self.wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.cart_badge)
        return badges[0].text if badges else "0"

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_link)).click()

    def sort_by(self, option_value):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))
        Select(dropdown).select_by_value(option_value)

    def get_product_names(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.product_names))
        return [element.text for element in self.driver.find_elements(*self.product_names)]

    def get_product_prices(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.product_prices))
        return [
            float(element.text.replace("$", ""))
            for element in self.driver.find_elements(*self.product_prices)
        ]
