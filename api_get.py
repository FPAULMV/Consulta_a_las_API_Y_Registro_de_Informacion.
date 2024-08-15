import requests
import json
import os
from decouple import config
from datetime import datetime as dt, timedelta as td
import re
import time
import sys
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Combierte una cadena de texto fecha con formato ddmmaaaa en dia mes y año
def get_dmy(fecha_str: str):
    """
    Devuelve día, mes y año de una fecha.  

    ***Parámetros:***
    - **fecha_str:** Una cadena de texto que representa la fecha en formato *'ddmmaaaa'*.

    ***Retorna:***
    - **day:** *Día de la fecha.*
    - **month:** *Nombre del mes en español.*
    - **year:** *Año de la fecha.*
    """
    
    meses_es = ["Enero", "Febrero", "Marzo", 
                "Abril", "Mayo", "Junio", 
                "Julio", "Agosto", "Septiembre", 
                "Octubre", "Noviembre", "Diciembre"]
    
    # Convertir la cadena de fecha en un objeto datetime
    fecha = dt.strptime(fecha_str, '%d%m%Y')
    
    # Obtener el día, mes y año
    day = fecha.day
    month = meses_es[fecha.month - 1]
    year = fecha.year   
    return day, month, year


# Valida si un directorio existe; si no, lo crea.
def validar_path(path: str):
    """
    Valida si una ruta a directorio existe. Si no, la crea.

    **Parametros:**  
    - **path:** *Ruta de el directorio a validar.*

    No retorna ningun valor. 
    """
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
        print(f"Ruta creada en: {path}")


# Genera un nombre de archivo con la siguiente versión disponible en un directorio.

def get_version(file_base: str, directory: str):
    """Encuentra el siguiente número de versión para los archivos que siguen el patrón dado dentro de un directorio específico.

        **Parámetros:**  
        - **file_base:** *La base del nombre del archivo, por ejemplo:* ***'Archivo_descargado'***.
        - **directory:**  *El directorio donde se encuentran los archivos.*

        **Retorna:**  
        - *El nombre del nuevo archivo con el sufijo de versión.*  
        **Ejemplo:** *'C:> Users > Mi_Usuario > Mis_archivos > Archivo_descargado_V_1'*  
        O en caso de existir: *'C:> Users > Mi_Usuario > Mis_archivos > Archivo_descargado_V_2'* 
    """
    # Buscar archivos existentes en el directorio que sigan el patrón 'file_base_V_X.json'
    existing_files = [f for f in os.listdir(directory) if re.match(file_base + r'_V_\d+\.json$', f)]
    
    # Extraer los números de versión y encontrar el máximo
    versions = [int(re.search(r'_V_(\d+)', f).group(1)) for f in existing_files]
    next_version = max(versions, default=0) + 1
    
    # Crear el nombre del nuevo archivo
    return os.path.join(directory, f"{file_base}_V_{next_version}.json")



# Genera URLs y fechas en formato 'ddmmaaaa' para un rango de fechas proporcionado.
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

    today = dt.now().date()  # Obtiene la fecha actual

    # Validar fechas
    if start_date:
        start_date = dt.strptime(start_date, '%d%m%Y').date()
        if start_date > today:
            print(f"La fecha inicial es mayor a la fecha actual.")
            exit()
    if end_date:
        end_date = dt.strptime(end_date, '%d%m%Y').date()
        if end_date > today:
            print(f"No se pueden consultar fechas mayores a el día actual.")
            exit()
    
    # Si no se proporciona start_date, calcula los dias a consultar segun el valor de la variable en el archivo .env 'query_days'
    if not start_date:
        start_date = today - td(days=int(config('query_days')))
    
    # i no se proporciona end_date el valor será igual a la fecha actual. 
    if not end_date:
        end_date = today

    # Validar que start_date no sea mayor que end_date
    if start_date > end_date:
        print(f"La fecha inicial es mayor a la fecha final.")
        exit()
    # Generar listas de fechas y URLs
    days_list = [(start_date + td(days=i)).strftime('%d%m%Y')
                 for i in range((end_date - start_date).days + 1)]
    urls = [f"{config('url')}{i}" for i in days_list]
    return urls, days_list

# Temporizador que cuenta hacia atrás entre cada consulta. 
def timer(segundos):
    """
    *Muestra un temporizador en la consola que cuenta hacia atrás desde el número
    de segundos especificado.*

    **Parámetros:** 
    - **segundos:** *Cantidad de segundos para el temporizador.*

    **No retorna ningún valor.**
    """

    for i in range(int(segundos), 0, -1):
        sys.stdout.write(f"\rConsultando siguiente fecha en : {i} segundos ")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r                                                            \n")

# Funcion principal para ejecutar el codigo: 
def main():
    try:
        url, date = url_embarques()
        logging.info("Consultando Fechas.")
        for u, d in zip(url, date):
            # Convertir la fecha de 'ddmmaaaa' a día, mes, año.
            day, month, year = get_dmy(d)
            logging.info(f"Consultando {config('name_api')} para el {day} de {month} del {year}.")
            
            path = f"{config('download_path')}{config('name_api')}\\{year}\\{month}\\"
            logging.info("Validando información.")

            # Validar y crear la ruta donde se guardarán los archivos
            validar_path(path)
            file_name = f"{config('name_dir')}_{d}"

            # Generar el nombre del archivo con la versión correspondiente
            new_name = get_version(file_name, path)
            logging.info("Información válida.")

            # Definir número máximo de reintentos
            max_retries = int(config('num_try'))
            attempt = 0
            success = False
            
            while attempt < max_retries and not success:
                attempt += 1
                logging.info(f"Intento {attempt} de {max_retries}.")
                
                try:
                    # Realizar la solicitud a la API
                    logging.info(f"Consultando API: {config('name_api')}. URL: {u}")
                    req = requests.get(u, auth=(config('user'), config('passw')))
                    req.raise_for_status()  # Lanza una excepción para códigos HTTP de error
                    logging.info("Obteniendo información.")
                    
                    data = req.json()
                    logging.info("Listo!")
                    
                    # Crea el documento
                    with open(new_name, 'w', encoding='utf-8') as json_file:
                        json.dump(data, json_file, ensure_ascii=False, indent=4)
                        logging.info(f"Documento guardado con éxito en: {new_name}")
                    
                    success = True  # Marca como exitoso si no hay excepciones
                    
                except requests.exceptions.RequestException as e:
                    logging.error(f"Error en la solicitud HTTP: {e}")
                    if attempt < max_retries:
                        logging.info(f"Reintentando en {config('time_sleep')} segundos...")
                        timer(config('time_sleep'))  # Esperar antes de reintentar
                    else:
                        logging.error("Número máximo de reintentos alcanzado. Pasando al siguiente URL.")
                        timer(config('time_sleep'))  # Esperar antes de reintentar
            
            # Activa temporizador para la siguiente consulta si la solicitud fue exitosa
            if success:
                timer(config('time_sleep'))

    except Exception as e:
        logging.error(f"Error en la ejecución del script: {e}")

    logging.info("Finalizado!")


# Ejecucion del codigo.
if __name__ == "__main__":
    main()