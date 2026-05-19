# Gherkin Best Practices (QA Expert)

## 1. Declarative vs Imperative
**Imperative (Avoid):**
```gherkin
Given I click on the login button
And I enter "user" in the username field
And I click "Submit"
```

**Declarative (Preferred):**
```gherkin
Given I am logged in as a standard user
```

## 2. One Assertion per Scenario
Each scenario should ideally verify one business outcome. Use `Then` for the primary outcome.

## 3. Scenario Outlines
Use them for data-driven tests:
```gherkin
Esquema del escenario: Validar navegación por secciones
  Dado que estoy en la página de inicio
  Cuando accedo a la sección "<seccion>"
  Entonces visualizo el título "<titulo>"

  Ejemplos:
    | seccion | titulo    |
    | Ayuda   | ¿Cómo te podemos ayudar? |
    | Empresas| Brubank para empresas |
```

## 4. Rule of Three
If you have more than 3 `And` steps, consider if the scenario is too technical or needs a higher level of abstraction.
