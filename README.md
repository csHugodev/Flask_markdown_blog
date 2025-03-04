# Blog de Tecnología con Flask

Este es un proyecto ejemplo de cómo implementar una aplicación de blog utilizando **Flask**. Los posts del blog se almacenan como archivos estáticos en formato **Markdown**, lo que permite gestionarlos fácilmente y renderizarlos en HTML dinámicamente utilizando la librería **Mistune**.

## Características

- **Flask**: Framework de Python utilizado para el desarrollo del backend.
- **Mistune**: Librería de Python utilizada para convertir archivos Markdown a HTML.
- **Markdown**: Los posts del blog están escritos en archivos Markdown que se leen y procesan en el servidor.
- **Bootstrap**: Framework CSS utilizado para el diseño y la interfaz de usuario.
- **Modo oscuro**: La aplicación soporta un modo oscuro, que se puede alternar con un botón en el frontend.
- **Estructura simple**: El proyecto está diseñado para ser una implementación básica de Flask con estructura modular para facilitar su extensión.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:


### Rutas principales

- `/`: Página principal con texto de inicio.
- `/posts/`: Página de la lista de posts
- `/posts/<post_id>`: Página de lectura de un post individual.

## Archivos Markdown

Los posts del blog se encuentran en la carpeta `/codex_blog/views/static/posts/` en formato Markdown. Cada archivo de post debe tener la siguiente estructura:

```markdown
# Título del Post
autor
fecha

## Contenido del Post
Aquí va el contenido completo del post.
```

## Uso
Para iniciar el servidor de desarrollo, ejecuta el siguiente comando:
```bash
python run.py
```
Esto levantará un servidor de desarrollo en http://localhost:1999/. Puedes acceder a las rutas para ver la lista de posts y leer el contenido de cada uno.
Se puede modificar en el archivo `config.py`

Este es un proyecto básico y ejemplar para mostrar cómo usar Flask con archivos estáticos Markdown. Puedes extenderlo y adaptarlo según tus necesidades.