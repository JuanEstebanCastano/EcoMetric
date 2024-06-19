""" import pandas as pd
from data.generators.generadorAire import generarDatosGestionResiduos
from helpers.crearTablaHTML import crearTabla



def construirGestionResiduosDataFrame():
    # Generación de los datos de gestión de residuos
    datosGestionResiduos = generarDatosGestionResiduos()
    
    # Generamos el DataFrame
    gestionResiduosDataFrame = pd.DataFrame(datosGestionResiduos, columns=["comuna", "nombre", "tipoResiduo", "cantidad", "fecha", "correo"])
    crearTabla(gestionResiduosDataFrame, "datosGestionResiduos")
    
    # Imprimimos el DataFrame original
    print(construirGestionResiduosDataFrame)
    # Limpiando el DataFrame
    gestionResiduosDataFrame.replace('sin', pd.NA, inplace=True)
    gestionResiduosDataFrame.dropna(inplace=True)

    # Filtrar Datos
    # Escala 1: Baja cantidad de residuos (cantidad < 30)
    filtroBajaCantidad = gestionResiduosDataFrame.query("cantidad < 30").value_counts()

    # Escala 2: Cantidad moderada de residuos (30 <= cantidad < 70)
    filtroCantidadModerada = gestionResiduosDataFrame.query("30 <= cantidad < 70").value_counts()

    # Escala 3: Alta cantidad de residuos (cantidad >= 70)
    filtroAltaCantidad = gestionResiduosDataFrame.query("cantidad >= 70").value_counts()

    # Imprimir resultados
    print("Filtro Baja Cantidad de Residuos:")
    print(filtroBajaCantidad)
    print("\n")

    print("Filtro Cantidad Moderada de Residuos:")
    print(filtroCantidadModerada)
    print("\n")

    print("Filtro Alta Cantidad de Residuos:")
    print(filtroAltaCantidad)

# Llamamos a la función para ejecutar el código
construirGestionResiduosDataFrame() """

import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorAire import generarDatosGestionResiduos  # Asumiendo el generador correcto
from helpers.crearTablaHTML import crearTabla

def construirGestionResiduosDataFrame():
    # Generación de los datos de gestión de residuos
    datosGestionResiduos = generarDatosGestionResiduos()
    
    # Generamos el DataFrame
    gestionResiduosDataFrame = pd.DataFrame(datosGestionResiduos, columns=["comuna", "nombre", "tipoResiduo", "cantidad", "fecha", "correo"])
    crearTabla(gestionResiduosDataFrame, "datosGestionResiduos")
    
    # Imprimimos el DataFrame original
    print(gestionResiduosDataFrame)
    
    # Limpiando el DataFrame
    gestionResiduosDataFrame.replace('sin', pd.NA, inplace=True)
    gestionResiduosDataFrame.dropna(inplace=True)

    # Filtrar Datos
    # Escala 1: Baja cantidad de residuos (cantidad < 30)
    filtroBajaCantidad = gestionResiduosDataFrame.query("cantidad < 30")
    
    # Escala 2: Cantidad moderada de residuos (30 <= cantidad < 70)
    filtroCantidadModerada = gestionResiduosDataFrame.query("30 <= cantidad < 70")
    
    # Escala 3: Alta cantidad de residuos (cantidad >= 70)
    filtroAltaCantidad = gestionResiduosDataFrame.query("cantidad >= 70")
    
    # Graficar los datos
    plt.figure(figsize=(10, 6))
    gestionResiduosDataFrame.groupby('comuna')['cantidad'].sum().plot(kind='bar', color='orange')
    plt.title("Cantidad de Residuos por Comuna")
    plt.xlabel("Comuna")
    plt.ylabel("Cantidad de Residuos")
    plt.grid(True)
    plt.savefig("./assets/img/gestionResiduos.png", format='png', dpi=300)
    
   

construirGestionResiduosDataFrame()
