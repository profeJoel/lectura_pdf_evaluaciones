import os
import tabula
import pdfquery
import pandas as pd

from scrape_pdf import recuperar_docente_asignatura

DIRECTORIO = "JoelTorres"

def leer_documento(documento):
    print(documento)
    try:
        datos_tabulados = tabula.read_pdf(documento, pages='all', encoding='cp1252')
    except:
        datos_tabulados = None
        print("Error en la lectura")
    print(type(datos_tabulados))
    return datos_tabulados 

def archivos_directorio():
    archivos = os.listdir(DIRECTORIO)
    return archivos

if __name__ == "__main__":
    
    archivos = archivos_directorio()
    for archivo in archivos:
        nombre, asignatura = recuperar_docente_asignatura(DIRECTORIO, archivo)
        datos_crudos = leer_documento(DIRECTORIO + "/" + archivo)
        # desde acá ya se puede manipular la información
        
        print(nombre + " -> " + asignatura)
        for dc in datos_crudos:
            print(dc.describe())
        