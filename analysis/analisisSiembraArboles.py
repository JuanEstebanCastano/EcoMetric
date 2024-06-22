""" import pandas as pd
from data.generators.generadorAire import generarDatosSiembraArboles
from helpers.crearTablaHTML import crearTabla

def construirSiembraArbolesDataFrame():
    datosSiembraArboles=generarDatosSiembraArboles()
    
    #generamos el dataframe
    SiembraArbolesDataFrame = pd.DataFrame(datosSiembraArboles,columns = ["corregimiento","hectarea","especieArbol",'nombre','fecha','correo'])
   #generamos el recurso HTML
   
    crearTabla(SiembraArbolesDataFrame,"datosSiembraArboles")
    print(SiembraArbolesDataFrame)
    #Limpiando el dataFrame
    #reemplazando valores
    SiembraArbolesDataFrame.replace('sin',pd.NA,inplace=True)
    #eliminar registros que no cumplen el criterio
    SiembraArbolesDataFrame.dropna(inplace=True)
   # Filtrar Datos
    # Escala 1: Pocas hectáreas
    filtropocasHectareas = SiembraArbolesDataFrame.query("hectarea < 5").value_counts()

    # Escala 2: Hectáreas aceptables
    filtroHectareasAceptables = SiembraArbolesDataFrame.query("5 <= hectarea < 10").value_counts()

    # Escala 3: Muchas hectáreas
    filtroMuchasHectareas = SiembraArbolesDataFrame.query("hectarea >= 10").value_counts()

    # Imprimir resultados
    print("Filtro pocas hectáreas:")
    print(filtropocasHectareas)
    print("\n")
    
    print("Filtro hectáreas aceptables:")
    print(filtroHectareasAceptables)
    print("\n")
    
    print("Filtro muchas hectáreas:")
    print(filtroMuchasHectareas)
    
construirSiembraArbolesDataFrame() """

import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorAire import generarDatosSiembraArboles  # Asumiendo el generador correcto
from helpers.crearTablaHTML import crearTabla

def construirSiembraArbolesDataFrame():
    datosSiembraArboles = generarDatosSiembraArboles()
    
    # Generamos el dataframe
    SiembraArbolesDataFrame = pd.DataFrame(datosSiembraArboles, columns=["corregimiento", "hectarea", "especieArbol", 'nombre', 'fecha', 'correo'])
    
    # Generamos el recurso HTML
    crearTabla(SiembraArbolesDataFrame, "datosSiembraArboles")
    
    # Limpiando el dataframe
    SiembraArbolesDataFrame.replace('sin', pd.NA, inplace=True)
    SiembraArbolesDataFrame.dropna(inplace=True)
    
    # Filtrar Datos
    # Escala 1: Pocas hectáreas
    filtroPocasHectareas = SiembraArbolesDataFrame.query("hectarea < 5")
    
    # Escala 2: Hectáreas aceptables
    filtroHectareasAceptables = SiembraArbolesDataFrame.query("5 <= hectarea < 10")
    
    # Escala 3: Muchas hectáreas
    filtroMuchasHectareas = SiembraArbolesDataFrame.query("hectarea >= 10")
    
    # Graficar los datos
    plt.figure(figsize=(10, 6))
    SiembraArbolesDataFrame.groupby('corregimiento')['hectarea'].sum().plot(kind='bar', color='green')
    plt.title("Siembra de Árboles por Corregimiento")
    plt.xlabel("Corregimiento")
    plt.ylabel("Hectáreas")
    plt.grid(True)
    plt.savefig("./assets/img/siembraArboles.png", format='png', dpi=300)
    
   

construirSiembraArbolesDataFrame()
