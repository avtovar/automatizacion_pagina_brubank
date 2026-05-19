import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect
from pages.empresas_page import EmpresasPage

# Cargar escenarios para la sección Empresas
scenarios('../features/brubank_empresas.feature')

@pytest.fixture(scope="function")
def empresas_page(page: Page):
    ep = EmpresasPage(page)
    ep.goto()
    return ep

# --- Step Definitions (English Keywords / Spanish Text) ---

@given('que el usuario se encuentra en la sección de Empresas de Brubank')
def step_user_is_on_empresas(empresas_page):
    assert "empresas" in empresas_page.page.url

@then(parsers.parse('el mensaje principal debe decir "{texto}"'))
def step_verify_hero_title(empresas_page, texto):
    # Brubank puede cambiar el texto exacto del H1, validamos visibilidad
    empresas_page.verify_hero_title(texto)

@then('debe visualizarse el botón para "Abrir cuenta" de empresa')
def step_verify_open_account_btn(empresas_page):
    empresas_page.verify_open_account_button()


@then('no deben visualizarse secciones destinadas exclusivamente a individuos')
def step_verify_no_individual_sections(empresas_page):
    empresas_page.verify_no_individual_only_sections()

@then(parsers.parse('debe visualizarse la sección informativa de "{solucion}"'))
def step_verify_section_visibility(empresas_page, solucion):
    empresas_page.verify_section_visibility(solucion)

@then('la información debe ser específica para el segmento corporativo')
def step_verify_corporate_info(empresas_page):
    empresas_page.verify_corporate_content()

@when('el usuario intenta iniciar el proceso de "Abrir cuenta"')
def step_click_open_account(empresas_page):
    empresas_page.open_account_btn.click()

@then('el sistema debe mostrar los requisitos para empresas')
def step_verify_requirements(empresas_page):
    empresas_page.verify_business_requirements_visible()

@then('debe permitir la descarga de la documentación necesaria')
def step_verify_doc_download(empresas_page):
    expect(empresas_page.page.locator("body")).to_contain_text("document", timeout=10000)

@then(parsers.parse('el pie de página debe contener el enlace legal "{enlace}"'))
def step_verify_footer_link(empresas_page, enlace):
    matches = empresas_page.page.get_by_text(enlace, exact=False)
    expect(matches.filter(visible=True).first).to_be_visible(timeout=10000)
