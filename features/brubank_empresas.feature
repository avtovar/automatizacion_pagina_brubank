@regression @empresas
Feature: Suite de Regresión - Sección Empresas Brubank
  Como representante de una empresa o emprendimiento
  Quiero conocer las herramientas financieras que ofrece Brubank Empresas
  Para potenciar la gestión de mi negocio

  Background:
    Given que el usuario se encuentra en la sección de Empresas de Brubank

  @hero @branding
  Scenario: Verificar propuesta de valor principal para empresas
    Then el mensaje principal debe decir "Abrí tu cuenta empresa gratis"
    And debe visualizarse el botón para "Abrir cuenta" de empresa
    But no deben visualizarse secciones destinadas exclusivamente a individuos

  @productos @funcional
  Scenario Outline: Validar visibilidad de soluciones para negocios
    Then debe visualizarse la sección informativa de "<solucion>"
    And la información debe ser específica para el segmento corporativo

    Examples:
      | solucion         |
      | Cuenta Empresas  |
      | Pagos            |
      | Cobros           |
      | Inversiones      |
      | Tarjetas         |

  @interaccion @conversion
  Scenario: Verificar acceso a la apertura de cuenta corporativa
    When el usuario intenta iniciar el proceso de "Abrir cuenta"
    Then el sistema debe mostrar los requisitos para empresas
    And debe permitir la descarga de la documentación necesaria

  @footer @legal
  Scenario Outline: Verificar enlaces legales específicos para empresas
    Then el pie de página debe contener el enlace legal "<enlace>"
    
    Examples:
      | enlace                           |
      | Comisiones Vigentes Empresas     |
      | Información importante           |
      | Usuario Bancario                 |
