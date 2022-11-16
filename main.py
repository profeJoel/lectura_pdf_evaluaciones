import os
import tabula

def leer_documento(documento):
    print(documento)
    try:
        datos_tabulados = tabula.read_pdf(documento, pages='all', encoding='cp1252')
    except:
        datos_tabulados = None
        print("Error en la lectura")
        
    return datos_tabulados 

if __name__ == "__main__":
    
    DIRECTORIO = "JoelTorres"
    archivos = os.listdir(DIRECTORIO)
    for archivo in archivos:
        datos_crudos = leer_documento(DIRECTORIO + "/" + archivos[0])
        # desde acá ya se puede manipular la información
        print(datos_crudos)