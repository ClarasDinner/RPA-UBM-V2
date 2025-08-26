from datetime import datetime
from src.pages.login_page import LoginPage
from src.pages.navigation_page import NavigationPage
from src.pages.reports_page import ReportsPage
from src.core.config import load_config
from src.workflows.base_workflow import BaseWorkflow

class CapacitacionWorkflow(BaseWorkflow):
    def __init__(self, driver):
        super().__init__(driver)
        self.config = load_config()
        self.fechas = self.config.get("rango_fechas", {})
        self.fecha_inicio = self.fechas.get("inicio", "2023-01-01")
        self.fecha_fin = self.fechas.get("fin", "2023-01-31")

    def run(self):
        LoginPage(self.driver).login()
        NavigationPage(self.driver).go_to_reports()
        ReportsPage(self.driver).generar_y_descargar_reporte(
            self.fecha_inicio, self.fecha_fin
        )