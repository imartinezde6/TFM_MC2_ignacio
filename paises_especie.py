# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:01:40 2024

@author: nacho
"""
# Programa que conecta con la API de la IUCN para saber que especies han sido introducidas en algún país
#%%

###################################

# Este programa no añade nada al excel ya que crea diccionarios

####################################



# PARA GUARDAR UN LISTADO DE LAS ESPECIES QUE HAN SIDO REINTRODUCIDAS
import requests
import pandas as pd

def obtener_especies_introducidas(nombre_especie, api_key):
    url = f"http://apiv3.iucnredlist.org/api/v3/species/countries/name/{nombre_especie}?token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and data["result"]:
            for country in data["result"]:
                if country["origin"] == "Introduced":
                    return nombre_especie
        else:
            print(f"No se encontró información de países de ocurrencia para la especie {nombre_especie}.")
    else:
        print(f"Error al obtener información de países de ocurrencia para la especie {nombre_especie}. Código de respuesta: {response.status_code}")

    return None

api_key = "806bc11f9d49a2c28690b7ba41bad7d49e2d756a1b122444e17cb2b77518f243"
excel_file_path = "unido_eaza_spp_zaa_buen_formato.xlsx"
excel = pd.read_excel(excel_file_path)  
especies = excel['Nombre Científico']

nombres_especies_introducidas = []  

for especie in especies:
    especie_introducida = obtener_especies_introducidas(especie, api_key)
    if especie_introducida:
        nombres_especies_introducidas.append(especie_introducida)
        print(f"La especie {especie_introducida} ha sido introducida en algún país.")

print("Nombres de especies introducidas:")
print(nombres_especies_introducidas)
#%% PASAMOS ESTA INFORMACION AL EXCEL
# En algunas especies, de "nombres_especies_introducidas" habia espacios al final del nombre y eso
# hacia que no encontrara coincidencia. Como solo eran siete, se han quitado a mano. Si se vuelve a 
# ejecutar el programa habra que quitarlos a mano otra vez
import pandas as pd

df = pd.read_excel('unido_eaza_spp_zaa_buen_formato_2.xlsx')
for especie in nombres_especies_introducidas:
    df.loc[df['Nombre_Cientifico'] == especie, 'Reintroduccion_pais'] = 1

df.to_excel('unido_eaza_spp_zaa_buen_formato_2.xlsx', index=False)

#%%PARA LAS ESPECIES DE LAS ASOCIACIONES
import requests
import pandas as pd

def obtener_especies_introducidas(nombre_especie, api_key):
    url = f"http://apiv3.iucnredlist.org/api/v3/species/countries/name/{nombre_especie}?token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and data["result"]:
            for country in data["result"]:
                if country["origin"] == "Introduced":
                    return nombre_especie
        else:
            print(f"No se encontró información de países de ocurrencia para la especie {nombre_especie}.")
    else:
        print(f"Error al obtener información de países de ocurrencia para la especie {nombre_especie}. Código de respuesta: {response.status_code}")

    return None

api_key = "806bc11f9d49a2c28690b7ba41bad7d49e2d756a1b122444e17cb2b77518f243"
excel_file_path = "nombres_especies_pdfgenerales_buen_formato.xlsx"
excel = pd.read_excel(excel_file_path)  
especies = excel['Nombre Científico']

nombres_especies_introducidas = []  

for especie in especies:
    especie_introducida = obtener_especies_introducidas(especie, api_key)
    if especie_introducida:
        nombres_especies_introducidas.append(especie_introducida)
        print(f"La especie {especie_introducida} ha sido introducida en algún país.")

print("Nombres de especies introducidas:")
print(nombres_especies_introducidas)

#%% PASAMOS ESTA INFORMACION AL EXCEL

import pandas as pd

df = pd.read_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx')
for especie in nombres_especies_introducidas:
    df.loc[df['Nombre_Cientifico'] == especie, 'Reintroduccion_pais'] = 1

df.to_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx', index=False)




