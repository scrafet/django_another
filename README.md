# DjangoAnother

Este es un proyecto base de Django que proporciona una base sólida para futuros proyectos. Incluye funcionalidades esenciales como la gestión de sesiones, un sistema de inicio de sesión (login) y un control de acceso basado en roles.

## Características

*   **Autenticación de usuarios:** Sistema de login y logout para usuarios.
*   **Gestión de sesiones:** Manejo seguro de las sesiones de usuario.
*   **Control de acceso por roles:** Permite definir diferentes niveles de acceso para distintos tipos de usuarios.
*   **Base de datos SQLite:** Configurado para usar SQLite, ideal para desarrollo y proyectos pequeños.
*   **Interfaz de administración:** Incluye el panel de administración de Django preconfigurado.

## Guía de Implementación Local

Siga estos pasos para configurar y ejecutar el proyecto en su máquina local.

### 1. Clonar el repositorio

Clone este repositorio en su máquina local utilizando el siguiente comando:

```bash
git clone <URL_DEL_REPOSITORIO>
```

### 2. Crear un entorno virtual

Es una buena práctica utilizar un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
```

Active el entorno virtual:

*   **En Windows:**
    ```bash
    venv\Scripts\activate
    ```
*   **En macOS y Linux:**
    ```bash
    source venv/bin/activate
    ```

### 3. Instalar dependencias

Instale todas las dependencias necesarias que se encuentran en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Realizar las migraciones

Aplique las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```

### 5. Crear un superusuario

Cree un superusuario para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

Siga las instrucciones en la terminal para establecer un nombre de usuario, correo electrónico y contraseña.

### 6. Ejecutar el servidor de desarrollo

Inicie el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

El proyecto estará disponible en `http://127.0.0.1:8000/`. Puede acceder al panel de administración en `http://127.0.0.1:8000/admin`.
