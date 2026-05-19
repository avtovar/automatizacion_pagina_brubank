@regression @faq
Feature: Preguntas Frecuentes (FAQ) - Brubank Portal
  As a user with common doubts
  I want to access the FAQ section from different entry points
  To quickly find answers without contacting support

  Background:
    Given que el usuario se encuentra en la página de inicio de Brubank

  @navegacion @footer
  Scenario: Acceder a FAQ desde el pie de página
    When el usuario navega hasta el pie de página
    And selecciona la opción de "Preguntas frecuentes"
    Then el sistema debe redirigir a la sección de Ayuda
    And el título de la página debe ser "Preguntas frecuentes"

  @busqueda @funcional
  Scenario Outline: Validar acceso a temas populares en FAQ
    When el usuario accede a la sección de "Preguntas frecuentes"
    Then debe visualizar el tema de interés "<tema>"
    And debe poder expandir la información de "<tema>"

    Examples:
      | tema             |
      | Abrir mi cuenta  |
      | Mi tarjeta       |
      | Transferencias   |
      | Plazo Fijo       |
      | Préstamos        |

  @interaccion
  Scenario: Validar utilidad de las respuestas
    When el usuario lee una respuesta en FAQ
    Then debe visualizar opciones para calificar si la respuesta fue útil
    And debe permitir volver a la lista de temas principales
