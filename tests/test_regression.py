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
    home_page.verify_nav_option("Personas")
    home_page.verify_nav_option("Empresas")
    home_page.verify_nav_option("Ayuda")

def test_hero_section(home_page: HomePage):
    """Acción: Verifica la sección principal (Hero)."""
    home_page.verify_hero_message("banco")

def test_personas_menu_items(home_page: HomePage):
    """Acción: Verifica items dentro del menú Personas."""
    home_page.explore_personas_menu()
    home_page.verify_persona_service("Cuenta")

def test_footer(home_page: HomePage):
    """Acción: Valida el footer legal."""
    home_page.verify_footer_legal_link("Información importante")

@pytest.fixture(scope="session", autouse=True)
def summary():
    yield
    print('\n================================================')
    print('🏁 REGRESIÓN FINALIZADA (PYTHON)')
    print('📄 PÁGINA: Brubank Homepage')
    print('📦 MÓDULOS: Navegación, Menú Personas, Hero, Footer')
    print('================================================\n')
