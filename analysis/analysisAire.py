import pandas as pd
import  matplotlib.pyplot as plt
from data.generators.generadorAire import generarDatosCalidadAire
from helpers.crearTablaHTML import crearTabla

def construirAireDataFrame():
    datosAire=generarDatosCalidadAire()
    
    #generamos el dataframe
    
    aireDataFrame = pd.DataFrame(datosAire,columns = ["nombre","comuna","ica",'fecha','correo'])
   
   #generamos el recurso HTML
   
    crearTabla(aireDataFrame,"datosAire")
    #print(aireDataFrame)
    #Limpiando el dataFrame
    #reemplazando valores
    aireDataFrame.replace('sin',pd.NA,inplace=True)
    #eliminar registros que no cumplen el criterio
    aireDataFrame.dropna(inplace=True)
    #print(aireDataFrame)
    #filtrar Datos
    #filtrar es aplicar condiciones logicas
    #que permitan analizar la informacion del dataframe DF
    filtroCalidadDEAireBueno=aireDataFrame.query("(ica>=10)and(ica<40)").value_counts()
    filtroCalidadDEAireMedio=aireDataFrame.query("(ica>=40)and(ica<50)").value_counts()
    filtroCalidadDEAireMalo=aireDataFrame.query("(ica>=50)and(ica<100)").value_counts()
    
   #ORDENANDO LOS DATOS PARA GRAFICARLOS
    datosOrdenadosDeAire=aireDataFrame.groupby('comuna')['ica'].mean()
    print(datosOrdenadosDeAire)
    
  #grafico la informacion
    plt.figure(figsize=(20,20))  
    datosOrdenadosDeAire.plot(kind='bar',color='green')
    plt.title("Indice de contaminacion del aire por comuna en medellin")
    plt.xlabel("comuna")
    plt.ylabel("ICA")
    plt.grid(True)
    plt.savefig("./assets/img/calidadDeAire.png",format='png',dpi=300)
construirAireDataFrame()   