
import random

def generarDatosCalidadAire():
    listaDatos = []
    for i in range(1000):
        nombre = random.choice(["Ana Perez", "Jose Jimenez", "Marcolo Agachateconocelo", "Karen Andrea", "Jesus Perez"])
        comuna = random.randint(1, 14)
        ica = random.randint(10, 50)
        fecha = random.choice(["2024-02-12", "2024-02-13", "2024-02-14"])
        correo = random.choice(["correo@correo.com", "correo1@correo.com", "correo2@correo.com", "correo4@correo.com", "correo5@correo.com"])
        encuesta = [nombre, comuna, ica, fecha, correo]
        listaDatos.append(encuesta)
    return listaDatos

def generarDatosRuidoAmbiental():
    listaDatos = []
    for i in range(1000):
        comuna = random.randint(1, 14)
        decibeliosDiurnos = random.randint(1, 80)
        decibeliosNocturnos = random.randint(1, 80)
        fecha = random.choice(["2024-02-12", "2024-02-13", "2024-02-14"])
        encuesta = [comuna, decibeliosDiurnos, decibeliosNocturnos, fecha]
        listaDatos.append(encuesta)
    return listaDatos

def generarDatosSiembraArboles():
    listaDatos = []
    for i in range(1000):
        corregimiento = random.choice(["San Sebastián de Palmitas", "San Cristóbal", "Altavista", "San Antonio de Prado"])
        hectarea = random.randint(1, 20)
        especieArbol = random.choice(["chochos", "cedros", "guayabillos", "acacias amarillas y rojas"])
        nombre = random.choice(["Ana Perez", "Jose Jimenez", "Marcolo Agachateconocelo", "Karen Andrea", "Jesus Perez"])
        fecha = random.choice(["2024-02-12", "2024-02-13", "2024-02-14"])
        correo = random.choice(["correo@correo.com", "correo1@correo.com", "correo2@correo.com", "correo4@correo.com", "correo5@correo.com"])
        encuesta = [corregimiento, hectarea, especieArbol, nombre, fecha, correo]
        listaDatos.append(encuesta)
    return listaDatos

def generarDatosGestionResiduos():
    listaDatos = []
    for i in range(1000):
        comuna = random.randint(1, 14)
        nombre = random.choice(["Ana Perez", "Jose Jimenez", "Marcolo Agachateconocelo", "Karen Andrea", "Jesus Perez"])
        consumoAgua = random.choice(["chochos", "cedros", "guayabillos", "acacias amarillas y rojas"])
        consumoAcueducto = random.choice(["San Sebastián de Palmitas", "San Cristóbal", "Altavista", "San Antonio de Prado"])
        fecha = random.choice(["2024-02-12", "2024-02-13", "2024-02-14"])
        correo = random.choice(["correo@correo.com", "correo1@correo.com", "correo2@correo.com", "correo4@correo.com", "correo5@correo.com"])
        encuesta = [comuna, nombre, consumoAgua, consumoAcueducto, fecha, correo]
        listaDatos.append(encuesta)
    return listaDatos

def generarDatosConsumoAgua():
    listaDatos = []
    for i in range(1000):
        comuna = random.randint(1, 14)
        nombre = random.choice(["Ana Perez", "Jose Jimenez", "Marcolo Agachateconocelo", "Karen Andrea", "Jesus Perez"])
        tipoResiduo = random.choice(["orgánico", "reciclable", "no reciclable", "peligroso"])
        cantidad = random.randint(1, 100)
        fecha = random.choice(["2024-02-12", "2024-02-13", "2024-02-14"])
        correo = random.choice(["correo@correo.com", "correo1@correo.com", "correo2@correo.com", "correo4@correo.com", "correo5@correo.com"])
        encuesta = [comuna, nombre, tipoResiduo, cantidad, fecha, correo]
        listaDatos.append(encuesta)
    return listaDatos

def main():
    while True:
        opcion = int(input("Ingrese la opción: 1. Calidad del aire 2. Ruido ambiental 3. Siembra de árboles 4. Gestión de residuos 5. Consumo de agua por comuna 6. Salir: "))
        if opcion == 1:
            datos = generarDatosCalidadAire()
        elif opcion == 2:
            datos = generarDatosRuidoAmbiental()
        elif opcion == 3:
            datos = generarDatosSiembraArboles()
        elif opcion == 4:
            datos = generarDatosGestionResiduos()
        elif opcion == 5:
            datos = generarDatosConsumoAgua()
        elif opcion == 6:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
            continue

        for dato in datos[:20]:  # Mostrar solo los primeros 5 datos como ejemplo
            print(dato)

if __name__ == "__main__":
    main()
