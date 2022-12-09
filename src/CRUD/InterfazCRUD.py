# Importamos la libreria JSON
import json
import requests
import os

# Importamos todas nuestras funciones que hemos hecho
import FindBike
import InsertOneBike
import UpdateOneBike
import DeleteOneBike

# Creamos una interfaz para el usuario
def InterfazCRUD():
    # Hacemos una interfaz gráfica para que el usuario puede decir que opción elegir
    print("¿Que es lo que quieres hacer?")
    print("1.   Ver todos los documentos")
    print("2.   Insertar un documento")
    print("3.   Modificar un documento")
    print("4.   Eliminar un documento")
    print("5.   Salir")

    action = int(input("Elige una número del 1 al 5: "))

    if action == 1: FindBike()
    elif action == 2: InsertOneBike()
    elif action == 3: UpdateOneBike()
    elif action == 4: DeleteOneBike()
    elif action == 5: print("Adios!")
InterfazCRUD()