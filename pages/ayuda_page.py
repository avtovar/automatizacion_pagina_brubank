from playwright.sync_api import Page, expect
import logging
from typing import Optional

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
        self.page.goto("https://www.brubank.com", wait_until="domcontentloaded", timeout=60000)
        self.page.wait_for_selector("body")
        ayuda_link = self.page.get_by_role("link", name="Ayuda").first
        if ayuda_link.is_visible(timeout=5000):
            ayuda_link.click()

    def search_for(self, term: str):
        logger.info(f"Buscando término: {term}")
        if self.search_input.is_visible(timeout=3000):
            self.search_input.fill(term)
            self.page.keyboard.press("Enter")
            self.page.wait_for_load_state("domcontentloaded")
        else:
            body = (self.page.locator("body").inner_text(timeout=15000) or "").casefold()
            assert term.casefold() in body, f"No se encontró {term!r} en el contenido de ayuda visible"

    def verify_search_results_visible(self, term: Optional[str] = None):
        if self.search_results.count():
            expect(self.search_results.first).to_be_visible(timeout=15000)
        else:
            expect(self.page.locator("body")).to_be_visible(timeout=15000)
        if term:
            body = (self.page.locator("body").inner_text(timeout=15000) or "").casefold()
            assert term.casefold() in body, f"No se encontró {term!r} en los resultados visibles"

    def select_category(self, category_name: str):
        logger.info(f"Seleccionando categoría: {category_name}")
        matches = self.page.get_by_text(category_name, exact=False)
        locator = matches.filter(visible=True).first if matches.count() else matches.first
        locator.scroll_into_view_if_needed(timeout=10000)
        expect(locator).to_be_visible(timeout=10000)
        locator.click()
        self.page.wait_for_load_state("domcontentloaded")

    def verify_faq_article_loaded(self, expected_title: str):
        expect(self.faq_article_title).to_be_visible(timeout=20000)
        if expected_title:
            expect(self.faq_article_title).to_contain_text(expected_title)
        text = (self.page.locator("body").inner_text(timeout=10000) or "").strip()
        assert len(text) >= 100, "El artículo o categoría no muestra contenido legible suficiente"

    def go_back(self):
        self.back_button.scroll_into_view_if_needed()
        self.back_button.click()
        self.page.wait_for_load_state("domcontentloaded")

    def verify_back_navigation_available(self):
        if self.back_button.count():
            expect(self.back_button).to_be_attached(timeout=10000)
        else:
            expect(self.page.get_by_text("Preguntas frecuentes", exact=False).first).to_be_visible(timeout=10000)
