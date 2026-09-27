from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")

    def get_item_names(self):
        return [element.text for element in self.driver.find_elements(*self.cart_items)]

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()
