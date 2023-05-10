# lista completa de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# separar los nombres en categorías
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros=[]

for item in nombres:
    if item not in magos and item not in cientificos:
        otros.append(item)

        

# función para hacer grandiosos a los magos
def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = "El gran " + lista_magos[i]

# función para imprimir nombres
def imprimir_nombres(lista_nombres):
    for nombre in lista_nombres:
        print(nombre)

# imprimir la lista completa de nombres
print("Lista completa de nombres:")
imprimir_nombres(nombres)
print("")

# hacer grandiosos a los magos
hacer_grandioso(magos)

# imprimir los nombres de los magos grandiosos
print("Nombres de los magos grandiosos:")
imprimir_nombres(magos)
print("")

# imprimir los nombres de los científicos
print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print("")

# imprimir los nombres de los restantes
print("Nombres de los restantes:")
imprimir_nombres(otros)



