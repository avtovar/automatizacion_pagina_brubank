# Automatización Brubank (Python) 🐍

Este proyecto es el equivalente en **Python** de la suite de pruebas de Brubank, utilizando **Playwright** y **Pytest**.

## 📋 Requisitos
- **Python 3.10+**
- **Pip** (Gestor de paquetes de Python)

## 🚀 Instalación

1. Navega a la carpeta del proyecto:
   ```bash
   cd automatizacion_pagina_brubank
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Instala los navegadores de Playwright:
   ```bash
   playwright install
   ```

## 🏃 Cómo Correr los Tests

### Ejecución Estándar (Headless)
```bash
pytest
```

### Ejecución con Navegador Visible (Headed)
```bash
pytest --headed
```

### Ejecución en un navegador específico (ej. Chrome)
```bash
pytest --browser chromium --headed
```

## 🏗️ Estructura
- `pages/`: Contiene el Page Object Model (`home_page.py`).
- `tests/`: Contiene los archivos de prueba (`test_regression.py`).
- `requirements.txt`: Lista de dependencias necesarias.
