# Consulta_a_las_API_de_Pemex
 - **Propósito:**
   Las API´s de Pemex solo están disponibles para sus comercializadores afiliados. Este repositorio se crea mientras trabajo para uno de estos y pretende automatizar las consultas a la API para descargar y almacenar esta información.

- **Funcionamiento general:**
  ~ El scrip esta pensado para ejecutarse automaticamente cada cierto tiempo (Depende de las nececidades del comercializador) sin la intervencion de una persona, aunque tambien se puede correr "manualmente".
  
  ~ Depende de un rango de fechas entre una fecha inicial y una fecha final, que se puede ingresar en el codigo y despues ejecutarse. En caso de no ingresar una fecha inicial el codigo se ejecutara en el rango de fechas comprendido entre la fecha actual menos la cantidad de dias señalado en el archivo .env con el nombre: 'query_days'.
  Ejemplo:
   Hoy es = 03-01-2024, query_days = 2, entonces el rango de fechas para realizar la consulta sera del 01-01-2024 al 03-01-2024


# - **Principales Funciones:**
   Inicialmente hay que generar un archvio .env en el directorio raiz de el proyecto donde ingresaremos configuraciones clave para el funcionamiento del scrip. Se explican a continuacion:

   **-- Datos de conexión a SQL Server. --**
  
   **Nombre del servidor de SQL Server al que se conectará la aplicación.**
   
   server = ''
   
   **Nombre de la base de datos en el servidor de SQL Server.**
   
   database = '' 

   **Nombre de usuario para autenticarse en el servidor de SQL Server.**

   
   user_name = ''
   # Contraseña correspondiente al nombre de usuario.
   password = ''
   # Controlador ODBC que se utilizará para la conexión con SQL Server. -> (Puede cambiar por el controlador de su eleccion, compatible con su sistema.)
   driver = ODBC Driver 17 for SQL Server 
   
   # -- Datos de conexión a la API. -- #
   # Nombre de usuario para autenticarse en la API. -> (Estas credenciales las proporciona Pemex a sus comercializadoras)
   user = ''
   # Contraseña correspondiente al nombre de usuario de la API. -> (Estas credenciales las proporciona Pemex a sus comercializadoras)
   passw = ''
   # URL base de la API, sin incluir los argumentos de búsqueda, y finalizando con '/'. -> (La URL de la API tambien la proporciona pemex a sus comercializadoras)
   url = ''
   
   # -- Datos de configuración. -- #
   # Número de días anteriores a la fecha actual que se utilizarán para la consulta. -> (Es el rango de días anterior a la fecha actual, en este rango de fechas se ejecutara el scrip. Mantener 1 como predeterminado)
   query_days = 1 
   # Tiempo de espera en segundos entre cada consulta a la API. -> (Al hacer varias consultas seguidas la API devuelve un codigo http 429, las consultas se pueden hacer con 60 segundos de diferencia. Puede aumentar este tiempo segun sus nececidades.  )
   time_sleep = 60 
   # Ruta del directorio donde se descargarán los archivos obtenidos de la API.
   download_path = '' 
   # Nombre del directorio predeterminado donde se almacenarán los archivos descargados.
   name_api = '' 
   # Nombre predeterminado del documento que se creará para almacenar los datos descargados.
   name_dir = '' 
 
