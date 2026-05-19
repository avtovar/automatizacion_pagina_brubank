import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect
from pages.ayuda_page import AyudaPage

# Cargar escenarios específicos de Robo y Extravío
scenarios('../features/brubank_robo_extravio.feature')

@pytest.fixture(scope="function")
def ayuda_page(page: Page):
    ap = AyudaPage(page)
    ap.goto()
    return ap

# --- Step Definitions ---

@given('que el usuario se encuentra en el Centro de Ayuda de Brubank')
def step_user_is_on_ayuda(ayuda_page):
    assert "ayuda" in ayuda_page.page.url or "brubank.com" in ayuda_page.page.url

@when(parsers.parse('el usuario busca el término "{termino}"'))
def step_search_emergency_term(ayuda_page, termino):
    ayuda_page.search_for(termino)

@then(parsers.parse('el sistema debe mostrar resultados relacionados con "{termino}"'))
def step_verify_emergency_results(ayuda_page, termino):
    ayuda_page.verify_search_results_visible()

@then(parsers.parse('debe ser visible el artículo principal sobre "{tema}"'))
def step_verify_emergency_article(ayuda_page, tema):
    # Buscamos que el texto esté presente en los resultados
    expect(ayuda_page.page.get_by_text(tema, exact=False).first).to_be_visible()

@when('el usuario selecciona la categoría "Seguridad"')
def step_select_security_category(ayuda_page):
    ayuda_page.select_category("Seguridad")

@then(parsers.parse('debe visualizarse la opción de "{opcion}"'))
def step_verify_security_option(ayuda_page, opcion):
    expect(ayuda_page.page.get_by_text(opcion, exact=False).first).to_be_visible()

@then('el contenido debe explicar cómo bloquear la tarjeta desde la app')
def step_verify_block_instructions(ayuda_page):
    # Entramos al primer artículo de la categoría
    ayuda_page.page.locator(".faq-item, .article-link").first.click()
    expect(ayuda_page.page.get_by_text("bloquear", exact=False).first).to_be_visible()
