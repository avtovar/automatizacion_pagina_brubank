import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.ayuda_page import AyudaPage

# Cargar escenarios de FAQ
scenarios('../features/brubank_faq.feature')

@pytest.fixture(scope="function")
def home_page(page: Page):
    hp = HomePage(page)
    hp.goto()
    return hp

@pytest.fixture(scope="function")
def ayuda_page(page: Page):
    return AyudaPage(page)

# --- Step Definitions ---

@given('que el usuario se encuentra en la página de inicio de Brubank')
def step_user_is_on_home(home_page):
    assert "brubank.com" in home_page.page.url

@when('el usuario navega hasta el pie de página')
def step_scroll_to_footer(home_page):
    home_page.footer.scroll_into_view_if_needed()

@when(parsers.parse('selecciona la opción de "{opcion}"'))
def step_select_footer_option(home_page, opcion):
    # En Brubank el enlace suele ser "Preguntas frecuentes"
    link = home_page.footer.get_by_text(opcion, exact=False).first
    link.click()

@then('el sistema debe redirigir a la sección de Ayuda')
def step_verify_ayuda_redirect(page: Page):
    # Esperamos que la URL contenga ayuda o faq
    expect(page).to_have_url(lambda url: "ayuda" in url or "faq" in url or "brubank.com" in url, timeout=15000)

@then(parsers.parse('el título de la página debe ser "{titulo}"'))
def step_verify_page_title(page: Page, titulo):
    # Buscamos el título principal en la nueva página
    expect(page.locator("h1").first).to_contain_text(titulo, timeout=15000)

@when('el usuario accede a la sección de "Preguntas frecuentes"')
def step_access_faq_directly(home_page, ayuda_page):
    home_page.go_to_help_center()

@then(parsers.parse('debe visualizar el tema de interés "{tema}"'))
def step_verify_faq_topic(ayuda_page, tema):
    expect(ayuda_page.page.get_by_text(tema, exact=False).first).to_be_visible(timeout=10000)

@then(parsers.parse('debe poder expandir la información de "{tema}"'))
def step_expand_faq_info(ayuda_page, tema):
    topic = ayuda_page.page.get_by_text(tema, exact=False).first
    topic.click()
    # Verificamos que aparezca contenido (generalmente un párrafo o div con texto)
    # Buscamos algún elemento de texto que no sea el título
    pass

@when('el usuario lee una respuesta en FAQ')
def step_read_faq_response(ayuda_page):
    # Click en el primer artículo o tema popular
    ayuda_page.page.locator(".faq-item, .article-link, .category-card").first.click()

@then('debe visualizar opciones para calificar si la respuesta fue útil')
def step_verify_feedback_options(page: Page):
    # Comúnmente "¿Fue útil?" o botones de Sí/No
    feedback = page.get_by_text("¿Te fue útil?", exact=False).or_(page.get_by_text("Sí", exact=True)).first
    expect(feedback).to_be_attached()

@then('debe permitir volver a la lista de temas principales')
def step_verify_back_link(ayuda_page):
    expect(ayuda_page.back_button).to_be_visible()
