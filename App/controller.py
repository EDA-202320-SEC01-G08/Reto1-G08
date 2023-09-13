"""
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
 """

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = model.new_data_structs()
    return control

def new_controller_array():
    control = model.new_data_structs()
    return control

# Funciones para la carga de datos

def loadResults(control, filename):
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for result in input_file:
        model.addResult(control, result)
    model.sort(control["results"])
    return model.resultSize(control), control["results"]

def loadGoalsco(control, filename):
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for goalscorer in input_file:
        model.addGoalsco(control, goalscorer)
    model.sort(control["goalscorers"])
    return model.goalscoSize(control), control["goalscorers"]

def loadShootouts(control, filename):
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for shootout in input_file:
        model.addShootouts(control, shootout)
    model.sort(control["shootouts"])
    return model.shootoutSize(control), control["shootouts"]

# Funciones de ordenamiento

def loadResultsOrd(control, filename, opcion_array):
    
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for i in input_file:
        model.addResultsOrd(control, i, opcion_array)
        
    model.sort(control["results"])
    return model.resultSize(control), control["results"]

def loadShootoutsOrd(control, filename, opcion_array):
    
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for i in input_file:
        model.addShootoutsOrd(control, i, opcion_array)
        
    model.sort(control["shootouts"])
    return model.shootoutSize(control), control["shootouts"]

def loadGoalscorersOrd(control, filename, opcion_array):
    
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for i in input_file:
        model.addGoalscorersOrd(control, i, opcion_array)
        
    model.sort(control["goalscorers"])
    return model.goalscoSize(control), control["goalscorers"]

def sortResults(control, size):
    start_time = getTime()
    sorted_list = model.sortResults(control["model"], size)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return delta_time, sorted_list

def sortGoalscorers(control, size):
    start_time = getTime()
    sorted_list = model.sortGoalscorers(control["model"], size)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return delta_time, sorted_list

def sortShootouts(control, size):
    start_time = getTime()
    sorted_list = model.sortShootouts(control["model"], size)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return delta_time, sorted_list

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def getResults(control, result):
    resul = model.getResults(control["model"], result)
    return resul

def getGoalsco(control, gsco):
    goalsc = model.getGoalsco(control["model"], gsco)
    return goalsc

def getShootouts(control, shootout):
    shoot = model.getShootouts(control["model"], shootout)
    return shoot


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
