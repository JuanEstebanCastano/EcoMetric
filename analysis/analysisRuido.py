""" import pandas as pd
from data.generators.generadorAire import generarDatosRuidoAmbiental
from helpers.crearTablaHTML import crearTabla

def construirRuidoDataFrame():
    datosRuido=generarDatosRuidoAmbiental()
    
    #generamos el dataframe
    ruidoDataFrame = pd.DataFrame(datosRuido,columns = ["comuna","decibeliosDiurnos","decibeliosNocturnos",'fecha'])
   #generamos el recurso HTML
   
    crearTabla(ruidoDataFrame,"datosRuido")
    print(ruidoDataFrame)
    #Limpiando el dataFrame
    #reemplazando valores
    ruidoDataFrame.replace('sin',pd.NA,inplace=True)
    #eliminar registros que no cumplen el criterio
    ruidoDataFrame.dropna(inplace=True)
   # Filtrar Datos
    # Escala 1: Ruido bajo (decibeliosDiurnos < 50 y decibeliosNocturnos < 45)
    filtroRuidoBajo = ruidoDataFrame.query("(decibeliosDiurnos < 50) and (decibeliosNocturnos < 45)").value_counts()

    # Escala 2: Ruido medio (50 <= decibeliosDiurnos < 70 o 45 <= decibeliosNocturnos < 60)
    filtroRuidoMedio = ruidoDataFrame.query("((50 <= decibeliosDiurnos < 70) or (45 <= decibeliosNocturnos < 60))").value_counts()

    # Escala 3: Ruido alto (decibeliosDiurnos >= 70 o decibeliosNocturnos >= 60)
    filtroRuidoAlto = ruidoDataFrame.query("(decibeliosDiurnos >= 70) or (decibeliosNocturnos >= 60)").value_counts()

    # Imprimir resultados
    print("Filtro Ruido Bajo:")
    print(filtroRuidoBajo)
    print("\n")
    
    print("Filtro Ruido Medio:")
    print(filtroRuidoMedio)
    print("\n")
    
    print("Filtro Ruido Alto:")
    print(filtroRuidoAlto)
    
construirRuidoDataFrame()    """ 

import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorAire import generarDatosRuidoAmbiental  # Asumiendo el generador correcto
from helpers.crearTablaHTML import crearTabla

def construirRuidoDataFrame():
    datosRuido = generarDatosRuidoAmbiental()
    
    # Generamos el dataframe
    ruidoDataFrame = pd.DataFrame(datosRuido, columns=["comuna", "decibeliosDiurnos", "decibeliosNocturnos", 'fecha'])
    
    # Generamos el recurso HTML
    crearTabla(ruidoDataFrame, "datosRuido")
    
    # Limpiando el dataframe
    ruidoDataFrame.replace('sin', pd.NA, inplace=True)
    ruidoDataFrame.dropna(inplace=True)
    
    # Filtrar Datos
    # Escala 1: Ruido bajo (decibeliosDiurnos < 50 y decibeliosNocturnos < 45)
    filtroRuidoBajo = ruidoDataFrame.query("(decibeliosDiurnos < 50) & (decibeliosNocturnos < 45)")
    
    # Escala 2: Ruido medio (50 <= decibeliosDiurnos < 70 o 45 <= decibeliosNocturnos < 60)
    filtroRuidoMedio = ruidoDataFrame.query("((50 <= decibeliosDiurnos < 70) | (45 <= decibeliosNocturnos < 60))")
    
    # Escala 3: Ruido alto (decibeliosDiurnos >= 70 o decibeliosNocturnos >= 60)
    filtroRuidoAlto = ruidoDataFrame.query("(decibeliosDiurnos >= 70) | (decibeliosNocturnos >= 60)")
    
    # Graficar los datos
    plt.figure(figsize=(10, 6))
    ruidoDataFrame.groupby('comuna')['decibeliosDiurnos'].mean().plot(kind='bar', color='blue')
    plt.title("Niveles de Ruido Ambiental por Comuna")
    plt.xlabel("Comuna")
    plt.ylabel("Decibelios Diurnos (Promedio)")
    plt.grid(True)
    plt.savefig("./assets/img/ruidoAmbiental.png", format='png', dpi=300)
    
  

construirRuidoDataFrame()
