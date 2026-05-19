# language: es
Característica: Página de Inicio de Brubank
  Como usuario interesado en servicios bancarios digitales
  Quiero navegar por la página principal de Brubank
  Para conocer los productos y servicios disponibles

  Antecedentes:
    Dado que el usuario accede a la página de Brubank

  Escenario: Verificar el logo de Brubank en el encabezado
    Entonces el logo de Brubank debe ser visible en el encabezado

  Escenario: Verificar el título principal en el Hero
    Entonces el título principal debe contener "EL BANCO DIGITAL MÁS GRANDE DE ARGENTINA"

  Escenario: Verificar el botón de descarga de la app en el Hero
    Entonces el botón para descargar la app debe estar presente en el hero

  Esquema del escenario: Verificación de ítems del menú principal
    Entonces el ítem de navegación "<item>" debe ser visible
    Ejemplos:
      | item     |
      | Personas |
      | Empresas |
      | Ayuda    |

  Esquema del escenario: Verificación de opciones del submenú Personas
    Cuando el usuario expande el menú de "Personas"
    Entonces debe ver la opción "<opcion>"
    Ejemplos:
      | opcion                |
      | Préstamos y adelantos |
      | Pago QR               |
      | Inversiones           |
      | Tarjeta               |
      | Cuentas               |
      | Transferencias        |

  Esquema del escenario: Verificación de opciones del submenú Empresas
    Cuando el usuario expande el menú de "Empresas"
    Entonces debe ver la opción "<opcion>"
    Ejemplos:
      | opcion            |
      | Brubank Business  |
      | Cobros con QR     |
      | Pago a proveedores|

  Esquema del escenario: Verificación de secciones de productos en la página de inicio
    Entonces la sección de "<seccion>" debe ser visible
    Ejemplos:
      | seccion        |
      | Préstamos      |
      | Transferencias |
      | Pagos          |
      | Inversiones    |
      | Seguridad      |
      | Beneficios     |
      | Dólar          |
      | BCRA           |
      | FAQ            |

  Esquema del escenario: Verificación de redes sociales en el pie de página
    Entonces el enlace a la red social "<red>" debe estar presente
    Ejemplos:
      | red       |
      | Instagram |
      | Facebook  |
      | Twitter   |
      | LinkedIn  |

  Esquema del escenario: Verificación de enlaces legales en el pie de página
    Entonces el enlace legal "<enlace>" debe ser visible
    Ejemplos:
      | enlace                            |
      | Información importante            |
      | Información al usuario financiero |
      | Defensa del consumidor            |
      | Contrato de adhesión              |
      | Régimen de transparencia          |
      | Código de ética                   |

  Esquema del escenario: Verificación de links de productos en el footer
    Entonces el link de producto "<producto>" debe estar en el footer
    Ejemplos:
      | producto   |
      | Préstamos  |
      | Inversiones|
      | Tarjetas   |
      | Cuentas    |
      | Seguros    |

  Escenario: Verificar el enlace a todas las preguntas en la sección FAQ
    Entonces el botón para ver todas las preguntas frecuentes debe estar presente
