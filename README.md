**Introducción**

Nuestro objetivo es ayudar a la escuela de baile Danza Fénix, dirigida por Mar, a modernizar su sistema de gestión de alumnos y cuentas mediante una herramienta digital. Crearemos una API que permitirá registrar, organizar y acceder a la información de manera más eficiente y segura. Con esta solución, Danza Fénix podrá dejar atrás el uso de papel y bolígrafo, ahorrando tiempo y evitando errores. Además, la API permitirá aplicar descuentos a los alumnos que traigan familiares y visualizar los inscritos en cada clase.

**Contexto y problemática que busca resolver la API y la base de datos.**

Danza Fénix enfrenta desafíos en la gestión de alumnos y cuentas debido a su sistema manual en papel y bolígrafo. Esto provoca problemas de organización, pérdida de información y un proceso laborioso para actualizar datos y aplicar descuentos. La API y la base de datos resuelven estos inconvenientes mediante una solución digital que facilita la gestión y garantiza la integridad de los datos.

**Descripción de las tecnologías utilizadas: FastAPI, MySQL, unittest, pydantic, uvicorn, swagger.**

Las tecnologías utilizadas en el desarrollo de la API y la base de datos son:

1. **FastAPI:** Framework moderno y de alto rendimiento para crear APIs web en Python, facilitando el diseño y desarrollo de APIs potentes y seguras.

2. **MySQL:** Sistema de gestión de bases de datos relacional ampliamente utilizado, empleado para almacenar y gestionar la información de alumnos, clases y cuentas.

3. **unittest:** Módulo de prueba unitaria en Python, utilizado para verificar que la API funciona correctamente, asegurando la calidad del software.

4. **pydantic:** Biblioteca que proporciona validación de datos y serialización de modelos en Python, garantizando que los datos cumplan con los requisitos establecidos.

5. **uvicorn:** Servidor ASGI que permite ejecutar aplicaciones web de manera asíncrona y de alto rendimiento, asegurando una excelente velocidad de respuesta.

6. **Swagger:** Herramienta para generar documentación interactiva de APIs web, proporcionando detalles sobre los endpoints y su funcionalidad.


**Requisitos previos para ejecutar el proyecto:**

1. Python: Instalar la versión Phyton 3.7 o superior

2. Gestor de paquetes de Python: Verificar la presencia de "pip" en el sistema.

3. Sistema de Gestión de Base de Datos: Instalar y configurar MySQL, con un usuario con privilegios para crear y gestionar bases de datos.

**Instrucciones para instalar las dependencias necesarias:**

1. Crear el entorno virtual desde la terminal o línea de comandos.

2. Dirigirse a la carpeta raíz del proyecto y ejecutar `pip install -r requirements.txt` para instalar las dependencias necesarias.

**Configuración de la base de datos (MySQL):**

1. Crear una nueva base de datos para el proyecto.

2. Modificar el archivo database_example.py con las credenciales de acceso a MySQL.
engine = create_engine("mysql+pymysql://UserExample:PasswordExample@localhost:3306/NombreBaseDatos")

3.Reemplazar las siguientes partes del engine:

- UserExample
- PasswordExample
- NombreBaseDatos


**Estructura del Proyecto**

1. "database_initialized.txt": archivo que se crea cuando se guardan los datos de fenix_example.py en la base de datos

2. "main.py": Archivo principal para iniciar la API y conectarse a la base de datos.

3. "models/": Carpeta con archivos que definen la estructura de datos en la base de datos (alumnos, clases, profesores etc).

4. "schemas/": Carpeta con archivos de esquemas que validan y describen los datos utilizados en la API.

5. "routers/": Carpeta con archivos que definen las rutas y endpoints de la API para diferentes partes de la aplicación.

6. "database_example.py": Archivo que contiene la información de conexión a la base de datos (NOTA: a reemplazar. Consultar apartado "configuración de la base de datos).

7. "Testing.py/": Archivo con pruebas unitarias para validar el funcionamiento de la API.

8. "requirements.txt": Archivo que lista las bibliotecas y paquetes necesarios para el proyecto.

9. "README.md": Archivo de texto con información general sobre el proyecto. 

10. fenix_example.py: script que carga un pequeño dataset en la base de datos a modo de ejemplo
