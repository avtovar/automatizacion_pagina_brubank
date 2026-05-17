# Automatización de Pruebas de Regresión - Brubank (Python)

Este proyecto realiza pruebas de regresión automatizadas sobre el sitio web de Brubank utilizando **Python**, **Pytest** y **Playwright**.

## 📋 Requisitos Previos

- Python 3.8 o superior.
- Pip (gestor de paquetes de Python).

## 🚀 Instalación Local

1.  **Clonar el repositorio:**
    ```bash
    git clone <url-del-repositorio>
    cd automatizacion_pagina_brubank
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Instalar los navegadores de Playwright:**
    ```bash
    playwright install chromium
    ```

## 🛠️ Ejecución de Pruebas

Para correr las pruebas de manera local y ver el navegador en vivo:

```bash
pytest --headed
```

- `--headed`: Abre el navegador para que puedas ver las acciones en vivo.
- Las pruebas generarán automáticamente un reporte HTML llamado `report.html` en la raíz del proyecto.

## 📊 Reportes

Al finalizar la ejecución, abre el archivo `report.html` en cualquier navegador para ver los resultados detallados de cada prueba.

## 🤖 Integración Continua (CI)

Este proyecto incluye un workflow de GitHub Actions que ejecuta las pruebas automáticamente en cada push o pull request. Los resultados y reportes se suben como artefactos de la ejecución.
