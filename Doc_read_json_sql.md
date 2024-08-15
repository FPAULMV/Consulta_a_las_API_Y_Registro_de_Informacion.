# Procesamiento de Archivos JSON y Almacenamiento en SQL Server

## **Propósito:**  
Este proyecto tiene como objetivo leer archivos JSON almacenados en un directorio específico, procesar los datos y almacenarlos en una base de datos SQL Server. Los archivos JSON se identifican por su fecha en el nombre del archivo y se almacenan en subdirectorios organizados por mes y año.  

## **Contenido:**  
- [Dependencias](#dependencias)
- [Instalación](#instalacion)
- [Descripción de funciones](#descripcion-de-funciones)
- [Configuración](#configuracion)
- [Uso](#uso)

### Dependencias

**Librerías requeridas:** `os`, `json`, `pyodbc`, `decouple`, `datetime`.

Instalar las librerías `pyodbc` y `python-decouple` vía pip:  
```bash
pip install pyodbc python-decouple
```
*`json`*, *`os`*, *`datetime`* (de la cual *`datetime`* y *`timedelta`* son partes), son parte de la biblioteca estándar de Python, por lo que no necesitan instalación a través de pip.  

### Instalación 

Puedes clonar este repositorio a través de git: 
```bash
git clone https://github.com/FPAULMV/Consulta_a_las_API_de_Pemex_Y_Registro_de_Informacion.
```
### Descripción de funciones  

- ***get_dmy():***  
Devuelve día, mes, y año de una fecha dada.
```python
def get_dmy(fecha_str: str):
```
**Requiere:** una fecha *(como str)* en formato `'ddmmaaaa'`.  
```bash
'01012024'
```
**Retorna:** El día *(como int)*, el nombre del mes en español *(como str)*, el año *(como int)*.
```bash
dia = 1
mes = 'Enero'
año = 2024
```
- ***get_dates():***
Genera una lista de fechas en formato `'ddmmaaaa'` dentro de un rango de fechas proporcionado.
```python
def url_embarques(start_date: str =None, end_date: str =None):
```

**Requiere:**  
   - **start_date:** *(como str, opcional)* Fecha de inicio en formato `'ddmmaaaa'`. Si no se proporciona, se toma el valor de ***`query_days`*** en el archivo `.env`.
   - **end_date:** *(como str, opcional)* Fecha de fin en formato `'ddmmaaaa'`. Si no se proporciona, se toma el valor de la fecha actual.
```bash
start_date = '01012024'
end_date = '03012024'
```

**Retorna:**  
   - Lista de fechas en formato `'ddmmaaaa'`.
```bash
Fechas:
(01012024, 02012024, 03012024)
```
- ***guardar_json_en_sql():***
Esta función realiza lo siguiente:
1. Determina la ruta donde se almacenan los archivos JSON basándose en la fecha proporcionada (`month` y `year`).
2. Filtra los archivos en esa ruta que coincidan con la fecha en el nombre del archivo.
3. Lee los archivos JSON y almacena los datos en la tabla indicada por ***`table_name`*** en el archivo `.env`.

```python
def url_embarques(start_date: str =None, end_date: str =None):
```
**Requiere:**  
   - **start_date:** *(como str, opcional)* Fecha de inicio en formato `'ddmmaaaa'`. Si no se proporciona, se toma el valor de ***`query_days`*** en el archivo `.env`.
   - **end_date:** *(como str, opcional)* Fecha de fin en formato `'ddmmaaaa'`. Si no se proporciona, se toma el valor de la fecha actual.
```bash
start_date = '01012024'
end_date = '03012024'
```

### Configuración  

Configura las variables de entorno para el script con un archivo `.env` ubicado en el directorio raíz donde se ejecuta el código.  

***server:*** Nombre del servidor al cual se va a conectar.  
```bash
server = nombre_de_mi_server
```
***database:*** Nombre de la base de datos donde se aloja tu tabla.
```bash
database = mi_base_de_datos
```
***user_name:*** Usuario con el que ingresa a el servidor.
```bash
user_name = Usuario_1 
```
***password:*** Contraseña de el usuario con el que ingresa a el servidor.
```bash
password = m1c0ntrasen4 
```
***driver:*** Controlador de conexion a sql server. *(Se tiene predeterminado ODBC Driver 17 for SQL Server pero puede ser cambiado por el de su preferencia.)*
```bash
driver = ODBC Driver 17 for SQL Server  
```
***table_name:*** Nombre de la tabla donde registra la informacion.
```bash
table_name = BaseDeDatos.dbo.MiTabla
```
***download_path:*** Utilizada en la variable *`carpeta_json`* de la función *`guardar_json_en_sql()`*. Define la ruta donde se descargará la información de la API y el nombre que va a tener cada archivo según su versión. 
```bash
download_path = C:\Usuarios\Mi_Usuario\Documentos\
```
***name_api:*** Utilizada en la variable *`carpeta_json`* de la función *`guardar_json_en_sql()`*. Define, después de la ruta principal, el nombre de la carpeta donde se guardarán los archivos. Esto permite controlar dónde se guardan los documentos de cada API. 
```bash
name_api = mi_api
```
***name_dir:*** Utilizada en la variable *`archivos_json`* de la función *`guardar_json_en_sql()`*. Define, el nombre que tendra el documento una vez la informacion sea descargada por la API. 
```bash
name_dir = Mi_archivo
```

### Uso  

Se planea que el uso del scrip, se ejecute en una tarea programada para que consulte automaticamente la consulta a las API segun las nececidades de cada comercializador.  

Aquí se presentan ejemplos de cómo utilizar el scrip disponible en este repositorio.   

#### **1. Configuración del entorno**  

Antes de ejecutar el script principal, asegúrate de que el archivo `.env` esté configurado correctamente con las credenciales y parámetros necesarios:

```bash
server = nombre_de_mi_server
database = mi_base_de_datos
user_name = Usuario_1
password = m1c0ntrasen4
driver = ODBC Driver 17 for SQL Server
table_name = BaseDeDatos.dbo.MiTabla 
```


