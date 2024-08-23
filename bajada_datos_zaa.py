# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:16:09 2024

@author: nacho
"""
# Conexión con la web de zaa para extraer el listado de especies de este programa de cría en cautividad

from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

website = 'https://www.zooaquarium.org.au/public/Public/Conservation/Species-Programs.aspx?hkey=c750d8b3-8493-4d92-994c-1bdcc976d23a'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'html.parser')

texto=soup.find('div', class_='col-sm-4').get_text()
species_info = re.findall(r'(.+?)\s*(.+?)\nSpecies Coordinator:(.+?)(?=\n|$)', texto)

df = pd.DataFrame(species_info, columns=['Species', 'Binomial Name', 'Species Coordinator'])

print(df)
#%%
website = 'https://www.zooaquarium.org.au/public/Public/Conservation/Species-Programs.aspx?hkey=c750d8b3-8493-4d92-994c-1bdcc976d23a'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'html.parser')
texto=soup.find('div', class_='ContentPanel').get_text()

print(texto)
#eliminamos directamente el primer parrafo que no nos interea abriendo y borrando desde el variable explorer
#%%


archivo_excel_entrada = 'zaa_especies_bajadas2_copypaste_from_python.xlsx'
df = pd.read_excel(archivo_excel_entrada, header=None)
nuevos_datos = []

for i in range(0, len(df), 3):
    if i + 2 < len(df):
        nombre_cientifico = df.iloc[i, 0]
        nombre_comun = df.iloc[i + 1, 0]
        zoo = df.iloc[i + 2, 0]

        zoo = zoo.replace("Species Coordinator:", "").strip()

        nuevos_datos.append([nombre_cientifico, nombre_comun, zoo])

nuevo_df = pd.DataFrame(nuevos_datos, columns=['Nombre Común', 'Nombre Científico', 'Coordinador'])

nuevo_df.to_excel('zaa_especies_tratado2_bajado_python.xlsx', index=False)

print(nuevo_df)








