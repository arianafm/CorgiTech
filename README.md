
# MercadoEnLínea

El objetivo de MercadoEnLíea es poder comprar y vender artículos desde la comodidad de casa y minimizando riesgos ante la contingencia sanitaria global. Los compradores y vendedores podrán mostrar sus productos y ofertas sin la necesidad de estar en contacto físicamente. Todo desde casa.

## Características

  - El sistema será de compra/venta, así que, los usuarios del sistema pueden tanto vender como comprar productos.
  - Los usuarios del sistema deben de realizar un registro previo para acceder al sistema para poder vender o comprar productos.
  - Para realizar el registro, el sistema le solicitará los siguientes datos al usuario: nombre de usuario, correo y teléfono.
  - Una vez registrado el usuario, este recibirá un correo de confirmación que incluye la contraseña que le dará acceso al sistema.
  - El usuario tendrá que acceder al sistema para poder hacer uso de las funcionalidades, y cerrar la sesión al salir.
  - El vendedor podrá dar de alta los productos que desea vender, agregándole una breve descripción, foto y precio. Podrá actualizar su producto o si ya fue vendido eliminar la publicación de venta.
  - El comprador podrá consultar la lista de objetos en venta, revisar las opiniones de otros compradores y decidir lo que va a comprar. También podrá buscar algún producto en especial.
  - Cuando el comprador haya comprado algún artículo, recibirá un correo notificándole que compró un producto.
  - La interfaz de usuario es fácil de usar y entender.
  
## Dependencias
Se tiene que tener instalado cualquier versión de python, posteriormente, se tiene que tener las siguientes dependencias instaladas a través del manejador de paquetes `pip`.
 - cryptography
 -  flask
 - flask-marshmellow
 - flask-mail
 - flask_mail==0.9.0
 - flask_MailboxValidator
 - flask-msearch
 - flask-sqlalchemy
 - qrcode
 
## Ejecución del programa
 Se tiene que estar en el directorio 

> CorgiTech/PrimeraIteracion/src/

Una vez estando ahí, se ejecuta el comando

    flask run
Y listo, la página estará corriendo. Para acceder a ella basta con irse a cualquier navegador e introducir en la barra de navegación

    localhost:5000
 

##
Desarrollado por el equipo Corgitech. 
