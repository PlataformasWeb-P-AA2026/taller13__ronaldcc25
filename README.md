# taller13

## Creación de Servicio Web y Consumo vía Flask

### Revisar
- Ejemplo de servicios web con Django y Django-Rest [ejemplos]
- Ejemplo de consumo de servicios web desde flask [consumo-api]

### Ejemplos

* Usando requests (librería de python)

```

# GET
import requests
r = requests.get("http://127.0.0.1:8000/api/estudiantes/", auth=('user', 'passs'))
r.content

# POST
r = requests.post('http://127.0.0.1:8000/api/numerost/', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/12/', 'telefono':'99999999', 'tipo'='principal' }, auth=('user', 'pass'))
print(r)

# PUT
r = requests.put('http://127.0.0.1:8000/api/numerost/26', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/13/', 'telefono':'99999999', 'tipo':'principal' }, auth=('user', 'pass'))
print(r)

# DELETE
r = requests.delete('http://127.0.0.1:8000/api/numerost/26/', auth=('user', 'pass'))
print(r)
```


### Problemática

Dadas dos entidades:

* Edificio:
	* nombre
	* dirección
	* ciudad
	* tipo [residencial, comercial]

* Departamento
	* nombre completo del propietario
	* costo del departamento
	* número de cuartos
	* edificio

Nota: Un departamento pertenece a un edificio

### Tecnologías y herramientas:

- Base de datos Sqlite / Postgres (agregar en el readme, evidencias de las tablas en ambas BD)
- Lenguaje Python
- Framework Django
- Django-Rest
- Flask


### Tarea a realizar:

- Crear un proyecto de Django.
- Crear una aplicación en el proyecto en Django.
- Generar el modelo de la aplicación usando las entidades descritas.
- Activar la interfaz de administración de la aplicación de Django.
- A través de views/template presentar un menú para listar en tablas: Edificios, Departamentos (usar el template adjunto)
- Agregar servicios web que permitan lista; crear; actualizar y eliminar entidades (todas deben tener acceso con token)
- Crear una aplicación en Flask que permita:
	-	Listar Edificios haciendo uso de los servicios web creados en el proyecto de Django
 -	<img width="1917" height="1020" alt="image" src="https://github.com/user-attachments/assets/7600495c-3d2d-424c-9129-cc0943432c53" />
	- Listar Departamentos haciendo uso de los servicios web creados en el proyecto de Django.
 - <img width="1917" height="1015" alt="image" src="https://github.com/user-attachments/assets/a070d53e-9e04-4f6b-81e3-3a39641553e6" />
	- Crear Edificios haciendo uso de los servicios web creados en el proyecto de Django.
 - <img width="1917" height="1020" alt="image" src="https://github.com/user-attachments/assets/b4214d93-9ff9-48b7-b880-b4a6137c7398" />
	- Crear Departamentos haciendo uso de los servicios web creados en el proyecto de Django.
 - <img width="1917" height="1016" alt="image" src="https://github.com/user-attachments/assets/88a3c8ab-c881-47d9-8790-35daa720a606" />

### BASE DE DATOS

- <img width="1352" height="446" alt="image" src="https://github.com/user-attachments/assets/8e311c50-c6bb-49f2-8b32-2c98445f4b5c" />

- <img width="1377" height="410" alt="image" src="https://github.com/user-attachments/assets/3056372b-43bc-4563-81bf-59268f532bae" />
