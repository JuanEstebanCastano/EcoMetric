""" import pandas as pd
from data.generators.generadorAire import generarDatosConsumoAgua
from helpers.crearTablaHTML import crearTabla

def construirConsumoAguaDataFrame():
    datosConsumoAgua = generarDatosConsumoAgua()
    
    # Generamos el DataFrame
    consumoAguaDataFrame = pd.DataFrame(datosConsumoAgua, columns=["comuna", "nombre", "origenAgua", "fecha", "correo", "consumoAgua", "costoConsumo"])
   
    # Generamos el recurso HTML
    crearTabla(consumoAguaDataFrame, "datosConsumoAgua")
    print(consumoAguaDataFrame)
    
    # Limpiando el DataFrame
    consumoAguaDataFrame.replace('sin', pd.NA, inplace=True)
    consumoAguaDataFrame.dropna(inplace=True)

    # Filtrar Datos
    # Escala 1: Bajo consumo de agua (consumoAgua < 30)
    filtroBajoConsumo = consumoAguaDataFrame.query("consumoAgua < 30").value_counts()

    # Escala 2: Consumo moderado de agua (30 <= consumoAgua < 70)
    filtroConsumoModerado = consumoAguaDataFrame.query("30 <= consumoAgua < 70").value_counts()

    # Escala 3: Alto consumo de agua (consumoAgua >= 70)
    filtroAltoConsumo = consumoAguaDataFrame.query("consumoAgua >= 70").value_counts()

    # Imprimir resultados
    print("Filtro Bajo Consumo de Agua:")
    print(filtroBajoConsumo)
    print("\n")

    print("Filtro Consumo Moderado de Agua:")
    print(filtroConsumoModerado)
    print("\n")

    print("Filtro Alto Consumo de Agua:")
    print(filtroAltoConsumo)
    
construirConsumoAguaDataFrame() """

import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorAire import generarDatosConsumoAgua  # Asumiendo el generador correcto
from helpers.crearTablaHTML import crearTabla

def construirConsumoAguaDataFrame():
    datosConsumoAgua = generarDatosConsumoAgua()
    
    # Generamos el DataFrame
    consumoAguaDataFrame = pd.DataFrame(datosConsumoAgua, columns=["comuna", "nombre", "origenAgua", "fecha", "correo", "consumoAgua", "costoConsumo"])
    
    # Generamos el recurso HTML
    crearTabla(consumoAguaDataFrame, "datosConsumoAgua")
    
    # Imprimimos el DataFrame original
    print(consumoAguaDataFrame)
    
    # Limpiando el DataFrame
    consumoAguaDataFrame.replace('sin', pd.NA, inplace=True)
    consumoAguaDataFrame.dropna(inplace=True)

    # Filtrar Datos
    # Escala 1: Bajo consumo de agua (consumoAgua < 30)
    filtroBajoConsumo = consumoAguaDataFrame.query("consumoAgua < 30")
    
    # Escala 2: Consumo moderado de agua (30 <= consumoAgua < 70)
    filtroConsumoModerado = consumoAguaDataFrame.query("30 <= consumoAgua < 70")
    
    # Escala 3: Alto consumo de agua (consumoAgua >= 70)
    filtroAltoConsumo = consumoAguaDataFrame.query("consumoAgua >= 70")
    
    # Graficar los datos
    plt.figure(figsize=(10, 6))
    consumoAguaDataFrame.groupby('comuna')['consumoAgua'].mean().plot(kind='bar', color='blue')
    plt.title("Consumo de Agua por Comuna")
    plt.xlabel("Comuna")
    plt.ylabel("Consumo de Agua (Promedio)")
    plt.grid(True)
    plt.savefig("./assets/img/consumoAgua.png", format='png', dpi=300)
    
  

construirConsumoAguaDataFrame()

