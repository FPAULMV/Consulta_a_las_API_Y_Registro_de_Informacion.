# Procesamiento de Archivos JSON y Almacenamiento en SQL Server

## **Propósito:**  
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
