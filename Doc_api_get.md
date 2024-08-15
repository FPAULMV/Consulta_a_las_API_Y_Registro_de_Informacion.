
# Consulta a las API de ------

## **Propósito:**  
Las API de ------ solo están disponibles para sus comercializadores afiliados. Este repositorio se crea mientras trabajo para uno de estos comercializadores y tiene como objetivo automatizar las consultas a la API para descargar y almacenar la información obtenida.  

## **Contenido:**  
- [Dependencias](#dependencias)
- [Instalación](#instalacion)
- [Descripción de funciones](#descripcion-de-funciones)
- [Configuración](#configuracion)
- [Uso](#uso)
- [Licencia](#licencia)
   
### **Dependencias**  

**Librerías requeridas:** *`python-decouple`*, *`requests`*, *`json`*, *`os`*, *`datetime`*, *`re`*, *`time`*, *`sys`*, *`logging`*.  

Instalar las librerías `requests` y `python-decouple` vía pip:  
```bash
pip install requests python-decouple
```
*`json`*, *`os`*, *`datetime`* (de la cual *`datetime`* y *`timedelta`* son partes), *`re`*, *`time`*, *`sys`*, y *`logging`* son parte de la biblioteca estándar de Python, por lo que no necesitan instalación a través de pip.  

### **Instalación**  

Puedes clonar este repositorio a través de git: 
```bash
git clone https://github.com/FPAULMV/Consulta_a_las_API_de_------
```

### **Descripción de funciones**  

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

- ***validar_path():***
Valida si una ruta a un directorio existe. Si no, la crea.
```python
def validar_path(path: str):
```
**Requiere:** Ruta del directorio a validar *(como str)*.
```bash
C:\Ruta\a_validar\de\tu_directorio\
```
**Retorna:** No retorna ningún valor.  

- ***get_version():***
Encuentra el siguiente número de versión para los archivos que siguen el patrón dado dentro de un directorio específico. El propósito de la función es evitar archivos con nombres duplicados agregando un número de versión. 
```python
def get_version(file_base: str, directory: str):
```  
**Requiere:** 
   - **file_base:** *(como str)* El nombre base que llevará el archivo descargado, a este se le agregará `"_V_"` más el número de versión `'1'`.
   - **directory:** *(como str)* El directorio donde se encuentran los archivos.
```bash
file_base = 'Mi_archivo'
directory = 'C:\Usuarios\Mi_Usuario\Documentos\'
```
**Retorna:** La ruta del directorio más el nombre del nuevo archivo con el sufijo de versión.  
```bash
nuevo_nombre = 'C:\Usuarios\Mi_Usuario\Documentos\Mi_archivo_V_1'
```

- ***url_embarques():***
Genera URLs de la API a consultar, agregando el parámetro de búsqueda para la API, que en este caso es una fecha en formato `'ddmmaaaa'` y una lista de fechas en formato `'ddmmaaaa'` dentro de un rango de fechas proporcionado.
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
   - Lista de URLs a consultar más el parámetro de búsqueda. 
   - Lista de fechas en formato `'ddmmaaaa'`.
```bash
URLs:
(https://api_a_consultar/01012024, https://api_a_consultar/02012024, https://api_a_consultar/03012024)
Fechas:
(01012024, 02012024, 03012024)
```

- ***timer():***
Muestra un temporizador en la consola que cuenta hacia atrás, iniciando desde el número de segundos especificado. Esto sirve para interactuar con el usuario y evitar el error HTTP 429 por *'Demasiadas solicitudes'*. Está predeterminado en 60 segundos. 
```python
def timer(segundos):
```
**Requiere:**
   - **segundos:** *(cualquier valor)* Este valor se proporciona en la variable ***`time_sleep`*** en el archivo `.env`.
```bash
segundos = 5
```
**Retorna:** Cuenta regresiva en consola. 
```bash
Tiempo restante para la siguiente consulta: 5 segundos.
Tiempo restante para la siguiente consulta: 4 segundos.
Tiempo restante para la siguiente consulta: 3 segundos.
Tiempo restante para la siguiente consulta: 2 segundos.
Tiempo restante para la siguiente consulta: 1 segundo.

- ¡Puede volver a consultar!
```

### **Configuración**  

Configura las variables de entorno para el script con un archivo `.env` ubicado en el directorio raíz donde se ejecuta el código. 

***user:*** Nombre de usuario proporcionado por ------ para autenticarnos en la API.
```bash
user = mi_usuario
```
***passw:*** Contraseña proporcionada por ------, del usuario con el que nos autenticamos en la API.
```bash
passw = m1Passw0rd!
```
***url:*** URL de la API proporcionada por ------. 
```bash
url = https://api_a_consultar/
```
***query_days:*** Utilizada en la función *`url_embarques()`*, indica el rango de días para los cuales se realizará una consulta en la API. Predeterminado en *1*
```bash
query_days = 1 
```
***time_sleep:*** Utilizada en la función *`timer()`*, indica el número de segundos para la cuenta regresiva. Predeterminado en *60*.
```bash
time_sleep = 60 
```
***download_path:*** Utilizada en la variable *`path`* de la función *`main()`*. Define la ruta donde se descargará la información de la API y el nombre que va a tener cada archivo según su versión. 
```bash
download_path = C:\Usuarios\Mi_Usuario\Documentos\
```  
***name_api:*** Utilizada en la variable *`path`* de la función *`main()`*. Define, después de la ruta principal, el nombre de la carpeta donde se guardarán los archivos. Esto permite controlar dónde se guardan los documentos de cada API. 
```bash
name_api = mi_api
```
***name_dir:*** Utilizada en la variable *`path`* de la función *`main()`*. Define, después de la ruta principal *(`download_path`)*, el nombre de la carpeta donde se guardarán los archivos. Esto permite controlar dónde se guardan los documentos de cada API. 
```bash
name_dir = Mi_archivo
```
***num_try:*** Utilizada en la variable *`max_retries`* de la función *`main()`*. Define el número de intentos que se realizarán a la API en caso de que la solicitud HTTP devuelva un valor diferente de *200*. Puede cambiar el valor dependiendo de sus necesidades. 
```bash
num_try = 1
```

El archivo `.env` resultante se verá así:
```bash
user = mi_usuario
passw = m1Passw0rd!
url = https://api_a_consultar/
query_days = 1
time_sleep = 60
download_path = C:\Usuarios\Mi_Usuario\Documentos\
name_api = mi_api
name_dir = Mi_archivo
num_try = 1
```

### **Uso**  

Se planea que el uso del scrip, se ejecute en una tarea programada para que consulte automaticamente la consulta a las API segun las nececidades de cada comercializador.   

Aquí se presentan ejemplos de cómo utilizar las funciones y scripts disponibles en este repositorio. 

#### **1. Configuración del entorno**

Antes de ejecutar el script principal, asegúrate de que el archivo `.env` esté configurado correctamente con las credenciales y parámetros necesarios:

```bash
user = mi_usuario
passw = m1Passw0rd!
url = https://api_a_consultar/
query_days = 1
time_sleep = 60
download_path = C:\Usuarios\Mi_Usuario\Documentos\
name_api = mi_api
name_dir = Mi_archivo
num_try = 1
```

#### **2. Ejecución del script principal**

Para ejecutar el script principal y comenzar a descargar datos desde la API de ------, usa el siguiente comando en la terminal:

```bash
python main.py
```

El script consultará la API en el rango de fechas especificado, descargará los datos y los almacenará en la carpeta indicada en el archivo `.env`.

#### **3. Uso de funciones individuales**

Puedes usar las funciones de manera individual en otros scripts o de forma interactiva. Aquí algunos ejemplos:

**Obtener día, mes y año de una fecha:**

```python
from funciones import get_dmy

fecha = '01012024'
dia, mes, año = get_dmy(fecha)
print(dia, mes, año)  # Salida: 1 Enero 2024
```

**Validar o crear un directorio:**

```python
from funciones import validar_path

ruta = 'C:\Usuarios\Mi_Usuario\Documentos\Nueva_Carpeta\'
validar_path(ruta)
```

**Generar URLs para consultas a la API:**

```python
from funciones import url_embarques

urls, fechas = url_embarques('01012024', '03012024')
print(urls)  # Salida: ['https://api_a_consultar/01012024', 'https://api_a_consultar/02012024', 'https://api_a_consultar/03012024']
```

#### **4. Errores comunes y soluciones**

- **Error 429: Demasiadas solicitudes:**  
  Si encuentras este error, puedes ajustar la variable `time_sleep` en el archivo `.env` para aumentar el tiempo de espera entre solicitudes y evitar este problema.

- **Error de autenticación:**  
  Verifica que las credenciales en el archivo `.env` sean correctas. Si cambian, deberás actualizarlas.






# Proyecto de Procesamiento de Archivos JSON y Almacenamiento en SQL Server

Este proyecto tiene como objetivo leer archivos JSON almacenados en un directorio específico, procesar los datos y almacenarlos en una base de datos SQL Server. Los archivos JSON se identifican por su fecha en el nombre del archivo y se almacenan en subdirectorios organizados por mes y año.

## Descripción del Código

### Dependencias

El script utiliza las siguientes bibliotecas:

- `os`: Para interactuar con el sistema operativo.
- `json`: Para manejar los archivos JSON.
- `pyodbc`: Para la conexión y manipulación de la base de datos SQL Server.
- `decouple`: Para manejar las variables de entorno.
- `datetime`: Para trabajar con fechas.

### Funciones

#### `get_dmy(fecha_str)`

Convierte una cadena de fecha en formato `ddmmaaaa` a un objeto `datetime` y devuelve el mes y el año en formato de cadena. Utiliza un arreglo para los nombres de los meses en español.

#### `get_dates(start_date=None, end_date=None)`

Genera una lista de fechas en formato `ddmmaaaa` entre dos fechas proporcionadas. Si no se proporciona una `start_date`, se toma como referencia la fecha actual menos una cantidad de días definida en una variable de entorno (`query_days`). Si no se proporciona una `end_date`, se toma la fecha actual.

#### `guardar_json_en_sql(fecha, month, year)`

Esta función realiza lo siguiente:
1. Determina la ruta donde se almacenan los archivos JSON basándose en la fecha proporcionada (`month` y `year`).
2. Filtra los archivos en esa ruta que coincidan con la fecha en el nombre del archivo.
3. Lee los archivos JSON y almacena los datos en la tabla `sinergia_aux.dbo.embarques` de SQL Server.

### Ejemplo de Uso

El script establece la conexión a SQL Server utilizando variables de entorno para los detalles de la conexión (`driver`, `server`, `database`, `user_name`, `password`). Luego, llama a la función `get_dates` para obtener las fechas de interés, y para cada fecha, llama a la función `guardar_json_en_sql` para procesar y almacenar los datos.

Finalmente, la conexión a SQL Server se cierra.

### Variables de Entorno

Este script utiliza `decouple` para gestionar las configuraciones a través de variables de entorno. Las siguientes variables deben estar configuradas en un archivo `.env`:

- `query_days`: Número de días atrás desde la fecha actual para iniciar el proceso.
- `download_path`: Ruta base donde se encuentran los archivos JSON.
- `name_api`: Nombre de la API (utilizado en la ruta de los archivos).
- `name_dir`: Prefijo en los nombres de los archivos JSON.
- `driver`: Driver de SQL Server.
- `server`: Nombre del servidor SQL.
- `database`: Nombre de la base de datos.
- `user_name`: Nombre de usuario para la conexión a SQL Server.
- `password`: Contraseña para la conexión a SQL Server.

### Ejecución del Script

El script se ejecuta en Python y requiere una configuración previa del entorno y las variables de conexión. Asegúrese de que todos los archivos JSON estén en la ubicación correcta y que las variables de entorno estén configuradas adecuadamente.

1. Clone este repositorio o copie el código.
2. Cree un archivo `.env` con las configuraciones necesarias.
3. Ejecute el script con `python <nombre_del_script>.py`.

```bash
python script_json_to_sql.py
