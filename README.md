# Consulta_a_las_API_de_Pemex.

# **Propósito:**  
   Las API´s de Pemex solo están disponibles para sus comercializadores afiliados. Este repositorio se crea mientras trabajo para uno de estos y pretende automatizar las consultas a la API para descargar y almacenar esta información.  

# **Contenido.**
## **Funcionamiento general:**   

### **Funciones principales.**   

Función principal donde se llama a la ejecucion de todo el codigo.
``` Python
def main():
```
###Uso de: url_embarques()
```python
def url_embarques(start_date: str =None, end_date: str =None):
   """
    *Genera URLs para consultar a una API y una lista de fechas en formato 'ddmmaaaa'
    dentro de un rango de fechas proporcionado.*

    **Parámetros:**  
    - **start_date:** *Fecha de inicio en formato **'ddmmaaaa'****.* *Si no se proporciona, se usa el valor del archivo .env* **'query_days'***.*
    - **end_date:** *Fecha de fin en formato* **'ddmmaaaa'***.* *Si no se proporciona, se usa la fecha actual.*

    **Retorna:**  
    - **urls:** *Lista de URLs generadas para cada fecha.*
    - **days_list:** *Lista de fechas en formato* **'ddmmaaaa'***.*
    """
```  
Valida que
```
```

```
```







## - **Principales Funciones:**
   Inicialmente hay que generar un archvio .env en el directorio raiz de el proyecto donde ingresaremos configuraciones clave para el funcionamiento del scrip. Se explican a continuacion:

   **-- Datos de conexión a SQL Server. --**
  
   **Nombre del servidor de SQL Server al que se conectará la aplicación.**  
   server = ''
   
   **Nombre de la base de datos en el servidor de SQL Server.**  
   database = '' 

   **Nombre de usuario para autenticarse en el servidor de SQL Server.**  
   user_name = ''
   
   **Contraseña correspondiente al nombre de usuario.**  
   password = ''
   
   **Controlador ODBC que se utilizará para la conexión con SQL Server.** -> *(Puede cambiar por el controlador de su eleccion, compatible con su sistema.)*  
   driver = ODBC Driver 17 for SQL Server 
   
   **-- Datos de conexión a la API. --**
   
   **Nombre de usuario para autenticarse en la API.** -> *(Estas credenciales las proporciona Pemex a sus comercializadoras)*  
   user = ''
   
   **Contraseña correspondiente al nombre de usuario de la API.** -> *(Estas credenciales las proporciona Pemex a sus comercializadoras)*  
   passw = ''
   
   **URL base de la API, sin incluir los argumentos de búsqueda, y finalizando con '/'.** -> *(La URL de la API tambien la proporciona pemex a sus comercializadoras)*  
   url = ''
   
   **-- Datos de configuración. --**
   
   **Número de días anteriores a la fecha actual que se utilizarán para la consulta.** -> *(Es el rango de días anterior a la fecha actual, en este rango de fechas se ejecutara el scrip. Mantener 1 como predeterminado)*  
   query_days = 1 
   
   **Tiempo de espera en segundos entre cada consulta a la API.** -> *(Al hacer varias consultas seguidas la API devuelve un codigo http 429, las consultas se pueden hacer con 60 segundos de diferencia. Puede aumentar este tiempo segun sus nececidades.)*  
   time_sleep = 60 
   
   **Ruta del directorio donde se descargarán los archivos obtenidos de la API.**  
   download_path = '' 
   
   **Nombre del directorio predeterminado donde se almacenarán los archivos descargados.**  
   name_api = '' 
   
   **Nombre predeterminado del documento que se creará para almacenar los datos descargados.**  
   name_dir = ''   
   
   **O de la siguiente manera**  
   server =  
   database =   
   user_name =    
   password =   
   driver =   
   user =   
   passw =   
   url =    
   query_days = 1   
   time_sleep = 60   
   download_path =   
   name_api =   
   name_dir =    
