@regression @ayuda
Feature: Suite de Regresión - Centro de Ayuda Brubank
  Como usuario que necesita soporte o información
  I want to browse the help center and search for solutions
  Para resolver mis dudas de forma autónoma

  Background:
    Given que el usuario se encuentra en el Centro de Ayuda de Brubank

  @busqueda @funcional
  Scenario Outline: Buscar soluciones en la base de conocimientos
    When el usuario busca el término "<termino>"
    Then el sistema debe mostrar resultados relacionados con "<termino>"
    And los resultados deben ser relevantes para la consulta

    Examples:
      | termino    |
      | Tarjeta    |
      | Clave      |
      | Transferencias |

  @categorias @navegacion
  Scenario Outline: Explorar categorías principales de ayuda
    When el usuario selecciona la categoría "<categoria>"
    Then se deben visualizar los artículos frecuentes de "<categoria>"
    And la navegación debe ser fluida dentro de la sección

    Examples:
      | categoria   |
      | Transferencias |
      | Tarjetas    |
      | Préstamos   |
      | Inversiones |

  @articulos @funcional
  Scenario: Visualizar detalle de un artículo de ayuda
    When el usuario accede a un artículo de soporte
    Then el contenido completo del artículo debe ser legible
    And debe permitir volver a la página de categorías principal
