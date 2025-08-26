from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.core.config import load_config
from src.core.exceptions import LoginError
from src.utils.selector_loader import load_selectors

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.config = load_config()
        self.selectors = load_selectors()["login_page"]
        self.url = self.config["base_url"]
        self.username = self.config["credentials"]["username"]
        self.password = self.config["credentials"]["password"]

    def login(self):
        try:
            self.driver.get(self.url)
            self.fill_input(self._loc("email_input"), self.username)
            self.fill_input(self._loc("password_input"), self.password)
            self.click(self._loc("submit_button"))
        except Exception as e:
            raise LoginError(f"Fallo al iniciar sesión: {e}")

    def _loc(self, name):
        sel = self.selectors[name]
        return (getattr(By, sel["by"].upper()), sel["value"])