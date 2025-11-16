# Comparativa de Proyectos: Portafolio Estático vs. Portafolio con Django

## Introducción

El presente documento describe y compara dos implementaciones de un portafolio personal. La primera versión original (propuesta de portafolio elaborada en Módulo 2 y disponible en el repositorio de GitHub: https://github.com/JorgeCardenasY/M2_PORTAFOLIO), corresponde a un sitio web estático elaborado en HTML, CSS y JavaScript. La segunda versión, desarrollada en el entorno actual, es una aplicación web dinámica construida con el framework Django. El objetivo de esta comparativa es analizar las diferencias en arquitectura, funcionalidades y escalabilidad entre ambas soluciones desde una perspectiva de desarrollo de software.

---

## 1. Tecnologías y Arquitectura

### 1.1. Versión Estática (GitHub)

El proyecto original se basa en una arquitectura de cliente-servidor puramente estática. Las tecnologías empleadas son:

-   **HTML5:** Para la estructuración del contenido.
-   **CSS3:** Para la estilización y el diseño visual.
-   **Bootstrap y jQuery:** Para la responsividad y la manipulación de eventos del DOM.

En este modelo, el servidor web se limita a entregar archivos (`.html`, `.css`, `.js`) al cliente sin ningún procesamiento del lado del servidor.

### 1.2. Versión Dinámica (Django)

El proyecto actual representa una evolución hacia una arquitectura dinámica, siguiendo el patrón **Modelo-Vista-Plantilla (MVT)** de Django:

-   **Backend (Python/Django):** Gestiona la lógica de negocio, el enrutamiento de URLs, el procesamiento de formularios y la interacción con la base de datos (aunque la base de datos no se utiliza en gran medida en la etapa actual).
-   **Frontend (Plantillas Django):** Utiliza un sistema de plantillas que permite la reutilización de componentes (ej. `base.html`, `navbar.html`) y la inserción de contenido dinámico en las páginas.

Esta arquitectura separa claramente la lógica de la presentación, lo que resulta en un código más organizado y mantenible.

---

## 2. Estructura del Proyecto

La diferencia en la organización de los archivos es notable y refleja la especificidad de configuración potencial (al mismo tiempo que la complejidad) de cada enfoque.

-   **Proyecto Estático:** Presenta una estructura simple con directorios para `css`, `js` e `img`, y archivos HTML en la raíz.<br> <br>
-   **Proyecto Django:** Adopta la estructura convencional de Django, con una clara separación de responsabilidades:
    -   `portafolio/`: Directorio de configuración del proyecto.
    -   `CV/`: La "aplicación" de Django que encapsula la funcionalidad del currículum y las vistas principales.
    -   `templates/`: Contiene las plantillas HTML reutilizables.
    -   `static/`: Gestiona los archivos estáticos (CSS, JS, imágenes).
    -   `manage.py`: El script de utilidad para la gestión del proyecto.

---

## 3. Análisis de Funcionalidades

### 3.1. Renderizado de Páginas

-   **Versión Estática:** Cada página es un archivo HTML autocontenido. Cualquier cambio en elementos comunes, como la barra de navegación, debe replicarse manualmente en todos los archivos.
-   **Versión Django:** Las páginas se generan dinámicamente. Se utiliza una plantilla base (`base.html`) que define la estructura común, y las páginas específicas (`index.html`, `analytics.html`) extienden esta base, _inyectando sólo_ el contenido particular del bloque `{% block content %}`. Esto reduce la duplicación de código y facilita el mantenimiento (filosofía DRY - Don't Repeat Yourself de DJANGO).

### 3.2. Formulario de Contacto

-   **Versión Estática:** El formulario de contacto es puramente visual. No posee la capacidad de procesar o enviar los datos ingresados por el usuario.<BR><BR>
-   **Versión Django:** Se implementa un `ContactForm` utilizando el sistema de formularios de Django. La vista `contact` procesa los datos del formulario en el servidor (validación, limpieza), lo que permitiría una futura integración con servicios de envío de correo electrónico.

### 3.3. Escalabilidad y Mantenibilidad

-   **Versión Estática:** La escalabilidad es limitada. Agregar nuevas secciones o páginas es un proceso manual y propenso a errores.
-   **Versión Django:** El diseño es inherentemente escalable. Es posible agregar nuevas aplicaciones, modelos de datos y funcionalidades de manera modular. El sistema de enrutamiento de URLs (`urls.py`) permite una gestión centralizada y clara de las rutas de la aplicación.

---

## Conclusión

Con lo anterior, podemos decir que la transición del proyecto estático a una aplicación Django demuestra un avance significativo en las competencias técnicas  desarrolladas durante el BootCamp: Se pasa de un modelo de presentación simple a una arquitectura de software robusta, escalable y mantenible. La implementación con Django evidencia la comprensión de conceptos de desarrollo backend, como el patrón MVT, el procesamiento de formularios del lado del servidor y el uso de un sistema de plantillas para la generación de vistas dinámicas. Este enfoque sienta las bases para futuras potencialidades en el desarrollo, tales como la integración con bases de datos SQL, la autenticación de usuarios y la creación de APIs.
