# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:45:07 2024

@author: nacho
"""
# Programa para sacar las instituciones/zoos/acuarios encargadas de las especies extraidas en el programa bajada_datos_eaza.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

especies = [
    "Desertas wolf spider",
    "Gooty sapphire ornamental spider",
    "Poeciliids",
    "Pupfishes",
    "Seychelles giant millipede",
    "Toothcarps",
    "Montseny brook newt",
    "Mountain chicken frog",
    "Egyptian tortoise",
    "European pond turtle",
    "Galapagos giant tortoise",
    "Henkel’s leaf-tailed gecko",
    "Mauremys sps",
    "Ploughshare tortoise",
    "Roti Island snake-necked turtle",
    "African penguin",
    "Black hornbill",
    "Dalmatian pelican",
    "Emei Shan liocichla",
    "Great hornbill",
    "Hill mynas complex",
    "Javan green magpie",
    "Gentoo penguin",
    "Grebe",
    "King penguin",
    "Lesser white-fronted goose",
    "Magellanic penguin",
    "Meller’s duck",
    "Red-billed chough",
    "Rockhopper",
    "Scaly-sided merganser",
    "Santa Cruz ground dove",
    "Scops owls",
    "Seaduck",
    "Snowy owl",
    "Ural owl",
    "White-winged duck",
    "Aye aye",
    "Black-crested mangabey",
    "Blue-eyed black lemur",
    "Buffy headed marmoset",
    "Buffy tufted ear marmoset",
    "Coquerel's sifaka",
    "Cotton-top tamarin",
    "Emperor tamarin",
    "Goeldi's monkey",
    "Guinea baboon",
    "Hamadryas baboon",
    "Invasive marmoset",
    "Lar gibbon",
    "Lion-tailed macaque",
    "Northern galago",
    "Pileated gibbon",
    "Pygmy marmoset",
    "Red-bellied lemur",
    "Roloway monkey",
    "Siamang",
    "Silvery marmoset",
    "White-fronted marmoset",
    "Maned wolf",
    "Spotted hyena",
    "Striped hyena",
    "Anoa",
    "Aoudad",
    "Bactrian wapiti",
    "Blesbok",
    "Chinese goral",
    "Cuvier's gazelle",
    "Eastern black rhino",
    "Eld’s deer",
    "European bison",
    "Forest reindeer",
    "Gaur",
    "Giraffe",
    "Grevy's zebra",
    "Hartmann's mountain zebra",
    "Lesser chevrotain",
    "Michie's tufted deer",
    "Mhorr gazelle",
    "Musk ox",
    "Okapi",
    "Przewalski's horse",
    "Somali wild ass",
    "Southern pudu",
    "Takin",
    "Turkmenian kulan",
    "Turkmenian markhor",
    "Urial"
]

base_url = "https://www.eaza.net/conservation/programmes/eep-pages/"

enlaces_especies = {}

for especie in especies:
    enlace_especie = base_url + especie.lower().replace(' ', '-') + "-eep/"
    enlaces_especies[especie] = enlace_especie

def obtener_informacion_especie(especie, enlace):
    response = requests.get(enlace)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        texto_pagina = soup.get_text()
        inicio = texto_pagina.find("Institution:") + len("Institution:")
        fin = texto_pagina.find("EAZA Member Area", inicio)

        if inicio != -1 and fin != -1:
            institucion = texto_pagina[inicio:fin].strip()
            return {"Institucion": institucion}
    
    if response.status_code == 404:
        return {"Institucion": f"No hay página disponible para {especie}. Código de estado: 404"}
    else:
        return {"Institucion": f"No se pudo acceder a la página de {especie}. Código de estado: {response.status_code}"}

informacion_especies = {}

for especie, enlace in enlaces_especies.items():
    informacion_especies[especie] = obtener_informacion_especie(especie, enlace)

for especie, info in informacion_especies.items():
    print(f"Especie: {especie}")
    print(f"Institucion: {info['Institucion']}")
    print("-" * 30)

informacion_especies = {}

for especie, enlace in enlaces_especies.items():
    informacion_especies[especie] = obtener_informacion_especie(especie, enlace)

df2 = pd.DataFrame.from_dict(informacion_especies, orient='index', columns=['Institucion'])

df2.to_excel('eaza_intituciones.xlsx')

print(df2)









