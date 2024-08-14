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
**Requiere:** una fecha como str en formato 'ddmmaaaa'.  
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
Valida si una ruta a directorio existe. Si no, la crea.
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
     El nombre base que llevara el archvio descargado, a este se le agregara *'_V_'* mas, el numero de version *'1'*.
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
Genera URL's para consultar a la API y una lista de fechas en formato 'ddmmaaaa' dentro de un rango de fechas proporcionado.  
```python
def url_embarques(start_date: str =None, end_date: str =None):
```  

**Requiere:**  
   - **start_date:** *(como str)* *(opcional)*
   - **end_date:** *(como str)* *(opcional)*













