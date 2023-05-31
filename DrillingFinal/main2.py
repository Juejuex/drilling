from clases import *
def ingresar_automoviles(n_automovil):
    automoviles = []

    n = 0
    while n != n_automovil:
        n += 1
        print(f"Datos del automovil {n}")
        tipo_automovil = input("Ingrese el tipo de automovil (P - Particular, C - Carga, N - Normal): ")
        marca = input("Inserte la marca del automovil: ")
        modelo = input("Inserte el modelo: ")
        n_ruedas = input("Inserte el numero de ruedas: ")
        velocidad = input("Inserte la velocidad: ")
        cilindraje = input("Inserte el cilindraje en cc: ")
        if tipo_automovil.upper() == "P":
            num_puesto = input("Inserte el número de puesto: ")
            vehiculo = AutomovilParticular(marca, modelo, n_ruedas, velocidad, cilindraje, num_puesto)
        elif tipo_automovil.upper() == "C":
            peso_carga = input("Inserte el peso de la carga en kg: ")
            vehiculo = AutomovilCarga(marca, modelo, n_ruedas, velocidad, cilindraje, peso_carga)
        elif tipo_automovil.upper() == "N":
            vehiculo = Automovil(marca, modelo, n_ruedas, velocidad, cilindraje)
        else:
            print("Tipo de automovil inválido. Se omitirá este vehiculo.")
            continue

        automoviles.append(vehiculo)  

    for i, automovil in enumerate(automoviles):
        print(f"Datos del automóvil {i + 1}: {automovil}")


n_automovil = int(input("Cuantos vehiculos desea ingresar: "))

ingresar_automoviles(n_automovil)