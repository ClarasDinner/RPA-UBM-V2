from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def fill_input(self, locator, value):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.wait_for_element(locator).text