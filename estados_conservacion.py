# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:35:11 2024

@author: nacho
"""
# Conexión por medio de la API de la IUCN para poder extraer los estados de conservación
# de cada especie de los listados obtenidos
import requests
import pandas as pd

def obtener_estado_conservacion_especie(nombre_cientifico):
    url_base = "http://apiv3.iucnredlist.org/api/v3/species/"
    api_key = "806bc11f9d49a2c28690b7ba41bad7d49e2d756a1b122444e17cb2b77518f243"

    url = f"{url_base}{nombre_cientifico}?token={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and data["result"]:
            estado_conservacion = data["result"][0]["category"]
            return estado_conservacion
        else:
            print(f"No se encontró información para {nombre_cientifico} en la API de la UICN Red List.")
            return None
    else:
        print(f"Error al obtener el estado de conservación para {nombre_cientifico}. Código de respuesta: {response.status_code}")
        return None

excel_file_path = "nombres_especies_pdfgenerales_buen_formato.xlsx"
excel = pd.read_excel(excel_file_path)
especies = excel['Nombre Científico']

conservacion_column = []

for especie in especies:
    estado_conservacion = obtener_estado_conservacion_especie(especie)
    conservacion_column.append(estado_conservacion)

excel['Estado Conservacion'] = conservacion_column

excel.to_excel(excel_file_path, index=False)

print(excel)
#%%
import requests
import pandas as pd

def obtener_estado_conservacion_especie(nombre_cientifico):
    url_base = "http://apiv3.iucnredlist.org/api/v3/species/"
    api_key = "806bc11f9d49a2c28690b7ba41bad7d49e2d756a1b122444e17cb2b77518f243"

    url = f"{url_base}{nombre_cientifico}?token={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and data["result"]:
            estado_conservacion = data["result"][0]["category"]
            return estado_conservacion
        else:
            print(f"No se encontró información para {nombre_cientifico} en la API de la UICN Red List.")
            return None
    else:
        print(f"Error al obtener el estado de conservación para {nombre_cientifico}. Código de respuesta: {response.status_code}")
        return None

excel_file_path = "unido_eaza_spp_zaa_buen_formato.xlsx"
excel = pd.read_excel(excel_file_path)
especies = excel['Nombre Científico']

conservacion_column = []

for especie in especies:
    estado_conservacion = obtener_estado_conservacion_especie(especie)
    conservacion_column.append(estado_conservacion)

excel['Estado Conservacion'] = conservacion_column

excel.to_excel(excel_file_path, index=False)

print(excel)







