from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.hero_section = page.locator(".section--hero")
        self.bcra_section = page.locator(".planeta-padding")
        self.dolar_section = page.locator(".section-light").first
        self.loans_section = page.locator("#creditos-adelantos")
        self.transfers_section = page.locator("#transferencia")
        self.payments_section = page.locator("#pago-de-servicio")
        self.investments_section = page.locator("#dolar-ahorro")
        self.security_section = page.locator('[id="24-7"]')
        self.benefits_section = page.locator(".section--inversiones.light-bg")
        self.footer = page.locator("footer, .footer-column-section")
        
        # Menu items
        self.personas_menu = page.get_by_text("Personas", exact=True).first
        self.empresas_menu = page.get_by_text("Empresas", exact=True).first
        self.ayuda_menu = page.get_by_text("Ayuda", exact=True).first
        
        # New locators for sub-items
        self.item_prestamos = page.get_by_role("link", name="Préstamos y adelantos").first
        self.item_pago_qr = page.get_by_role("link", name="Pago QR").first
        self.faq_section = page.locator('.section-title-wrapper').filter(has_text="Preguntas frecuentes").first

    def goto(self):
        self.page.set_viewport_size({"width": 1280, "height": 800})
        self.page.goto("https://www.brubank.com")
        self.page.wait_for_load_state("networkidle")

    def open_personas_menu(self):
        # Hover first to see if it triggers visibility
        self.personas_menu.hover()
        # If it needs a click, dispatch it if it's "hidden" but interactable
        self.personas_menu.dispatch_event("click")
        # Wait for the item to be visible instead of a fixed timeout
        self.item_prestamos.wait_for(state="visible", timeout=5000)

    def verify_navigation_menu(self):
        expect(self.personas_menu).to_be_attached()
        expect(self.empresas_menu).to_be_attached()
        expect(self.ayuda_menu).to_be_attached()

    def verify_hero_section(self):
        expect(self.hero_section).to_be_visible()
        expect(self.hero_section).to_contain_text("El banco digital más grande de Argentina")

    def verify_personas_items(self):
        self.open_personas_menu()
        expect(self.item_prestamos).to_be_visible()
        expect(self.item_pago_qr).to_be_visible()

    def verify_footer(self):
        expect(self.footer.first).to_be_visible()
        expect(self.page.locator(".footer-column-section").get_by_text("Información importante")).to_be_visible()
