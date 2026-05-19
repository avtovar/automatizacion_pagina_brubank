# Python Testing Patterns (Pytest & Playwright)

## 1. Page Object Model (POM)
- Keep locators private or encapsulated in methods.
- Use `expect` from `playwright.sync_api` for auto-retrying assertions.

## 2. Fixtures
- Use `conftest.py` for shared fixtures.
- Scope fixtures appropriately (session, function).

## 3. Pytest-BDD Integration
- Use `@scenario` or `scenarios()` to link features.
- Keep step definitions clean by delegating logic to POM.

## 4. Reporting
- Integrate `pytest-html` or `allure` for professional reports.
