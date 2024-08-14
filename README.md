# Consulta_a_las_API_de_Pemex.

# **Propósito:**  
   Las API´s de Pemex solo están disponibles para sus comercializadores afiliados. Este repositorio se crea mientras trabajo para uno de estos y pretende automatizar las consultas a la API para descargar y almacenar esta información.  

# **Contenido.**  
- [Dependencias.]()
- [Instalacion.]()
- [Descripcion de funciones.]()
- [Configuracion.]()
- [Uso.]()
- [Licencia.]()
   
### **Dependencias.**  

**Librerias requeridas:** *python-decouple*, *requests*, *json*, *os*, *datetime*, *re*, *time*, *sys*, *logging*.  

Instalar via pip las librerias requests y  python-decouple.  
```bash
pip install requests python-decouple
```
*json*, *os*, *datetime* (de la cual *datetime* y *timedelta* son partes), *re*, *time*, *sys*, y *logging* son parte de la biblioteca estándar de Python, por lo que no necesitan instalación a través de pip.  


### **Instalacion.**  

Puedes clonar este repositorio a travez  git bash. 
```bash
   git clone https://github.com/FPAULMV/Consulta_a_las_API_de_Pemex

```
### **Descripción de funciones.**  

- ***get_dmy():***  
Devuelve dia, mes, año de una fecha dada.
```python
def get_dmy(fecha_str: str):
```
**Requiere:** una fecha *(como str)* en formato 'ddmmaaaa'.  
```bash
'01012024'
```
**Retorna:** El dia *(como int)*, el nombre del mes en español *(como str)*, el año *(como int)*.
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
**Requiere:** Ruta de el directorio a validar *(como str)*
```bash
C:\Ruta\a_validar_de\tu_directortio\
```
**Retorna:** No retorna ningun valor.  

- ***get_version():***
Encuentra el siguiente número de versión para los archivos que siguen el patrón dado dentro de un directorio específico. El propocito de la funcion es evitar archivos con nombres duplicados agregando un numero de version. 
```python
def get_version(file_base: str, directory: str):
```  
**Requiere:** 
   - **file_base:** *(como str)*
     El nombre base que llevara el archvio descargado, a este se le agregara *"\_V\_"* mas, el numero de version *'1'*.
   - **directory:** *(como str)*
     El directorio donde se encuentran los archivos.
```bash
file_base = 'Mi_archivo'
directory = 'C:\Usuarios\Mi_Usuario\Documentos\'
```
**Retorna:** La ruta del directorio mas, el nombre del nuevo archivo con el sufijo de versión.  
```bash
nuevo_nombre = 'C:\Usuarios\Mi_Usuario\Documentos\Mi_archivo_V_1'
```

- ***url_embarques():***
Genera URL's de la API  a consultar agregando el parametro de busqueda para la API, que en este caso es una fecha en formato 'ddmmaaaa' y una lista de fechas en formato 'ddmmaaaa' dentro de un rango de fechas proporcionado.
```python
def url_embarques(start_date: str =None, end_date: str =None):
```  

**Requiere:**  
   - **start_date:** *(como str)* *(opcional)*
     Fecha de inicio en formato 'ddmmaaaa'. De no proporcionar se toma el valor de ***'query_days'*** en el archivo .env.
   - **end_date:** *(como str)* *(opcional)*
     Fecha de fin en formato 'ddmmaaaa'. De no proporcionar se toma el valor de la fecha actual.
```bash
start_date = '01012024'
end_date = '03012024'
```

**Retorna:**
   - Lista de URL's a consular mas el parametro de busqueda. 
   - Lista de fechas en formato 'ddmmaaaa'
```bash
URL's:
(https://api_a_consultar/01012024, https://api_a_consultar/02012024, https://api_a_consultar/03012024)
Fechas:
(01012024, 02012024, 03012024)
```

- ***timer():***
Muestra un temporizador en la consola que cuenta hacia atrás, iniciando desde el número de segundos especificado. Esto para interactuar con el usuario y evitar error http 429 por *'Demasiadas solicitudes'*. Esta predeterminado en 60 segundos. 
```python
def timer(segundos):
```
**Requiere:**
   - **segundos:** *(cualquier valor)*
     Este valor se proporciona en la variable ***time_sleep*** en el archivo .env.
```bash
segundos = 5
```
**Retorna:** Cuenta regresiva en consola. 
```bash
Tiempo restante para la siguiente consulta: 5 segundos.
Tiempo restante para la siguiente consulta: 4 segundos.
Tiempo restante para la siguiente consulta: 3 segundos.
Tiempo restante para la siguiente consulta: 2 segundos.
Tiempo restante para la siguiente consulta: 1 segundos.

- Puede volver a consultar!
```

### **Configuraciones.**  

Configuramos las variables de entorno para el scrip con un archivo .env ubicado en el directorio raíz donde se ejecuta el codigo. 

***user:*** Nombre de usuario proporcionado por Pemex para autenticarnos en la API .
```bash
user = mi_usuario
```
***passw:*** Contraseña proporcionada por Pemex, del usuario con el que nos autenticamos en la API.
```bash
passw = m1Passw0rd!
```
***url:*** URL de la API proporcionada por Pemex. 
```bash
url:https://api_a_consultar/
```
***query_days:*** Utilizada en la función *url_embarques()* indica el rango de días para los cuales se realizara una consulta en la API. Predeterminado en *'1'*
```bash
query_days = 1 
```
***time_sleep:*** Utilizada en la funcion *timer()* indica el numero de segundos para la cuenta regresiva. Predeterminado en *'60'*.
```bash
time_sleep = 60 
```
***download_path:*** Utilizada en variable *path* de la funcion *main()*. Define la ruta donde se descargara la informacion de la API y el nombre que va a tener cada archivo segun su version. 
```bash
download_path = C:\Usuarios\Mi_Usuario\Documentos\
```  
***name_api:*** Utilizada en variable *path* de la funcion *main()*. Define despues de la ruta principal, el nombre de la carpeta donde se guardaran los archivos, esto para dar control a donde se guardan los documentos de cada API. 
```bash
name_api = mi_api
```
***name_dir:*** Utilizada en variable *path* de la funcion *main()*. Define despues de la ruta principal *('download_path')*, el nombre de la carpeta donde se guardaran los archivos, esto para dar control a donde se guardan los documentos de cada API. 
```bash
name_dir = Mi_archivo
```
***num_try:*** Utilizada en variable *max_retries* de la funcion *main()*. Define el numero de intentos que se realizaran a la API en caso de que la solicitud http devuelva un valor diferente de *'200'*. Puede cambiar el valor dependiendo de sus necesidades. 
```bash
num_try = 1
```



