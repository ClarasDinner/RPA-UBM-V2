from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.core.exceptions import DownloadError
from src.utils.selector_loader import load_selectors

class ReportsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.selectors = load_selectors()["reports_page"]

    def generar_y_descargar_reporte(self, fecha_inicio, fecha_fin):
        try:
            self.fill_input(self._loc("fecha_inicio"), fecha_inicio)
            self.fill_input(self._loc("fecha_fin"), fecha_fin)
            self.click(self._loc("buscar_boton"))
            self.click(self._loc("descargar_boton"))
        except Exception as e:
            raise DownloadError(f"No se pudo descargar el reporte: {e}")

    def _loc(self, name):
        sel = self.selectors[name]
        return (getattr(By, sel["by"].upper()), sel["value"])