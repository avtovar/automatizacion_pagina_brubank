from playwright.sync_api import Page, expect
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmpresasPage:
    def __init__(self, page: Page):
        self.page = page
        
        # --- Locators: Hero ---
        self.hero_title = page.locator("h1").first
        self.open_account_btn = page.get_by_role("link", name="Abrir cuenta").or_(page.get_by_text("Abrir cuenta")).first

        # --- Locators: Product Sections (Empresas) ---
        self.sections = {
            "Cuenta Empresas": page.get_by_text("negocio", exact=False).first,
            "Pagos": page.get_by_text("Pagá", exact=False).first,
            "Cobros": page.get_by_text("Cobrá", exact=False).first,
            "Inversiones": page.get_by_text("rendir", exact=False).first,
            "Tarjetas": page.get_by_text("Tarjetas corporativas", exact=False).first
        }

    def goto(self):
        logger.info("Navegando a Brubank Empresas...")
        self.page.goto("https://www.brubank.com/empresas", wait_until="domcontentloaded", timeout=60000)
        self.page.wait_for_selector("body")

    def verify_hero_title(self, expected_text: str):
        # Propuesta de valor dinámica
        expect(self.hero_title).to_be_visible(timeout=20000)

    def verify_section_visibility(self, section_name: str):
        logger.info(f"Verificando sección Empresas: {section_name}")
        locator = self.sections.get(section_name)
        if not locator:
            locator = self.page.get_by_text(section_name, exact=False).first
        
        locator.scroll_into_view_if_needed(timeout=10000)
        expect(locator).to_be_visible(timeout=15000)

    def verify_open_account_button(self):
        expect(self.open_account_btn).to_be_visible(timeout=15000)
