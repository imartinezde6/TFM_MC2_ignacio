# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:40:43 2024

@author: nacho
"""
# Conexión por medio de la API de la IUCN para poder extraer las acciones de conservación aplicadas
# a cada especie de los listados obtenidos
#%%
import requests
import pandas as pd

def obtener_medidas_conservacion_por_nombre(nombre_especie, api_key):
    url = f"http://apiv3.iucnredlist.org/api/v3/measures/species/name/{nombre_especie}?token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and data["result"]:
            medidas_conservacion = data["result"]
            return medidas_conservacion
        else:
            print(f"No se encontró información de medidas de conservación para la especie {nombre_especie}.")
            return None
    else:
        print(f"Error al obtener información de medidas de conservación para la especie {nombre_especie}. Código de respuesta: {response.status_code}")
        return None

api_key = "806bc11f9d49a2c28690b7ba41bad7d49e2d756a1b122444e17cb2b77518f243"
excel_file_path = "nombres_especies_pdfgenerales_buen_formato.xlsx"
excel = pd.read_excel(excel_file_path)
especies = excel['Nombre Científico']

conservation_actions_columns = [
    '1.1', '1.2', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3', '3.4', '4.1', '4.2', '4.3', '5.1',
    '5.2', '5.3', '5.4', '6.1', '6.2', '6.3', '6.4', '6.5'
]

conservation_actions_df = pd.DataFrame(columns=['Nombre Científico'] + conservation_actions_columns)

for especie in especies:
    medidas_conservacion_especie = obtener_medidas_conservacion_por_nombre(especie, api_key)
    row = {'Nombre Científico': especie}

    if medidas_conservacion_especie is not None:
        for medida in medidas_conservacion_especie:
            codigo = medida['code']
            if codigo in conservation_actions_columns:
                row[codigo] = 1

                if '.' in codigo:
                    parent_code, child_code = codigo.split('.')
                    row[parent_code] = 1

    conservation_actions_df = conservation_actions_df.append(row, ignore_index=True)

conservation_actions_df.to_excel('acciones_conservacion_por_especie.xlsx', index=False)
##############################

# ESTE PROGRAMA GENERA UN EXCEL NUEVO QUE LUEGO HE COPIADO Y PEGADO EN EL EXCEL ORIGINAL

##############################
#%%
import requests
import pandas as pd
##############################

# ESTE PROGRAMA GENERA UN EXCEL NUEVO QUE LUEGO HE COPIADO Y PEGADO EN EL EXCEL ORIGINAL

##############################
def obtener_medidas_conservacion_por_nombre(nombre_especie, api_key):
    url = f"http://apiv3.iucnredlist.org/api/v3/measures/species/name/{nombre_especie}?token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and data["result"]:
            medidas_conservacion = data["result"]
            return medidas_conservacion
        else:
            print(f"No se encontró información de medidas de conservación para la especie {nombre_especie}.")
            return None
    else:
        print(f"Error al obtener información de medidas de conservación para la especie {nombre_especie}. Código de respuesta: {response.status_code}")
        return None

api_key = "806bc11f9d49a2c28690b7ba41bad7d49e2d756a1b122444e17cb2b77518f243"
excel_file_path = "unido_eaza_spp_zaa_buen_formato.xlsx"
excel = pd.read_excel(excel_file_path)
especies = excel['Nombre Científico']

conservation_actions_columns = [
    '1.1', '1.2', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3', '3.4', '4.1', '4.2', '4.3', '5.1',
    '5.2', '5.3', '5.4', '6.1', '6.2', '6.3', '6.4', '6.5'
]

conservation_actions_df = pd.DataFrame(columns=['Nombre Científico'] + conservation_actions_columns)

for especie in especies:
    medidas_conservacion_especie = obtener_medidas_conservacion_por_nombre(especie, api_key)
    row = {'Nombre Científico': especie}

    if medidas_conservacion_especie is not None:
        for medida in medidas_conservacion_especie:
            codigo = medida['code']
            if codigo in conservation_actions_columns:
                row[codigo] = 1

                if '.' in codigo:
                    parent_code, child_code = codigo.split('.')
                    row[parent_code] = 1

    conservation_actions_df = conservation_actions_df.append(row, ignore_index=True)

conservation_actions_df.to_excel('acciones_conservacion_por_especie2.xlsx', index=False)

