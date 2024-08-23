# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:11:01 2024

@author: nacho
"""
# Programa que saca un listado de las espcies que se encuentran en los documentos de la IUCN analizados

#%% 2008
import fitz  
import re
import pandas as pd

def extract_intro_text_from_pdf(pdf_path, start_page=12):
    intro_text_list = []

    with fitz.open(pdf_path) as doc:
        if start_page <= doc.page_count:
            for page_number in range(start_page - 1, doc.page_count):
                page = doc[page_number]
                text = page.get_text("text")

                intro_positions = [match.start() for match in re.finditer('Introduction', text)]

                for intro_position in intro_positions:
                    content_after_intro = text[intro_position:]

                    match = re.search(r'\(([^)]+)', content_after_intro)

                    if match:
                        intro_text = match.group(1).strip()
                        intro_text_list.append({'Page': page_number + 1, 'Especie': intro_text})

    return pd.DataFrame(intro_text_list)

pdf_path_to_process = 'rsg-book-2008.pdf'

df_result = extract_intro_text_from_pdf(pdf_path_to_process, start_page=12)

print(df_result)

df_result.to_excel('nombres_especies_pdfgeneral_2008.xlsx', index=False)




#%% 2010

pdf_path_to_process = 'rsg-book-2010.pdf'

df_result = extract_intro_text_from_pdf(pdf_path_to_process, start_page=14)

print(df_result)

df_result.to_excel('nombres_especies_pdfgeneral_2010.xlsx', index=False)


#%% 2011

pdf_path_to_process = 'rsg-book-2011.pdf'

df_result = extract_intro_text_from_pdf(pdf_path_to_process, start_page=16)

print(df_result)

df_result.to_excel('nombres_especies_pdfgeneral_2011.xlsx', index=False)


#%% 2013

pdf_path_to_process = 'rsg-book-2013.pdf'

df_result = extract_intro_text_from_pdf(pdf_path_to_process, start_page=16)

print(df_result)
df_result.to_excel('nombres_especies_pdfgeneral_2013.xlsx', index=False)


#%% 2016

pdf_path_to_process = 'rsg-book-2016.pdf'

df_result = extract_intro_text_from_pdf(pdf_path_to_process, start_page=16)

print(df_result)
df_result.to_excel('nombres_especies_pdfgeneral_2016.xlsx', index=False)



#%% 2018

pdf_path_to_process = '2018-006-En.pdf'

df_result = extract_intro_text_from_pdf(pdf_path_to_process, start_page=16)

print(df_result)

df_result.to_excel('nombres_especies_pdfgeneral_2018.xlsx', index=False)


#%% 2021

pdf_path_to_process = 'CTSG_Book_Issue_7_Feb_2021.pdf'

df_result = extract_intro_text_from_pdf(pdf_path_to_process, start_page=16)

print(df_result)

df_result.to_excel('nombres_especies_pdfgeneral_2021.xlsx', index=False)












