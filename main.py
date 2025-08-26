import argparse
from src.core.driver import build_driver
from src.workflows.capacitacion_workflow import CapacitacionWorkflow
from src.core.exceptions import LoginError, NavigationError, DownloadError

def main():
    parser = argparse.ArgumentParser(description="RPA UBM CLI")
    parser.add_argument("workflow", choices=["capacitacion"], help="Flujo a ejecutar")
    parser.add_argument("--headless", action="store_true", help="Ejecutar en modo headless (sin navegador visible)")
    args = parser.parse_args()

    driver = build_driver(headless=args.headless)

    try:
        if args.workflow == "capacitacion":
            CapacitacionWorkflow(driver).run()

    except (LoginError, NavigationError, DownloadError) as e:
        print(f"❌ Error en el flujo: {e}")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")
    finally:
        driver.quit()
        print("✅ Proceso finalizado.")

if __name__ == "__main__":
    main()