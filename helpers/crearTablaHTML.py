""" def crearTabla(dataFrame,nombreTabla):
    archivoHTML= dataFrame.to_html()
    archivo=open(f"/tables/{nombreTabla}.html","w")
    archivo.write(
        '''
            <html>
                <head>
                    <title>tabla aire</title>
                </head>
                <body>
                ''')
    archivo.write(archivoHTML)
    archivo.write(
                    '''
                </body>
            </html>
        '''
    )
    
     """
     
import os

def crearTabla(dataFrame, nombreTabla):
    directorio = "tables"
    # Crear el directorio si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    ruta_archivo = os.path.join(directorio, f"{nombreTabla}.html")
    archivoHTML = dataFrame.to_html()

    with open(ruta_archivo, "w") as archivo:
        archivo.write(
            '''
            <html>
                <head>
                    <title>tabla aire</title>
                </head>
                <body>
            '''
        )
        archivo.write(archivoHTML)
        archivo.write(
            '''
                </body>
            </html>
            '''
        )
