# Automatizacion de Pruebas de Regresion - Brubank

Suite de pruebas automatizadas sobre el sitio web de Brubank usando Python, Pytest, Pytest-BDD y Playwright.

La suite cubre:

- Home principal de Brubank.
- Navegacion superior y menu de Personas.
- Secciones de productos y beneficios.
- Footer, enlaces legales y redes sociales.
- Centro de Ayuda y FAQ.
- Seccion Empresas.
- Flujo de Robo y Extravío.

## Requisitos

- Python 3.8 o superior.
- Pip.
- Chromium instalado por Playwright.

## Instalacion

Desde la raiz del proyecto:

```powershell
pip install -r requirements.txt
playwright install chromium
```

Opcionalmente, si queres usar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## Ejecutar Todos Los Casos

Ejecuta toda la suite en modo headless:

```powershell
pytest
```

Ejecuta toda la suite viendo el navegador:

```powershell
pytest --headed
```

Ejecuta la suite con salida resumida:

```powershell
pytest -q
```

## Ejecutar Por Modulo

Smoke/regresion basica:

```powershell
pytest tests\test_regression.py
```

Suite BDD principal:

```powershell
pytest tests\test_brubank_bdd.py
```

Centro de Ayuda:

```powershell
pytest tests\test_ayuda_bdd.py
```

Empresas:

```powershell
pytest tests\test_empresas_bdd.py
```

FAQ:

```powershell
pytest tests\test_faq_bdd.py
```

Robo y extravio:

```powershell
pytest tests\test_robo_extravio_bdd.py
```

## Ejecutar Por Tags

Los escenarios BDD tienen tags registrados en `pytest.ini`.

Ejemplos:

```powershell
pytest -m regression
pytest -m empresas
pytest -m ayuda
pytest -m faq
pytest -m seguridad
pytest -m critical
```

## Ejecutar Un Caso Puntual

Para listar casos disponibles:

```powershell
pytest --collect-only -q
```

Para ejecutar un test exacto:

```powershell
pytest tests\test_brubank_bdd.py::test_verificar_identidad_de_marca_y_mensaje_principal_en_la_sección_hero
```

Para cortar en el primer fallo:

```powershell
pytest -x
```

Para mostrar logs y prints:

```powershell
pytest -s
```

## Reportes

La configuracion de `pytest.ini` genera automaticamente:

```text
report.html
```

Para generar otro reporte manualmente:

```powershell
pytest --html=qa-report.html --self-contained-html
```

## CI

El workflow de GitHub Actions se encuentra en:

```text
.github/workflows/playwright.yml
```

En cada push o pull request a `main` o `master`, instala dependencias, instala Chromium y ejecuta:

```powershell
pytest --html=qa-report.html --self-contained-html
```

El reporte `qa-report.html` se sube como artefacto del workflow.

## Ultima Validacion Local

La suite completa fue validada localmente con:

```powershell
pytest -q
```

Resultado:

```text
64 passed
```
