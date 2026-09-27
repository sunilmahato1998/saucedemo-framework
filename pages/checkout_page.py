from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.confirmation_header = (By.CLASS_NAME, "complete-header")

    def enter_information(self, first_name, last_name, postal_code):
        for locator, value in (
            (self.first_name_input, first_name),
            (self.last_name_input, last_name),
            (self.postal_code_input, postal_code),
        ):
            field = self.wait.until(EC.visibility_of_element_located(locator))
            field.clear()
            field.send_keys(value)

    def continue_to_overview(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_button)).click()

    def get_confirmation_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.confirmation_header)).text
