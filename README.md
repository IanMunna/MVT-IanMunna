# Proyecto_Final1
Miembros: Ian Munna Fourcade.

<----- Guia de uso ---->

-El primer paso es crear una base de datos. Para eso usaremos los siguientes comandos:

*Python manage.py migrate*
*Python manage.py makemigrations*
 
-Una vez ejecutado el comando 'python manage.py runserver' y dirigirnos a la web (generalmente usaremos la url 'http://127.0.0.1:8000/') tendremos las siguientes opciones:

-Dentro de la web podremos realizar diferentes acciones mediante los siguientes comandos (los cuales ingresaremos en nuestra url):

'admin/': agregando este a la url podremos ingresar a la interface de administrador de Django; donde podemos administras los usuarios con sus respectivos permisos y tambien podremos agrerar a nuestra base de datos nuevos 'familiares/mascotas/hogares'.
'AppMvt/': agregando este a la url seremos redirigidos a la pagina de inicio de la web; en esta encontraremos apartados correspondientes a los models creados.
'familiarFormulario/': agregando este a la url seremos redirigidos al apartado de creacion de 'familiares' (mediante un formulario) y una vez finalizado este nos redirigira al inicio de la web.
'busquedaFamiliar/': agregando este a la url seremos redirigidos al apartado de busqueda de 'familiares' (mediante un formulario se buscara en la base de datos los posibles resultados de busqueda) y luego de enseñarlo nos rediriga al inicio de la web.









