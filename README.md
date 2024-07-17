# Red Social con API REST usando Django Rest Framework

Esta es una API REST desarrollada con Django Rest Framework (DRF) para una red social. La API permite a los usuarios registrarse, iniciar sesión y realizar diversas acciones en la plataforma. El proyecto incorpora un modelo de usuario personalizado que incluye campos como imagen de perfil y biografía. La autenticación está habilitada mediante JWT (JSON Web Token), proporcionando una capa de seguridad para las transacciones. Además, se ha implementado la paginación para optimizar la visualización de resultados.

## Características Principales

- **Registro y Autenticación:** Los usuarios pueden registrarse en la plataforma proporcionando información básica. El sistema implementa autenticación basada en JWT para garantizar la seguridad de las transacciones. Se generan tokens de acceso que permiten a los usuarios autenticados realizar acciones específicas.

- **Usuarios:** La API permite listar usuarios registrados y obtener información sobre ellos. Cada usuario tiene un perfil que incluye detalles como biografía e imagen de perfil.

- **Publicaciones:** Los usuarios autenticados pueden crear, editar y eliminar sus propias publicaciones. Además, pueden acceder a la lista completa de publicaciones disponibles en la plataforma.

- **Comentarios en Publicaciones:** Los usuarios pueden agregar comentarios a las publicaciones existentes, editarlos y eliminarlos. Los endpoints de los comentarios están anidados en los endpoints de las publicaciones, lo que permite una interacción fluida.

- **Permisos Personalizados:** Se han implementado permisos personalizados para controlar el acceso a las acciones. Los usuarios autenticados tienen privilegios para crear, editar y eliminar sus propias publicaciones y comentarios. Todos los usuarios, autenticados o no, pueden visualizar todas las publicaciones y comentarios en la plataforma.

- **Interacción Social:** Se ha agregado la funcionalidad de "me gusta" a las publicaciones. Los usuarios pueden dar y quitar "me gusta" a las publicaciones de otros usuarios.

- **Pruebas Unitarias:** Se realizaron pruebas unitarias exhaustivas utilizando pytest en los modelos y ViewSets de todas las aplicaciones para garantizar su funcionalidad y detectar posibles problemas.

- **Paginación:** La API utiliza la paginación para mejorar la experiencia del usuario al visualizar listas de usuarios, publicaciones y comentarios. Esto permite cargar resultados de manera eficiente y mejorar el rendimiento en casos de conjuntos de datos grandes.

## Instalación y Uso

1. Clona este repositorio en tu máquina local.
2. Crea y activa un entorno virtual.
3. Instala las dependencias utilizando `pip install -r requirements.txt`.
4. Configura la base de datos y migra los modelos con `python manage.py makemigrations` y `python manage.py migrate`.
5. Crea un superusuario para acceder al panel de administración con `python manage.py createsuperuser`.
6. Inicia el servidor de desarrollo con `python manage.py runserver`.
7. Accede a la API en `http://localhost:8000/api/`.
