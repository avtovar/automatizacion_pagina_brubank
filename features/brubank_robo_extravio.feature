@regression @seguridad @critico
Feature: Robo y Extravío - Brubank Support
  As a user who lost their card or had it stolen
  I want to find the instructions to report it quickly
  To protect my money and account

  Background:
    Given que el usuario se encuentra en el Centro de Ayuda de Brubank

  @emergencia @funcional
  Scenario: Buscar información de reporte por robo o extravío
    When el usuario busca el término "Robo y extravío"
    Then el sistema debe mostrar resultados relacionados con "Robo y extravío"
    And debe ser visible el artículo principal sobre "robo o extravío"

  @navegacion @seguridad
  Scenario: Acceder directamente desde la categoría Seguridad
    When el usuario selecciona la categoría "Seguridad"
    Then debe visualizarse la opción de "Denunciar robo o extravío"
    And el contenido debe explicar cómo bloquear la tarjeta desde la app
