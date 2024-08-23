# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:40:04 2024

@author: nacho
"""

import pandas as pd
df_cambios_categoria = pd.read_excel('cambios_categoria.xlsx')
df_especies_iucn= pd.read_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx')

coincidencias = df_especies_iucn['Nombre_Cientifico'].isin(df_cambios_categoria['Scientific name'])

especies_coincidentes = df_especies_iucn[coincidencias]
especies=especies_coincidentes['Nombre_Cientifico']

for especie in especies:
    estado_antiguo = df_cambios_categoria.loc[df_cambios_categoria['Scientific name'] == especie, 'antigua'].values[0]
    estado_nuevo = df_cambios_categoria.loc[df_cambios_categoria['Scientific name'] == especie, 'nueva'].values[0]

    df_especies_iucn.loc[df_especies_iucn['Nombre_Cientifico'] == especie, 'estado_antiguo'] = estado_antiguo
    df_especies_iucn.loc[df_especies_iucn['Nombre_Cientifico'] == especie, 'estado_nuevo'] = estado_nuevo

df_especies_iucn.to_excel('nombres_especies_pdfgenerales_buen_formato_2.xlsx', index=False)
#%%
import pandas as pd
df_cambios_categoria = pd.read_excel('cambios_categoria.xlsx')
df_especies_iucn= pd.read_excel('unido_eaza_spp_zaa_buen_formato_2.xlsx')

coincidencias = df_especies_iucn['Nombre_Cientifico'].isin(df_cambios_categoria['Scientific name'])

especies_coincidentes = df_especies_iucn[coincidencias]
especies=especies_coincidentes['Nombre_Cientifico']

for especie in especies:
    estado_antiguo = df_cambios_categoria.loc[df_cambios_categoria['Scientific name'] == especie, 'antigua'].values[0]
    estado_nuevo = df_cambios_categoria.loc[df_cambios_categoria['Scientific name'] == especie, 'nueva'].values[0]

    df_especies_iucn.loc[df_especies_iucn['Nombre_Cientifico'] == especie, 'estado_antiguo'] = estado_antiguo
    df_especies_iucn.loc[df_especies_iucn['Nombre_Cientifico'] == especie, 'estado_nuevo'] = estado_nuevo

df_especies_iucn.to_excel('unido_eaza_spp_zaa_buen_formato_2.xlsx', index=False)







