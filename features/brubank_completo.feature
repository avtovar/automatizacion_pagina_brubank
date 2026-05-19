# language: es
@regresion @ui
Característica: Suite de Regresión Integral - Portal Brubank
  Como usuario del ecosistema financiero de Brubank
  Quiero navegar por la plataforma de manera fluida
  Para conocer los productos, servicios y soporte disponibles

  Antecedentes:
    Dado que el usuario se encuentra en la página de inicio de Brubank

  @navegacion @critico
  Esquema del escenario: Validar disponibilidad de opciones en el menú superior
    Entonces el menú de navegación debe mostrar la opción "<opcion>"
    
    Ejemplos:
      | opcion   |
      | Personas |
      | Empresas |
      | Ayuda    |
      | Ingresar |

  @hero @branding
  Escenario: Verificar identidad de marca y mensaje principal en el Hero
    Entonces el mensaje principal debe comunicar "El banco digital más grande de Argentina"
    Y deben estar disponibles los enlaces de descarga para tiendas de aplicaciones móviles

  @productos @funcional
  Esquema del escenario: Validar visibilidad de secciones de productos y servicios
    Entonces debe visualizarse la sección informativa de "<producto>"
    
    Ejemplos:
      | producto              |
      | Préstamos y adelantos |
      | Transferencias        |
      | Pago de servicios     |
      | Inversiones           |
      | Seguridad             |
      | Beneficios            |

  @personas @funcional
  Esquema del escenario: Explorar el catálogo de servicios para Personas
    Cuando el usuario explora el menú "Personas"
    Entonces debe visualizarse el acceso directo a "<servicio>"
    
    Ejemplos:
      | servicio              |
      | Cuenta                |
      | Tarjeta Visa          |
      | Préstamos             |
      | Inversiones           |
      | Dólar                 |
      | Pago QR               |
      | Brubank Plus          |
      | Control Parental      |

  @footer @legal @cumplimiento
  Esquema del escenario: Verificar integridad de enlaces legales en el pie de página
    Entonces el pie de página debe contener el enlace legal "<enlace_legal>"
    
    Ejemplos:
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

  @redes @branding
  Esquema del escenario: Verificar presencia en redes sociales oficiales
    Entonces debe estar visible el acceso a la red social "<red_social>"
    
    Ejemplos:
      | red_social |
      | Instagram  |
      | Facebook   |
      | Twitter    |
      | LinkedIn   |

  @soporte @ayuda
  Esquema del escenario: Validar categorías principales en el Centro de Ayuda
    Cuando el usuario accede al Centro de Ayuda
    Entonces debe visualizarse la categoría de soporte "<categoria>"
    
    Ejemplos:
      | categoria          |
      | Mi Cuenta          |
      | Tarjeta            |
      | Seguridad          |
      | Estafas            |
      | Límites y Costos   |
