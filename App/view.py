﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar Datos")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def loadResults(control):
    resultados = controller.loadResults(control, "Data/results-utf8-small.csv")
    return resultados

def loadGoalsco(control):
    resultados = controller.loadGoalsco(control, "Data/goalscorers-utf8-small.csv")
    return resultados

def loadShootouts(control):
    resultados = controller.loadShootouts(control, "Data/shootouts-utf8-small.csv")
    return resultados


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    printable = controller.get_data(control, id)
    print(printable)

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    printable = controller.req_1(control)
    print(printable)


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    printable = controller.req_2(control)
    print(printable)


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    printable = controller.req_3(control)
    print(printable)


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    printable = controller.req_4(control)
    print(printable)


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    printable = controller.req_5(control)
    print(printable)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    printable = controller.req_6(control)
    print(printable)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    printable = controller.req_7(control)
    print(printable)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    printable = controller.req_8(control)
    print(printable)


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando informacion de los archivos ....\n")
            resultados, results = loadResults(control)
            print("Se cargaron" + " " + str(resultados) + " " + "resultados de partidos...\n")
            print("Primeros tres resultados de los partidos: ")
            print(results["elements"][0:2])
            print("\n")
            print("Ultimos tres resultados de partidos: ")
            print(results["elements"][-3:], "\n")
            
            print("Cargando informacion de los archivos ....\n")
            resultados, goalscorers = loadGoalsco(control)
            print("Se cargaron" + " " + str(resultados) + " " + "jugadores que marcaron gol o anotaciones...\n")
            print("Primeros tres resultados de goleadores: ")
            print(goalscorers["elements"][0:2])
            print("\n")
            print("Ultimos tres resultados de goleadores: ")
            print(goalscorers["elements"][-3:], "\n")
            
            print("Cargando informacion de los archivos ....\n")
            resultados, shootouts = loadShootouts(control)
            print("Se cargaron" + " " + str(resultados) + " " + "definiciones de partidos desde el punto penal...\n")
            print("Primeros tres resultados por penales: ")
            print(shootouts["elements"][0:2])
            print("\n")
            print("Ultimos tres resultados por penales: ")
            print(shootouts["elements"][-3:], "\n")
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
