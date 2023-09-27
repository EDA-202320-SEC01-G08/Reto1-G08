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
    control = model.new_data_structs_array()
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

def loadResultsOrd(control, filename, opcion_array, sort_option):
    
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for i in input_file:
        model.addResultsOrd(control, i, opcion_array)
        
    model.sort(control["results"], sort_option)
    return model.resultSize(control), control["results"]

def loadShootoutsOrd(control, filename, opcion_array, sort_option):
    
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for i in input_file:
        model.addShootoutsOrd(control, i, opcion_array)
        
    model.sort(control["shootouts"], sort_option)
    return model.shootoutSize(control), control["shootouts"]

def loadGoalscorersOrd(control, filename, opcion_array, sort_option):
    
    input_file = csv.DictReader(open(filename, encoding="utf-8"))
    for i in input_file:
        model.addGoalscorersOrd(control, i, opcion_array)
        
    model.sort(control["goalscorers"], sort_option)
    return model.goalscoSize(control), control["goalscorers"]


def get_time():
    return float(time.perf_counter()*1000)

def delt_time(start, end):
    elaps = float(end - start)
    return elaps


def sort_data(size, lista, sort_option):
    start = getTime()
    sorted_result = model.sortThings(lista, sort_option, size)
    end = getTime()
    time = deltaTime(start, end)
    return time, sorted_result

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

def sort_data(size, lista, sort_option):
    start = getTime()
    sorted_result = model.sortThings(lista, sort_option, size)
    end = getTime()
    time = deltaTime(start, end)
    return time, sorted_result

def getDatabyTournament(control, nombre, fecha_inicio, fecha_fin):
    resultado = model.getDatabyTournament(control["results"], control["shootouts"], nombre, fecha_inicio, fecha_fin)
    return resultado

def getDatabyPlayer(control, nombre, fecha_inicio, fecha_fin):
    resultado = model.getDatabyPlayer(control["goalscorers"], control["results"], nombre, fecha_inicio, fecha_fin)
    return resultado

def getGoalsbyPlayer(control, nombre, size):
    goles = model.getGoalsbyPlayer(control["goalscorers"], nombre, size)
    return goles

def getMatchbyTeam(control, team, condition):
    data_structs = control["results"]
    results = model.getMatchbyTeam(data_structs, team, condition)
    return len(results), results

def getResultsbyTeam(control, team, fecha_inicio, fecha_fin):
    
    data_structs_results = control["results"]
    data_structs_goalscorers = control["goalscorers"]
    
    results = model.getResultsbyTeam(data_structs_results, data_structs_goalscorers, team, fecha_inicio, fecha_fin)
    
    counting_home=0
    counting_away=0
    
    for data in results:
        if data["home_team"] == team:
            counting_home += 1
        else:
            counting_away += 1
    return len(results), counting_home, counting_away, results

def getBestTeams(control, fecha_inicio, fecha_fin):
    
    data_structs_results = control["results"]
    data_structs_goalscorers = control["goalscorers"]
    
    scorers = model.getBestTeams(data_structs_results, data_structs_goalscorers, fecha_inicio, fecha_fin)
    
    return scorers

def getBestPlayers(control):
    model.getBestPlayers(control, "1900-01-01", "2023-08-01", 17)

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
    team1 = 'Argentina'
    team2 = 'Chile'
    start_d ='1952-03-25'
    end_d = '2021-11-23'
    start_time = get_time()
    n_years1, n_matches1, home_matches1, away_matches1, oldest_date1, newest_match1, elements1, n_years2, n_matches2, home_matches2, away_matches2, oldest_date2, newest_match2, elements2, n_joint_matches, joint_wins1, joint_losses1, joint_wins2, joint_losses2, joint_draws, newest_joint_match, scores = model.req_8(control['model'],team1, team2, start_d, end_d)
    end_time = get_time()
    delta = deltaTime(start_time, end_time)
    print('Tiempo que tomó ejecutar el requerimiento:',delta)
    return n_years1, n_matches1, home_matches1, away_matches1, oldest_date1, newest_match1, elements1, n_years2, n_matches2, home_matches2, away_matches2, oldest_date2, newest_match2, elements2, n_joint_matches, joint_wins1, joint_losses1, joint_wins2, joint_losses2, joint_draws, newest_joint_match, scores, team1, team2


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


