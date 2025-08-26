# 🧠 RPA Universidad Bulkmatic (UBM)

Este proyecto implementa un RPA en Python con Selenium para automatizar la descarga de reportes desde la plataforma de la Universidad Bulkmatic.

---

## 📁 Estructura del Proyecto

```
rpa-ubm-v2/
├── main.py
├── config/
│   ├── config.yaml
│   └── selectors.yaml
├── requirements.txt
├── Dockerfile
├── src/
│   ├── core/
│   │   ├── config.py
│   │   ├── driver.py
│   │   └── exceptions.py
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── navigation_page.py
│   │   └── reports_page.py
│   ├── workflows/
│   │   ├── base_workflow.py
│   │   └── capacitacion_workflow.py
│   └── utils/
│       └── selector_loader.py
```

---

## ⚙️ Configuración

Edita el archivo `config/config.yaml` con tus credenciales y fechas de reporte:

```yaml
base_url: "https://universidad.bulkmatic.com.mx/login"

credentials:
  username: "usuario@empresa.com"
  password: "secreto123"

rango_fechas:
  inicio: "2023-01-01"
  fin: "2023-01-31"

webdriver:
  headless: false
```

---

## ▶️ Uso (modo local)

1. Instala dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta el RPA:
```bash
python main.py capacitacion
```

3. O en modo headless:
```bash
python main.py capacitacion --headless
```

---

## 🐳 Uso con Docker

```bash
docker build -t rpa-ubm .
docker run --rm rpa-ubm
```

---

## 🧪 Flujo incluido

- ✅ Login automático
- ✅ Navegación al módulo de reportes
- ✅ Filtro por fecha
- ✅ Descarga de reporte

---

## 📌 Extensibilidad

Este proyecto usa patrones escalables como:

- Page Object Model
- Configuración desacoplada por YAML
- Separación clara por `core/`, `pages/`, `workflows/`

Puedes fácilmente agregar módulos como:

- `objetivos_workflow.py`
- `pdp_workflow.py`