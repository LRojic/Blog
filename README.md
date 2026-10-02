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

## Guardar los datos entre cargas

La base de datos SQLite (`db.sqlite3`) y las imágenes subidas (`media/`) se conservan en el repositorio. Después de crear usuarios, entradas, comentarios o subir imágenes, guardá esos cambios en Git para que estén disponibles al volver a clonar o cargar el proyecto:

```bash
git add db.sqlite3 media/
git commit -m "Actualizar datos del blog"
git push
```

Usá un repositorio privado: la base contiene cuentas de administración (incluidos hashes de contraseñas), correos y comentarios. Git conserva los datos solo después de hacer commit y push; no los sincroniza automáticamente.