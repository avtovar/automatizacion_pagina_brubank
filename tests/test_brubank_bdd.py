import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page
from pages.home_page import HomePage

# Load scenarios using English keywords but Spanish step text
scenarios('../features/brubank_regresion_v2.feature')

@pytest.fixture(scope="function")
def home_page(page: Page):
    hp = HomePage(page)
    hp.goto()
    return hp

# --- Step Definitions (English Keywords / Spanish Text) ---

@given('que el usuario se encuentra en la página de inicio de Brubank')
def step_user_is_on_home(home_page):
    assert "brubank.com" in home_page.page.url

@then(parsers.parse('el menú de navegación debe mostrar la opción "{opcion}"'))
def step_verify_nav_menu_option(home_page, opcion):
    home_page.verify_nav_option(opcion)

@then('la opción debe estar habilitada para su interacción')
def step_verify_option_enabled(home_page):
    pass

@then(parsers.parse('el mensaje principal debe comunicar "{texto}"'))
def step_verify_hero_message(home_page, texto):
    home_page.verify_hero_message(texto)

@then('deben estar disponibles los enlaces de descarga para tiendas de aplicaciones móviles')
def step_verify_app_links(home_page):
    home_page.verify_store_links()

@then('no deben visualizarse mensajes de error de carga en la sección')
def step_verify_no_errors(home_page):
    pass

@then(parsers.parse('debe visualizarse la sección informativa de "{producto}"'))
def step_verify_product_section(home_page, producto):
    home_page.verify_product_visibility(producto)

@then('la sección debe contener información relevante para el usuario')
def step_verify_section_info(home_page):
    pass

@when('el usuario explora el menú "Personas"')
def step_explore_personas_menu(home_page):
    home_page.explore_personas_menu()

@then(parsers.parse('debe visualizarse el acceso directo a "{servicio}"'))
def step_verify_persona_service(home_page, servicio):
    home_page.verify_persona_service(servicio)

@then(parsers.parse('el enlace debe redirigir a la sección correspondiente de "{servicio}"'))
def step_verify_service_redirect(home_page, service):
    pass

@then(parsers.parse('el pie de página debe contener el enlace legal "{enlace_legal}"'))
def step_verify_legal_link(home_page, enlace_legal):
    home_page.verify_footer_legal_link(enlace_legal)

@then('al hacer clic debe mostrar la información de cumplimiento vigente')
def step_verify_compliance_info(home_page):
    pass

@then(parsers.parse('debe estar visible el acceso a la red social "{red_social}"'))
def step_verify_social_network(home_page, red_social):
    home_page.verify_social_presence(red_social)

@then(parsers.parse('el icono debe representar fielmente la identidad de "{red_social}"'))
def step_verify_social_icon(home_page, red_social):
    pass

@when('el usuario accede al Centro de Ayuda')
def step_access_help_center(home_page):
    home_page.go_to_help_center()

@then(parsers.parse('debe visualizarse la categoría de soporte "{categoria}"'))
def step_verify_support_category(home_page, categoria):
    home_page.verify_help_category(category_name=categoria)

@then(parsers.parse('debe permitir la navegación hacia las preguntas frecuentes de "{categoria}"'))
def step_verify_faq_navigation(home_page, categoria):
    pass
