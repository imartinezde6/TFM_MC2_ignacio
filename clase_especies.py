# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:45:15 2024

@author: nacho
"""
# Conexión por medio de la API de la IUCN para poder extraer los taxones
# de cada especie de los listados obtenidos
import requests
import pandas as pd

def obtener_clase_especie(nombre_especie):
    url_base = "http://apiv3.iucnredlist.org/api/v3/species/"
    api_key = "806bc11f9d49a2c28690b7ba41bad7d49e2d756a1b122444e17cb2b77518f243"

    url = f"{url_base}{nombre_especie}?token={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and data["result"]:
            clasificacion_taxonomica = data["result"][0]["class"]
            return clasificacion_taxonomica
        else:
            print(f"No se encontró información para la especie {nombre_especie} en la API de la UICN Red List.")
            return None
    else:
        print(f"Error al obtener la clasificación taxonómica para la especie {nombre_especie}. Código de respuesta: {response.status_code}")
        return None

excel_file_path = "nombres_especies_pdfgenerales_buen_formato.xlsx"
excel = pd.read_excel(excel_file_path)
especies = excel['Nombre Científico']

clase_column=[]
for especie in especies:
    estado_conservacion = obtener_clase_especie(especie)
    clase_column.append(estado_conservacion)

excel['Clase'] = clase_column

excel.to_excel(excel_file_path, index=False)

print(excel)
#%%
import requests
import pandas as pd

def obtener_clase_especie(nombre_especie):
    url_base = "http://apiv3.iucnredlist.org/api/v3/species/"
    api_key = "806bc11f9d49a2c28690b7ba41bad7d49e2d756a1b122444e17cb2b77518f243"

    url = f"{url_base}{nombre_especie}?token={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and data["result"]:
            clasificacion_taxonomica = data["result"][0]["class"]
            return clasificacion_taxonomica
        else:
            print(f"No se encontró información para la especie {nombre_especie} en la API de la UICN Red List.")
            return None
    else:
        print(f"Error al obtener la clasificación taxonómica para la especie {nombre_especie}. Código de respuesta: {response.status_code}")
        return None

excel_file_path = "unido_eaza_spp_zaa_buen_formato.xlsx"
excel = pd.read_excel(excel_file_path)
especies = excel['Nombre Científico']

clase_column=[]
for especie in especies:
    estado_conservacion = obtener_clase_especie(especie)
    clase_column.append(estado_conservacion)

excel['Clase'] = clase_column

excel.to_excel(excel_file_path, index=False)

print(excel)




