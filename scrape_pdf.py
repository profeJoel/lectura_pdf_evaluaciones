import os
import pdfquery
import pandas as pd

#from main import DIRECTORIO, archivos_directorio

def recuperar_docente_asignatura(directorio, documento):
    pdf = pdfquery.PDFQuery(directorio + '/' + documento)
    pdf.load()
    #print(directorio + "/aux_XML/" + documento[:-4] + "_XML.txt")
    #pdf.tree.write(directorio + "/aux_XML/" + documento[:-4] + "_XML.txt", pretty_print = True)
    pdf.tree.write(documento[:-4] + "_XML.txt", pretty_print = True)
    pdf.load(0)
    nombre = pdf.pq('LTTextLineHorizontal:overlaps_bbox("46.016, 652.184, 201.956, 658.184")').text()
    asignatura = pdf.pq('LTTextLineHorizontal:overlaps_bbox("46.016, 583.872, 197.69, 589.872")').text()
    
    os.remove(documento[:-4] + "_XML.txt") #Opcional para eliminar archivos temporales XML
        
    #print(nombre + " -> " + asignatura)
    return nombre, asignatura

if __name__ == "__main__":
    pass
"""
    archivos = archivos_directorio()
    pdf = pdfquery.PDFQuery(DIRECTORIO + '/' + archivos[0])
    pdf.load()
    #print(archivos[0][:-4] + "_XML.txt")
    pdf.tree.write(archivos[0][:-4] + "_XML.txt", pretty_print = True)
    
    pdf.load(0)
    nombre = pdf.pq('LTTextLineHorizontal:overlaps_bbox("46.016, 652.184, 201.956, 658.184")').text()
    asignatura = pdf.pq('LTTextLineHorizontal:overlaps_bbox("46.016, 583.872, 197.69, 589.872")').text()
        
    print(nombre + " -> " + asignatura)
"""