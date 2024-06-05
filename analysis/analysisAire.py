import pandas as pd
from data.generadorAire import generarDatosCalidadAire
from helpers.crearTablaHTML import crearTabla

def construirAireDataFrame():
    datosAire=generarDatosCalidadAire()
    
    #generamos el dataframe
    
    aireDataFrame = pd.DataFrame(datosAire,columns = ["nombre","comuna","ica",'fecha','correo'])
   
   #generamos el recurso HTML
   
    crearTabla(aireDataFrame,"datosAire")
    print(aireDataFrame)
    
construirAireDataFrame()    