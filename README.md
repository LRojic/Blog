# Bitácora · Blog personal

Blog personal desarrollado con Django para el trabajo práctico de Laboratorio de Algoritmos y Estructuras de Datos.

## Funcionalidades

- Entradas ordenadas de la más nueva a la más antigua.
- Texto, categoría e imagen opcional por entrada.
- Comentarios públicos asociados a cada entrada.
- Panel `/admin/` para que el administrador cree entradas y elimine comentarios.
- Diseño responsive y consistente para escritorio y móvil.

## Cómo ejecutar

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Luego abrí `http://127.0.0.1:8000/` para ver el portafolio. Desde allí podés entrar al blog con el enlace **Blog** o visitando `http://127.0.0.1:8000/blog/`. El panel de administración está en `http://127.0.0.1:8000/admin/`.