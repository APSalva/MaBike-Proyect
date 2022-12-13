
import json
import requests
# Importamos todas nuestras funciones que hemos hecho
from FindBike import FindBike
from InsertOneBike import InsertOneBike
from UpdateOneBike import UpdateOneBike
from DeleteOneBike import DeleteOneBike
# Creamos una interfaz para el usuario
def interfazCRUD():
    # Hacemos una interfaz gráfica para que el usuario puede decir que opción elegir
    print("¿Que es lo que quieres hacer?")
    print("1.   Ver todos los documentos")
    print("2.   Insertar un documento")
    print("3.   Modificar un documento")
    print("4.   Eliminar un documento")
    print("5.   Salir")
    action = input("Elige una número del 1 al 5: ")
    if action == "1":
        FindBike()
    elif action == "2":
        InsertOneBike()
    elif action == "3":
        UpdateOneBike()
        print("La bici ha sido actualizada correctamente")
    elif action == "4":
        DeleteOneBike()
        print("La bici ha sido eliminada correctamente")
    elif action == "5":
        print("Adios!")
    else:
        print("No entendi lo que me dijiste")
        interfazCRUD
interfazCRUD()