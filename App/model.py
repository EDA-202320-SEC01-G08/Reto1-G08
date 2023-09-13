﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {"results": None, 
               "goalscorers": None, 
               "shootouts": None}
    
    catalog["results"] = lt.newList("ARRAY_LIST")
    catalog["goalscorers"] = lt.newList("ARRAY_LIST")
    catalog["shootouts"] = lt.newList("ARRAY_LIST")
    
    return catalog

# Funciones para agregar informacion al modelo

def addResult(data_structs, data):
    lt.addLast(data_structs["results"], data)
    return data_structs

def addGoalsco(data_structs, data):
    lt.addLast(data_structs["goalscorers"], data)
    return data_structs

def addShootouts(data_structs, data):
    lt.addLast(data_structs["shootouts"], data)
    return data_structs

def addResultsOrd(data_structs, data, opcion_array):
    if opcion_array == "1":
        lt.addLast(data_structs["results"], data)
    elif opcion_array == "2":
        data_structs["results"] = lt.newList("LINKED_LIST")
        lt.addLast(data_structs["results"], data)
    return data_structs

def addGoalscorersOrd(data_structs, data, opcion_array):
    if opcion_array == "1":
        lt.addLast(data_structs["goalscorers"], data)
    elif opcion_array == "2":
        data_structs["goalscorers"] = lt.newList("LINKED_LIST")
        lt.addLast(data_structs["goalscorers"], data)
    return data_structs

def addShootoutsOrd(data_structs, data, opcion_array):
    if opcion_array== "1":
        lt.addLast(data_structs["shootouts"], data)
    elif opcion_array == "2":
        data_structs["shootouts"] = lt.newList("LINKED_LIST")
        lt.addLast(data_structs["shootouts"], data)
    return data_structs

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def getResults(catalog, result):
    resul = lt.isPresent(catalog["results"], result)
    if resul > 0:
        res = lt.getElement(catalog["results"], resul)
        return res
    return None

def getGoalsco(catalog, goalsc):
    goals = lt.isPresent(catalog["goalscorers"], goalsc)
    if goals > 0:
        gsco = lt.getElement(catalog["goalscorers"], goals)
        return gsco
    return None

def getShootouts(catalog, shootout):
    shoot = lt.isPresent(catalog["shootouts"], shootout)
    if shoot > 0:
        shoo = lt.getElement(catalog["shootouts"], shoot)
        return shoo
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass

def resultSize(catalog):
    return lt.size(catalog["results"])

def goalscoSize(catalog):
    return lt.size(catalog["goalscorers"])

def shootoutSize(catalog):
    return lt.size(catalog["shootouts"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

def compareresults(result1, result2):
    return (float(result1["date"]) < float(result2["date"]))

def comparegoalscorers(goalscorer1, goalscorer2):
    return (float(goalscorer1["date"]) < float(goalscorer2["date"]))

def compareshootouts(shootout1, shootout2):
    return (float(shootout1["date"]) < float(shootout2["date"]))

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    return (str(data_1["date"]) < str(data_2["date"]))

def sort(data_structs, sort_option="shell"):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    if sort_option == "shell":
        sa.sort(data_structs, sort_criteria)
    elif sort_option == "insertion":
        sa.sort(data_structs, sort_criteria)
    elif sort_option == "selection":
        sa.sort(data_structs, sort_criteria)
        
def sortResults(control, size):
    sub_list = lt.subList(control["results"], 1, size)
    sorted_list = sa.sort(sub_list, compareresults)
    return sorted_list

def sortGoalscorers(control, size):
    sub_list = lt.subList(control["goalscorers"], 1, size)
    sorted_list = sa.sort(sub_list, comparegoalscorers)
    return sorted_list

def sortShootouts(control, size):
    sub_list = lt.subList(control["shootouts"], 1, size)
    sorted_list = sa.sort(sub_list, compareshootouts)
    return sorted_list
