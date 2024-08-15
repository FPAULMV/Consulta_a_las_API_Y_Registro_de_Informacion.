import os
import json
import pyodbc
from decouple import config
from datetime import datetime as dt, timedelta as td

def get_dmy(fecha_str):
    meses_es = ["Enero", "Febrero", "Marzo", 
                "Abril", "Mayo", "Junio", 
                "Julio", "Agosto", "Septiembre", 
                "Octubre", "Noviembre", "Diciembre"]
    # Convertir la cadena de fecha en un objeto datetime
    fecha = dt.strptime(fecha_str, '%d%m%Y')
    # Obtener el día, mes y año
    month = meses_es[fecha.month - 1]
    year = fecha.year   
    return month, year

def get_dates(start_date=None, end_date=None):
    """
    *Genera una lista de fechas en formato 'ddmmaaaa' dentro de un rango de fechas proporcionado.*

    **Parámetros:**  
    - **start_date:** *Fecha de inicio en formato **'ddmmaaaa'****.* *Si no se proporciona, se usa el valor del archivo .env* **'query_days'***.*
    - **end_date:** *Fecha de fin en formato* **'ddmmaaaa'***.* *Si no se proporciona, se usa la fecha actual.*

    **Retorna:**  
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
    return days_list


# Función para leer y guardar el contenido de los archivos JSON en la base de datos
def guardar_json_en_sql(fecha, month, year):
    # Ruta de la carpeta donde se encuentran los archivos JSON
    carpeta_json = f"{config('download_path')}{config('name_api')}\\{year}\\{month}\\"
    archivos_json = [f for f in os.listdir(carpeta_json) if f.startswith(f'{config('name_dir')}_{fecha}') and f.endswith('.json')]
    
    if not archivos_json:
        print(f'No se encontraron archivos para la fecha {fecha}.')
        return
    
    for archivo_json in archivos_json:
        ruta_completa = os.path.join(carpeta_json, archivo_json)
        
        # Leer el archivo JSON
        with open(ruta_completa, 'r', encoding='utf-8') as file:
            datos = json.load(file)
            print(f"Leyendo archivo {archivo_json}.")
        # Insertar los datos en la tabla.
        print(f"Grabando datos en la tabla. \n")
        for item in datos:
            cursor.execute(f'''
                INSERT INTO {config('table_name')} (
                    Icte, ElargaCto, ElargaDest, EcortaProd, EcortaPres, ElargaMedio,
                    Ivehiculo, ElargaTransport, Itonel, CtonelProg, Fhprog, ElargaAtencion,
                    KnumOrden, Icto, Fprog, FprogOper, Bandera, Echofer, Kturno, KfolioPedido, doc_referencia
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item['Icte'],
                item['ElargaCto'],
                item['ElargaDest'],
                item['EcortaProd'],
                item['EcortaPres'],
                item['ElargaMedio'],
                item['Ivehiculo'],
                item['ElargaTransport'],
                item['Itonel'],
                item['CtonelProg'],
                item['Fhprog'],
                item['ElargaAtencion'],
                item['KnumOrden'],
                item['Icto'],
                dt.strptime(item['Fprog'], '%d/%m/%Y'),  # Convierte el string a fecha
                item['FprogOper'],
                item['Bandera'],
                item['Echofer'],
                item['Kturno'],
                item['KfolioPedido'],
                archivo_json  # Se añade el nombre del archivo
            ))
        
        conn.commit()
        print(f'Datos del archivo {ruta_completa} guardados en la base de datos.  \n')

# Ejemplo de uso

def main():# Configuración de la conexión a SQL Server
    print(f"Conectando con SQLServer")
    conn = pyodbc.connect(
        f"DRIVER={config('driver')};"
        f"SERVER={config('server')};"
        f"DATABASE={config('database')};"
        f"UID={config('user_name')};"
        f"PWD={config('password')}"
    )
    cursor = conn.cursor()

    date = get_dates()
    print(f"Obteniendo fecha. \n")
    for d in date:
        month, year = get_dmy(d)
        print(f"Leyendo documentos de la carpeta {month} - {year}.")
        guardar_json_en_sql(d, month, year)

    print(f"Finalizado!")
    # Cerrar la conexión
    cursor.close()
    conn.close()
    print(f"Conexion finalizada.")

# Ejecucion del codigo.
if __name__ == "__main__":
    main()