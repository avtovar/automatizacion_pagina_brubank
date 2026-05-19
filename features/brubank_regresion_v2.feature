@regression @ui
Feature: Suite de Regresión Integral v2.2 - Portal Brubank
  Como usuario del ecosistema financiero de Brubank
  Quiero navegar por la plataforma de manera fluida y acceder a información clara
  Para gestionar mis finanzas de forma segura y eficiente

  Background:
    Given que el usuario se encuentra en la página de inicio de Brubank

  @navigation @critical
  Scenario Outline: Validar disponibilidad de opciones en el menú superior
    Then el menú de navegación debe mostrar la opción "<opcion>"
    And la opción debe estar habilitada para su interacción

    Examples:
      | opcion   |
      | Personas |
      | Empresas |
      | Ayuda    |
      | Ingresar |

  @hero @branding
  Scenario: Verificar identidad de marca y mensaje principal en la sección Hero
    Then el mensaje principal debe comunicar "El banco digital más grande de Argentina"
    And deben estar disponibles los enlaces de descarga para tiendas de aplicaciones móviles
    But no deben visualizarse mensajes de error de carga en la sección

  @productos @funcional
  Scenario Outline: Validar visibilidad de secciones informativas de productos
    Then debe visualizarse la sección informativa de "<producto>"
    And la sección debe contener información relevante para el usuario

    Examples:
      | producto              |
      | Préstamos y adelantos |
      | Transferencias        |
      | Pago de servicios     |
      | Inversiones           |
      | Seguridad             |
      | Beneficios            |

  @personas @submenu
  Scenario Outline: Explorar el catálogo de servicios detallados para Personas
    When el usuario explora el menú "Personas"
    Then debe visualizarse el acceso directo a "<servicio>"
    And el enlace debe redirigir a la sección correspondiente de "<servicio>"

    Examples:
      | service              |
      | Cuenta                |
      | Tarjeta Visa          |
      | Préstamos             |
      | Inversiones           |
      | Dólar                 |
      | Pago QR               |
      | Brubank Plus          |
      | Control Parental      |

  @footer @legal @compliance
  Scenario Outline: Verificar integridad de enlaces legales y transparencia
    Then el pie de página debe contener el enlace legal "<enlace_legal>"
    And al hacer clic debe mostrar la información de cumplimiento vigente

    Examples:
      | enlace_legal                     |
      | Términos y condiciones           |
      | Privacidad                       |
      | Defensa del Consumidor           |
      | Usuario de Servicios Financieros |
      | Código de Prácticas Bancarias    |
      | FATCA                            |
      | CRS                              |
      | Comisiones                       |
      | Comparativa                      |
      | Ayuda                            |

  @social @branding
  Scenario Outline: Verificar presencia en redes sociales oficiales de la marca
    Then debe estar visible el acceso a la red social "<red_social>"
    And el icono debe representar fielmente la identidad de "<red_social>"

    Examples:
      | red_social |
      | Instagram  |
      | Facebook   |
      | Twitter    |
      | LinkedIn   |

  @support @help
  Scenario Outline: Validar categorías de soporte en el Centro de Ayuda
    When el usuario accede al Centro de Ayuda
    Then debe visualizarse la categoría de soporte "<categoria>"
    And debe permitir la navegación hacia las preguntas frecuentes de "<categoria>"

    Examples:
      | categoria          |
      | Mi Cuenta          |
      | Tarjeta            |
      | Seguridad          |
      | Estafas            |
      | Límites y Costos   |
      | Inversiones        |
