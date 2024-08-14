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
- ***get_dmy()***
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
