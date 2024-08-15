# Procesamiento de Archivos JSON y Consulta a las API de Pemex

## Propósito
Este repositorio tiene dos objetivos principales:

1. **Procesamiento de Archivos JSON y Almacenamiento en SQL Server:** Leer archivos JSON almacenados en un directorio específico, procesar los datos y almacenarlos en una base de datos SQL Server.

2. **Consulta a las API de Pemex:** Automatizar las consultas a las API de Pemex para descargar y almacenar la información obtenida, exclusivamente para los comercializadores afiliados.

## Contenido
- [Dependencias](#dependencias)
- [Instalación](#instalación)
- [Descripción de funciones](#descripción-de-funciones)
- [Configuración](#configuración)
- [Uso](#uso)
- [Errores comunes y soluciones](#errores-comunes-y-soluciones)

### Dependencias

**Librerías requeridas:**  
- *`python-decouple`*  
- *`requests`*  
- *`json`*  
- *`os`*  
- *`datetime`*  
- *`re`*  
- *`time`*  
- *`sys`*  
- *`logging`*  
- *`pyodbc`*

Instalar las librerías necesarias vía pip:  
```bash
pip install requests python-decouple pyodbc
```
json, os, datetime, re, time, sys, y logging son parte de la biblioteca estándar de Python, por lo que no necesitan instalación a través de pip.

Instalación
Clona este repositorio usando Git:

bash
Copiar código
git clone https://github.com/FPAULMV/Consulta_a_las_API_de_Pemex_Y_Registro_de_Informacion
Descripción de funciones
Procesamiento de Archivos JSON
get_dmy():
Devuelve día, mes, y año de una fecha dada en formato 'ddmmaaaa'.

guardar_json_en_sql():
Lee archivos JSON de un directorio específico y almacena los datos en una tabla SQL Server.

Consulta a las API de Pemex
validar_path():
Valida si una ruta a un directorio existe; si no, la crea.

get_version():
Encuentra el siguiente número de versión para los archivos en un directorio específico.

url_embarques():
Genera URLs de la API a consultar y una lista de fechas en formato 'ddmmaaaa'.

timer():
Muestra un temporizador en la consola para evitar errores HTTP 429 (Demasiadas solicitudes).

Configuración
Configura las variables de entorno usando un archivo .env en el directorio raíz:

bash
Copiar código
# SQL Server Configuration
server = nombre_de_mi_server
database = mi_base_de_datos
user_name = Usuario_1
password = m1c0ntrasen4
driver = ODBC Driver 17 for SQL Server
table_name = BaseDeDatos.dbo.MiTabla

# API Pemex Configuration
user = mi_usuario
passw = m1Passw0rd!
url = https://api_a_consultar/
query_days = 1
time_sleep = 60
download_path = C:\Usuarios\Mi_Usuario\Documentos\
name_api = mi_api
name_dir = Mi_archivo
num_try = 1
Uso
Procesamiento de Archivos JSON
Configura el entorno correctamente en el archivo .env.
Ejecuta el script para procesar y almacenar archivos JSON en SQL Server:
bash
Copiar código
python main_json.py
Consulta a las API de Pemex
Configura el entorno correctamente en el archivo .env.
Ejecuta el script para consultar las API y descargar datos:
bash
Copiar código
python main.py
Errores comunes y soluciones
Error 429: Demasiadas solicitudes:
Aumenta el valor de time_sleep en el archivo .env.

Error de autenticación:
Verifica y actualiza las credenciales en el archivo .env.
