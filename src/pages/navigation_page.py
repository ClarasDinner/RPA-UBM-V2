from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.core.exceptions import NavigationError
from src.utils.selector_loader import load_selectors

class NavigationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.selectors = load_selectors()["navigation_page"]

    def go_to_reports(self):
        try:
            self.click(self._loc("reportes_menu"))
        except Exception as e:
            raise NavigationError(f"No se pudo acceder al menú de reportes: {e}")

    def _loc(self, name):
        sel = self.selectors[name]
        return (getattr(By, sel["by"].upper()), sel["value"])