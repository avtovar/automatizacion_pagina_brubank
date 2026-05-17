import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

@pytest.fixture(scope="function", autouse=True)
def home_page(page: Page):
    hp = HomePage(page)
    hp.goto()
    return hp

def test_navigation_menu(home_page: HomePage):
    """Acción: Verifica el menú de navegación superior."""
    home_page.verify_navigation_menu()

def test_hero_section(home_page: HomePage):
    """Acción: Verifica la sección principal (Hero)."""
    home_page.verify_hero_section()

def test_personas_menu_items(home_page: HomePage):
    """Acción: Verifica items dentro del menú Personas."""
    home_page.verify_personas_items()

def test_footer(home_page: HomePage):
    """Acción: Valida el footer legal."""
    home_page.verify_footer()

@pytest.fixture(scope="session", autouse=True)
def summary():
    yield
    print('\n================================================')
    print('🏁 REGRESIÓN FINALIZADA (PYTHON)')
    print('📄 PÁGINA: Brubank Homepage')
    print('📦 MÓDULOS: Navegación, Menú Personas, Hero, Footer')
    print('================================================\n')
