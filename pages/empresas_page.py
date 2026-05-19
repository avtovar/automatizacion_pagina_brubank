from playwright.sync_api import Page, expect
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmpresasPage:
    def __init__(self, page: Page):
        self.page = page
        
        # --- Locators: Hero ---
        self.hero_title = page.locator("h1").first
        self.open_account_btn = page.get_by_role("link", name="Abrir cuenta", exact=False).filter(visible=True).first

        # --- Locators: Product Sections (Empresas) ---
        self.sections = {
            "Cuenta Empresas": page.get_by_text("Una cuenta pensada", exact=False),
            "Pagos": page.get_by_text("Pagá todo lo que necesitás", exact=False),
            "Cobros": page.get_by_text("Cobrá tus ventas", exact=False),
            "Inversiones": page.get_by_text("Invertí y rescatá", exact=False),
            "Tarjetas": page.get_by_text("tarjeta de crédito corporativa", exact=False)
        }

    def goto(self):
        logger.info("Navegando a Brubank Empresas...")
        self.page.goto("https://www.brubank.com/empresas", wait_until="domcontentloaded", timeout=60000)
        self.page.wait_for_selector("body")

    def verify_hero_title(self, expected_text: str):
        expect(self.hero_title).to_be_visible(timeout=20000)
        if expected_text:
            actual = " ".join((self.hero_title.inner_text(timeout=10000) or "").casefold().split())
            expected = " ".join(expected_text.casefold().split())
            assert expected in actual, f"Hero Empresas esperado: {expected_text!r}. Hero actual: {actual!r}"

    def verify_section_visibility(self, section_name: str):
        logger.info(f"Verificando sección Empresas: {section_name}")
        locator = self.sections.get(section_name)
        if not locator:
            locator = self.page.get_by_text(section_name, exact=False).first
        if locator.count():
            locator = locator.filter(visible=True).first
        
        locator.scroll_into_view_if_needed(timeout=10000)
        expect(locator).to_be_visible(timeout=15000)
        text = (locator.inner_text(timeout=10000) or "").strip()
        assert len(text) >= 10, f"La sección {section_name!r} tiene poco contenido visible"

    def verify_open_account_button(self):
        expect(self.open_account_btn).to_be_visible(timeout=15000)
        assert self.open_account_btn.get_attribute("href") or self.open_account_btn.is_enabled(), "El botón Abrir cuenta no tiene destino ni está habilitado"

    def verify_no_individual_only_sections(self):
        individual_only = self.page.get_by_text("Cuenta para menores", exact=False).or_(
            self.page.get_by_text("Control Parental", exact=False)
        )
        assert individual_only.count() == 0, "La página Empresas muestra secciones exclusivas para individuos"

    def verify_corporate_content(self):
        body = (self.page.locator("body").inner_text(timeout=10000) or "").casefold()
        assert any(term in body for term in ("empresa", "negocio", "corporativa", "proveedores")), "No se detectó contenido específico para empresas"

    def verify_business_requirements_visible(self):
        body = (self.page.locator("body").inner_text(timeout=10000) or "").casefold()
        assert any(term in body for term in ("cuit", "empresa", "requisito", "document")), "No se detectaron requisitos o documentación para empresas"
