from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, expect
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        
        # --- Locators: Header ---
        self.nav_menu = page.locator("nav")
        self.personas_menu = page.get_by_role("button", name="Personas").or_(page.get_by_text("Personas", exact=True)).first
        self.empresas_menu = page.get_by_role("button", name="Empresas").or_(page.get_by_text("Empresas", exact=True)).first
        self.ayuda_menu = page.get_by_role("link", name="Ayuda").or_(page.get_by_text("Ayuda", exact=True)).first
        # Brubank a veces usa 'Ingresar' o un icono
        self.login_button = page.get_by_role("link", name="Ingresar").or_(page.locator('a:has-text("Ingresar")')).first

        # --- Locators: Hero ---
        self.hero_title = page.locator("h1").first
        self.store_buttons = page.locator('a[href*="apple.com"], a[href*="google.com"]')

        # --- Locators: Products (Home) ---
        self.product_sections = {
            "Préstamos y adelantos": page.get_by_text("Adelantos y préstamos", exact=False).first,
            "Transferencias": page.get_by_text("Transferencias express", exact=False).first,
            "Pago de servicios": page.get_by_text("Pagá todos tus servicios", exact=False).first,
            "Inversiones": page.get_by_text("Inversiones inmediatas", exact=False).first,
            "Seguridad": page.get_by_text("seguridad biométrica", exact=False).first,
            "Beneficios": page.get_by_text("Con Brubank, ahorrá siempre", exact=False).first
        }

        # --- Locators: Footer ---
        self.footer = page.locator("footer")
        self.social_map = {
            "Instagram": 'a[href*="instagram.com"]',
            "TikTok": 'a[href*="tiktok.com"]',
            "Twitter": 'a[href*="twitter.com"], a[href*="x.com"]',
            "LinkedIn": 'a[href*="linkedin.com"]'
        }
        self.last_verified_locator = None

    def goto(self):
        logger.info("Navegando a Brubank Home...")
        self.page.set_viewport_size({"width": 1280, "height": 900})
        try:
            self.page.goto("https://www.brubank.com", wait_until="networkidle", timeout=60000)
        except PlaywrightTimeoutError:
            self.page.goto("https://www.brubank.com", wait_until="load", timeout=60000)
            
        self.page.wait_for_selector("body")
        cookie_btn = self.page.get_by_role("button", name="Aceptar").or_(self.page.get_by_text("Aceptar", exact=False)).first
        if cookie_btn.is_visible(timeout=3000):
            cookie_btn.click()

    def verify_nav_option(self, option_name: str):
        logger.info(f"Verificando opción de menú: {option_name}")
        mapping = {
            "Personas": self.personas_menu,
            "Empresas": self.empresas_menu,
            "Ayuda": self.ayuda_menu,
            "Ingresar": self.login_button
        }
        locator = mapping.get(option_name)
        if not locator:
            locator = self.page.get_by_text(option_name, exact=True).first
            
        # Esperamos a que el elemento sea interactuable
        locator.wait_for(state="attached", timeout=15000)
        expect(locator).to_be_visible(timeout=15000)
        self.last_verified_locator = locator

    def verify_last_nav_option_enabled(self):
        assert self.last_verified_locator is not None, "No hay una opción de navegación verificada previamente"
        expect(self.last_verified_locator).to_be_enabled(timeout=10000)

    def verify_hero_message(self, expected_text: str):
        expect(self.hero_title).to_be_visible(timeout=20000)
        if expected_text:
            actual = " ".join((self.hero_title.inner_text(timeout=10000) or "").casefold().split())
            expected = " ".join(expected_text.casefold().split())
            assert expected in actual, f"Hero esperado: {expected_text!r}. Hero actual: {actual!r}"

    def verify_store_links(self):
        visible_store_button = self.store_buttons.filter(visible=True).first
        visible_store_button.wait_for(state="visible", timeout=15000)
        assert visible_store_button.get_attribute("href"), "El enlace de descarga visible no tiene href"

    def verify_no_loading_errors(self):
        error_messages = self.page.get_by_text("error", exact=False).or_(
            self.page.get_by_text("no se pudo", exact=False)
        ).or_(self.page.get_by_text("404", exact=False))
        assert error_messages.count() == 0, "Se encontraron mensajes de error visibles o renderizados"

    def verify_product_visibility(self, product_name: str):
        logger.info(f"Verificando sección de producto: {product_name}")
        # Búsqueda más amplia para productos en Home
        section = self.product_sections.get(product_name)
        if not section:
            section = self.page.get_by_text(product_name, exact=False).first
        if section.count():
            section = section.filter(visible=True).first
        
        section.scroll_into_view_if_needed()
        expect(section).to_be_visible(timeout=20000)
        self.last_verified_locator = section

    def verify_last_section_has_relevant_text(self):
        assert self.last_verified_locator is not None, "No hay una sección verificada previamente"
        text = (self.last_verified_locator.inner_text(timeout=10000) or "").strip()
        assert len(text) >= 20, f"La sección tiene poco contenido visible: {text!r}"

    def explore_personas_menu(self):
        logger.info("Explorando menú Personas...")
        expect(self.personas_menu).to_be_visible(timeout=15000)
        self.personas_menu.click()
        expect(self.page.locator("body")).to_contain_text("Cuenta", timeout=15000)

    def verify_persona_service(self, service_name: str):
        logger.info(f"Verificando servicio para personas: {service_name}")
        locator = self.page.get_by_role("link", name=service_name, exact=False).first
        if locator.count() == 0:
            locator = self.page.get_by_text(service_name, exact=False).first
        expect(locator).to_be_visible(timeout=15000)
        self.last_verified_locator = locator

    def verify_last_link_has_destination(self):
        assert self.last_verified_locator is not None, "No hay un enlace verificado previamente"
        if self.last_verified_locator.evaluate("node => node.tagName.toLowerCase()") == "a":
            assert self.last_verified_locator.get_attribute("href"), "El enlace verificado no tiene href"

    def verify_footer_legal_link(self, link_text: str):
        logger.info(f"Verificando enlace legal: {link_text}")
        footer_scope = self.footer.first if self.footer.count() else self.page.locator("body")
        matches = footer_scope.get_by_text(link_text, exact=False)
        link = matches.filter(visible=True).first if matches.count() else matches.first
        link.scroll_into_view_if_needed()
        expect(link).to_be_visible(timeout=15000)
        self.last_verified_locator = link

    def verify_social_presence(self, platform: str):
        logger.info(f"Verificando red social: {platform}")
        selector = self.social_map.get(platform)
        if selector:
            link = self.page.locator(selector).first
            link.scroll_into_view_if_needed()
            expect(link).to_be_visible(timeout=15000)
            assert link.get_attribute("href"), f"El enlace social de {platform} no tiene href"
            self.last_verified_locator = link

    def go_to_help_center(self):
        logger.info("Navegando al Centro de Ayuda...")
        self.ayuda_menu.click()
        self.page.wait_for_load_state("load", timeout=40000)

    def verify_help_category(self, category_name: str):
        logger.info(f"Verificando categoría de ayuda: {category_name}")
        matches = self.page.get_by_text(category_name, exact=False)
        locator = matches.filter(visible=True).first if matches.count() else matches.first
        locator.scroll_into_view_if_needed()
        expect(locator).to_be_visible(timeout=15000)
        self.last_verified_locator = locator
        
    # Compatibilidad con tests antiguos si existen
    def verify_navigation_menu(self): self.verify_nav_option("Personas")
    def verify_hero_section(self): self.verify_hero_message("")
    def verify_personas_items(self): self.explore_personas_menu()
    def verify_footer(self): self.verify_footer_legal_link("Términos")
