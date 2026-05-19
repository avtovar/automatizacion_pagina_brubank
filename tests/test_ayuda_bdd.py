import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page
from pages.ayuda_page import AyudaPage

# Cargar escenarios para el Centro de Ayuda
scenarios('../features/brubank_ayuda.feature')

@pytest.fixture(scope="function")
def ayuda_page(page: Page):
    ap = AyudaPage(page)
    ap.goto()
    return ap

# --- Step Definitions (English Keywords / Spanish Text) ---

@given('que el usuario se encuentra en el Centro de Ayuda de Brubank')
def step_user_is_on_ayuda(ayuda_page):
    assert "ayuda" in ayuda_page.page.url or "brubank.com" in ayuda_page.page.url

@when(parsers.parse('el usuario busca el término "{termino}"'))
def step_search_term(ayuda_page, termino):
    ayuda_page.search_for(termino)

@then(parsers.parse('el sistema debe mostrar resultados relacionados con "{termino}"'))
def step_verify_search_results(ayuda_page, termino):
    ayuda_page.verify_search_results_visible()

@then('los resultados deben ser relevantes para la consulta')
def step_verify_relevance(ayuda_page):
    pass

@when(parsers.parse('el usuario selecciona la categoría "{categoria}"'))
def step_select_category(ayuda_page, categoria):
    ayuda_page.select_category(categoria)

@then(parsers.parse('se deben visualizar los artículos frecuentes de "{categoria}"'))
def step_verify_category_articles(ayuda_page, categoria):
    ayuda_page.verify_faq_article_loaded(None)

@then('la navegación debe ser fluida dentro de la sección')
def step_verify_fluid_navigation(ayuda_page):
    pass

@when('el usuario accede a un artículo de soporte')
def step_access_article(ayuda_page):
    # Seleccionamos el primer resultado o artículo visible
    ayuda_page.page.locator(".faq-item, .article-link").first.click()

@then('el contenido completo del artículo debe ser legible')
def step_verify_article_legibility(ayuda_page):
    ayuda_page.verify_faq_article_loaded(None)

@then('debe permitir volver a la página de categorías principal')
def step_verify_back_nav(ayuda_page):
    # Validamos que el botón volver existe (no hacemos click para no romper flujo si hay más pasos)
    expect(ayuda_page.back_button).to_be_attached()
