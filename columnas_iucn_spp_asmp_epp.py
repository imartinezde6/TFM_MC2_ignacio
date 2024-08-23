# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:04:55 2024

@author: nacho
"""
# Programa para poder tener columnas de cada programa de cría en cautividad o IUCN (reintroducciones)
# para poder saber en que programa está incluida cada especie. Se añade un "1" en las filas de las especies que 
# están incluidas en el programa de la columna en cuestión
#%%
# Busca coincidencias en los dos excel y añade 1 a la columna de IUCN del excel de los programas de cría en cautividad
import pandas as pd

df_unido_zaa = pd.read_excel('unido_eaza_spp_zaa_buen_formato_2.xlsx')
df_otro_excel = pd.read_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx')

coincidencias = df_unido_zaa['Nombre_Cientifico'].isin(df_otro_excel['Nombre_Cientifico'])

df_unido_zaa.loc[coincidencias,'IUCN']=1

df_unido_zaa.to_excel('unido_eaza_spp_zaa_buen_formato_2.xlsx', index=False)

#%% Para las coincidencias de especies que están en el ZAA
df_unido_zaa = pd.read_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx')
df_otro_excel = pd.read_excel('ZAA.xlsx')

coincidencias = df_unido_zaa['Nombre_Cientifico'].isin(df_otro_excel['Nombre_Cientifico'])

df_unido_zaa.loc[coincidencias,'ZAA']=1

df_unido_zaa.to_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx', index=False)
#%% Para las coincidencias de especies que están en el EAZA
df_unido_zaa = pd.read_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx')
df_otro_excel = pd.read_excel('EAZA.xlsx')

coincidencias = df_unido_zaa['Nombre_Cientifico'].isin(df_otro_excel['Nombre_Cientifico'])

df_unido_zaa.loc[coincidencias,'EAZA']=1

df_unido_zaa.to_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx', index=False)

#%% Para las coincidencias de especies que están en el SPP
df_unido_zaa = pd.read_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx')
df_otro_excel = pd.read_excel('SPP.xlsx')

coincidencias = df_unido_zaa['Nombre_Cientifico'].isin(df_otro_excel['Nombre_Cientifico'])

df_unido_zaa.loc[coincidencias,'SPP']=1

df_unido_zaa.to_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx', index=False)