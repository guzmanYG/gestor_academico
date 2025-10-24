# Gestor Académico Web (GAW)
Proyecto Django: Gestor Académico Web - scaffold generado automáticamente.

## Requisitos
- Python 3.8+
- pip

## Instalación rápida
1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Migraciones y ejecución:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
4. Admin: crea un superusuario con `python manage.py createsuperuser`.

## Estructura generada
- gestor_academico_web/ (settings, urls, wsgi)
- gestor_academico/ (app principal: models, views, algorithms, structures, templates, static)
