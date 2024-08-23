# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:48:18 2024

@author: nacho
"""
# Conexión con la base de datos de SPP para extraer el listado de especies de este programa de cría en cautividad
from bs4 import BeautifulSoup
import re
import requests
website=('https://ams.aza.org/eweb/DynamicPage.aspx?Site=AZA&WebKey=2b7e3aaf-dc68-49da-ab2e-0dc83ef91a5d&FromSearchControl=Yes')
result=requests.get(website)
content=result.text
soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())

texto=soup.find('div', class_='bodyTXT').get_text()
print(texto)

#%%

texto=soup.find('div', class_='bodyTXT').get_text()
patron = re.compile(r'\r\n\n\n\n\n\n\n\n(.+?)\r\n', re.DOTALL)

nombres_especies = patron.findall(texto)

# Imprimir los nombres de las especies
for nombre_especie in nombres_especies:
    print(nombre_especie.strip())

