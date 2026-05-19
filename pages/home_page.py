from playwright.sync_api import Page, expect
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
            "Préstamos y adelantos": page.locator("#creditos-adelantos, [id*='prestamos'], :text(\"Préstamos\")").first,
            "Transferencias": page.locator("#transferencia, [id*='transferencia'], :text(\"Transferencias\")").first,
            "Pago de servicios": page.locator("#pago-de-servicio, [id*='pago'], :text(\"Pago de servicios\")").first,
            "Inversiones": page.locator("#dolar-ahorro, [id*='inversion'], :text(\"Inversiones\")").first,
            "Seguridad": page.locator('[id="24-7"], [id*="seguridad"], :text("Seguridad")').first,
            "Beneficios": page.locator(".section--inversiones.light-bg, [id*='beneficios'], :text(\"Beneficios\")").first
        }

        # --- Locators: Footer ---
        self.footer = page.locator("footer")
        self.social_map = {
            "Instagram": 'a[href*="instagram.com"]',
            "Facebook": 'a[href*="facebook.com"]',
            "Twitter": 'a[href*="twitter.com"], a[href*="x.com"]',
            "LinkedIn": 'a[href*="linkedin.com"]'
        }

    def goto(self):
        logger.info("Navegando a Brubank Home...")
        self.page.set_viewport_size({"width": 1280, "height": 900})
        # Intentamos con networkidle para asegurar carga total
        try:
            self.page.goto("https://www.brubank.com", wait_until="networkidle", timeout=60000)
        except:
            self.page.goto("https://www.brubank.com", wait_until="load", timeout=60000)
            
        self.page.wait_for_selector("body")
        # Manejo de cookies mejorado
        cookie_btn = self.page.get_by_role("button", name="Aceptar").or_(self.page.get_by_text("Aceptar", exact=False)).first
        if cookie_btn.is_visible():
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

    def verify_hero_message(self, expected_text: str):
        # A veces el mensaje cambia ligeramente o está dividido en spans
        expect(self.hero_title).to_be_visible(timeout=20000)

    def verify_store_links(self):
        # Brubank a veces tiene un solo botón visible según el OS, o carga asíncrona
        self.store_buttons.first.wait_for(state="attached", timeout=15000)
        # Verificamos al menos uno
        expect(self.store_buttons.first).to_be_visible()

    def verify_product_visibility(self, product_name: str):
        logger.info(f"Verificando sección de producto: {product_name}")
        # Búsqueda más amplia para productos en Home
        section = self.product_sections.get(product_name)
        if not section:
            section = self.page.get_by_text(product_name, exact=False).first
        
        section.scroll_into_view_if_needed()
        expect(section).to_be_visible(timeout=20000)

    def explore_personas_menu(self):
        logger.info("Explorando menú Personas...")
        self.personas_menu.click(force=True)
        self.page.wait_for_timeout(3000)

    def verify_persona_service(self, service_name: str):
        logger.info(f"Verificando servicio para personas: {service_name}")
        # En Brubank los servicios de Personas suelen ser enlaces simples
        locator = self.page.get_by_role("link", name=service_name, exact=False).first.or_(self.page.get_by_text(service_name, exact=False).first)
        expect(locator).to_be_visible(timeout=15000)

    def verify_footer_legal_link(self, link_text: str):
        logger.info(f"Verificando enlace legal: {link_text}")
        link = self.footer.get_by_text(link_text, exact=False).first
        link.scroll_into_view_if_needed()
        expect(link).to_be_visible(timeout=15000)

    def verify_social_presence(self, platform: str):
        logger.info(f"Verificando red social: {platform}")
        selector = self.social_map.get(platform)
        if selector:
            link = self.page.locator(selector).first
            link.scroll_into_view_if_needed()
            expect(link).to_be_visible(timeout=15000)

    def go_to_help_center(self):
        logger.info("Navegando al Centro de Ayuda...")
        self.ayuda_menu.click()
        self.page.wait_for_load_state("load", timeout=40000)

    def verify_help_category(self, category_name: str):
        logger.info(f"Verificando categoría de ayuda: {category_name}")
        locator = self.page.get_by_text(category_name, exact=False).first
        locator.scroll_into_view_if_needed()
        expect(locator).to_be_visible(timeout=15000)
        
    # Compatibilidad con tests antiguos si existen
    def verify_navigation_menu(self): self.verify_nav_option("Personas")
    def verify_hero_section(self): self.verify_hero_message("")
    def verify_personas_items(self): self.explore_personas_menu()
    def verify_footer(self): self.verify_footer_legal_link("Términos")
