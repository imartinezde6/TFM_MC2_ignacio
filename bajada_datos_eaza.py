# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:28:42 2024

@author: nacho
"""
# Conexión con la web de eaza para extraer el listado de especies de este programa de cría en cautividad

#SI SE VUELVE A EJECTUTAR NO VA A FUNCIONAR PORQUE HAY COSAS QUE SE HA QUITADO A MANO DESDE EL 
# VARIABLE EXPLORER
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

website = 'https://www.eaza.net/conservation/programmes/eep-pages/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'html.parser')

texto=soup.find('div', class_='blocks').get_text()
print(texto)
#%%
#se descarga toda la pagina, por esto que igual que en zaa, abrimos desde el variable
#explorer y eliminamos directamente lo que no nos interesa
filas = [fila.strip() for fila in texto.split('•') if fila]

df = pd.DataFrame(filas, columns=['Nombre Común'])

def extraer_contenido_parentesis(texto):
    match = re.search(r'\((.*?)\)', texto)
    return match.group(1) if match else None
df['Nombre Científico'] = df['Nombre Común'].apply(extraer_contenido_parentesis)

df['Nombre Común'] = df['Nombre Común'].replace(to_replace=r'\(.*?\)', value='', regex=True).str.strip()
df = df.dropna()
print(df)
df.to_excel('eaza_especies_tratado2_bajado_python.xlsx', index=False)


