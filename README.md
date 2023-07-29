El archivo tiene asociado un archivo requirements con todos los paquetes necesarios por lo cual solo se debe ejecutar un pip install -r requirements.txt y agregar 'django_extensions' en settings INSTALLED_APP

Funciones de la App:

#Home: Landing de bienvenida que muestra información general de la página y desde el cual se puede acceder al nav donde estan almacenadas las demas funciones.
#Mostrar Usuario: Permite visualizar todos los usuarios creados en nuestra app como tarjetas junto con sus datos (Nombre, Apellido, Rut, Correo y fecha de registro).
#Mensaje Proveedor: Permite a posibles proveedores dejar sus datos junto con un comentario para ser almacenados en una base de datos.
#Registro: Función encargada de crear nuevos usuarios, esta pide todos los datos solicitados por la estructura de user establacida de django, además, se agrega logica para que al crear usuario quede logeado con la cuenta creada.
#LogIn: Permite a los usuarios ya registrados acceder al sitio web, la logica del codigo solicita como username el correo del usuario.
#LogOut: Función para poder cerrar la sesión del usuario actual.