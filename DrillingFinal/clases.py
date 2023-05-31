import csv

class Vehiculo:
    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv", "a", newline="") as archivo:
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerow([type(self).__name__, str(vars(self))])
            print("Datos guardados correctamente")
        except Exception as e:
            print("Error al guardar los datos:", e)

    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv", "r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de vehiculos {type(self).__name__}")

                for item in vehiculos:
                    vehiculo_tipo = type(self).__name__
                    if vehiculo_tipo in item[0]:
                        print(item[1])
                        print("")

        except Exception as e:
            print("Error al leer los datos:", e)


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Número de ruedas: {self.n_ruedas}, Velocidad: {self.velocidad} Km/h, Cilindrada: {self.cilindrada} cc"

class AutomovilParticular(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, num_puesto):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.num_puesto = num_puesto

    def __str__(self):
        return super().__str__() + f", Número de puesto: {self.num_puesto}"

class AutomovilCarga(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return super().__str__() + f", Peso de carga: {self.peso_carga} kg"
    

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo_bicicleta = tipo_bicicleta



class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, n_ruedas, tipo_bicicleta, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, n_ruedas, tipo_bicicleta)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor