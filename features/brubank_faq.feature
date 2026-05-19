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
      | abrir una cuenta |
      | beneficios tiene la tarjeta |
      | pagar sin usar la tarjeta |
      | pagar servicios |

  @interaccion
  Scenario: Validar lectura de respuestas frecuentes
    When el usuario lee una respuesta en FAQ
    Then debe visualizar el contenido de la respuesta
    And debe permitir volver a la lista de temas principales
