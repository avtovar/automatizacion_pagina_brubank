from playwright.sync_api import Page, expect
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AyudaPage:
    def __init__(self, page: Page):
        self.page = page
        
        # --- Locators: Search ---
        self.search_input = page.get_by_placeholder("¿Cómo podemos ayudarte?").or_(page.locator("input[type='search']")).first
        self.search_results = page.locator(".search-results, .faq-list, .section-content")

        # --- Locators: Categories ---
        self.categories = {
            "Mi Cuenta": page.get_by_text("Mi Cuenta").first,
            "Tarjeta": page.get_by_text("Tarjeta", exact=True).first,
            "Seguridad": page.get_by_text("Seguridad").first,
            "Inversiones": page.get_by_text("Inversiones").first,
            "Préstamos": page.get_by_text("Préstamos").first
        }

        # --- Locators: FAQ Items ---
        self.faq_article_title = page.locator("h1, .article-title, .section-title").first
        self.back_button = page.get_by_role("link", name="Volver").or_(page.get_by_text("Volver")).first

    def goto(self):
        logger.info("Navegando al Centro de Ayuda de Brubank...")
        # Ayuda suele estar en un subdominio o carpeta, nos aseguramos de ir a la URL correcta
        self.page.goto("https://www.brubank.com/ayuda", wait_until="domcontentloaded", timeout=60000)
        self.page.wait_for_selector("body")

    def search_for(self, term: str):
        logger.info(f"Buscando término: {term}")
        # Aseguramos visibilidad del input
        self.search_input.wait_for(state="visible", timeout=15000)
        self.search_input.fill(term)
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state("domcontentloaded")

    def verify_search_results_visible(self):
        # A veces los resultados tardan en renderizar
        self.page.wait_for_timeout(2000)
        expect(self.search_results.first).to_be_visible(timeout=15000)

    def select_category(self, category_name: str):
        logger.info(f"Seleccionando categoría: {category_name}")
        locator = self.page.get_by_text(category_name, exact=False).first
        locator.scroll_into_view_if_needed(timeout=10000)
        locator.click(force=True)
        self.page.wait_for_load_state("domcontentloaded")

    def verify_faq_article_loaded(self, expected_title: str):
        expect(self.faq_article_title).to_be_visible(timeout=20000)
        if expected_title:
            expect(self.faq_article_title).to_contain_text(expected_title)

    def go_back(self):
        self.back_button.scroll_into_view_if_needed()
        self.back_button.click()
        self.page.wait_for_load_state("domcontentloaded")
