<a id="readme-top"></a>

[![https://www.linkedin.com/in/leonelmaretto/][linkedin-shield]][linkedin-url]

# Data Engineering Project

![enter image description here](https://mmos.com/wp-content/uploads/2020/01/riot-games-new-logo-red-bg-banner.jpg)

<!-- ABOUT THE PROJECT -->
## Descripción del proyecto

![enter image description here](https://nosnerds.com.br/wp-content/uploads/2018/01/background-1002091.jpg)

Este proyecto forma parte de una práctica de Ingeniería de Datos, cuyo objetivo principal es la extracción de datos utilizando la [API de Riot Games](https://developer.riotgames.com/). El proyecto está enfocado en obtener información relevante sobre jugadores, ligas y otros datos relacionados con el ecosistema de League of Legends.

### **Tecnologías y Lenguaje de Programación:**

El proyecto está desarrollado en **Python** y ha utilizado **Poetry** como gestor de dependencias y control del entorno de desarrollo, ya que facilita la instalación y gestión de librerías de forma eficiente.

### **Buenas prácticas implementadas:**

El proyecto sigue diversas buenas prácticas de programación y desarrollo de software, tanto en la parte técnica como en la organización del código:

*  **PEP 8**: El código sigue las convenciones de estilo definidas en PEP 8, asegurando una mayor legibilidad y consistencia en el uso de nombres de variables y funciones.

*  **Documentación**: Cada función incluye **docstrings** bien estructurados que describen el propósito de la función, los parámetros de entrada y el valor de retorno. Esto facilita la comprensión y el uso del código para otros desarrolladores.

*  **Type Hints**: Se han utilizado anotaciones type hints para especificar el tipo de datos esperado en las funciones, mejorando la claridad del código y ayudando a herramientas de análisis estático.

*  **Manejo de excepciones**: Se implementa el manejo de errores utilizando bloques try-except, lo que permite capturar errores comunes en las solicitudes HTTP o en el procesamiento de los datos.

*  **Logging**: Se ha integrado el uso de logging para rastrear el flujo de ejecución y manejar mensajes de información, advertencias y errores, lo cual es útil para la depuración y mantenimiento del código.

### **Librerías y Herramientas Usadas:**

Este proyecto utiliza varias librerías populares de Python, principalmente enfocadas en la manipulación de datos y en la interacción con la API de Riot Games:

*  **requests**: Utilizado para realizar las solicitudes HTTP a la API REST de Riot Games.

*  **pandas**: Librería clave para la manipulación y análisis de datos, transformando los datos extraídos en estructuras como DataFrames.

*  **configparser**: Para gestionar la configuración del proyecto de forma externa, almacenando claves API y otros parámetros en archivos .ini, lo que facilita el cambio de configuración sin tocar el código fuente.

*  **logging**: Para generar mensajes de log que permiten un seguimiento eficiente de la ejecución del código.

*  **Jupyter Notebooks**: Utilizado para prototipar y probar el código en un entorno interactivo antes de su integración en los módulos principales del proyecto.

### **Estructura del Proyecto:**

El proyecto está organizado de manera que sea fácil de mantener y escalar:

```bash
riotgames_demoV0/
│
├── riotgames_demov0/
│   ├── config/         # Configuración del proyecto
│   │   └── config.ini  # Archivo con las claves API y parámetros
│   ├── notebooks/      # Notebooks para pruebas y prototipos
│   │   └── riotgames_notebook.ipynb
│   ├── __init__.py     # Archivo de inicialización del paquete
│   └── main.py         # Código principal del proyecto
│
└── README.md           # Documentación del proyecto
```


<!-- CONTACT -->
## Contact

Leonel Maretto - [LINKEDIN](https://www.linkedin.com/in/leonelmaretto/) - leosmaretto.dev@gmail.com

Project Link: [https://github.com/cachitossj/RIOT-GAMES-API_v0.1](https://github.com/cachitossj/RIOT-GAMES-API_v0.1)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/leonelmaretto/