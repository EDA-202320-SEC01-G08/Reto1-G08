"""
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

from tabulate import tabulate
import threading
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

def list_python(list) -> None:
    python_list = []
    for i in list["elements"]:
        python_list.append(i)
        
    return python_list

def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control

def new_controller_array():
    
    control = controller.new_controller_array()
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
    print("10- Cargar Datos segun tipo de representacion de lista")
    print("0- Salir")


def loadResults(control):
    resultados = controller.loadResults(control, "Data/results-utf8-large.csv")
    return resultados

def loadGoalsco(control):
    resultados = controller.loadGoalsco(control, "Data/goalscorers-utf8-large.csv")
    return resultados

def loadShootouts(control):
    resultados = controller.loadShootouts(control, "Data/shootouts-utf8-large.csv")
    return resultados



def loadResultsOrd(control, archivo, opcion_array, sort_option):
    if archivo == "1":
        resultados = controller.loadResultsOrd(control, "Data/results-utf8-20pct.csv", opcion_array, sort_option)
    elif archivo == "2":
        resultados = controller.loadResultsOrd(control, "Data/results-utf8-50pct.csv", opcion_array, sort_option)
    elif archivo == "3":
        resultados = controller.loadResultsOrd(control, "Data/results-utf8-large.csv", opcion_array, sort_option)
    return resultados   

def loadShootoutsOrd(control, archivo, opcion_array, sort_option):
    if archivo == "1":
        resultados = controller.loadShootoutsOrd(control, "Data/shootouts-utf8-20pct.csv", opcion_array, sort_option)
    elif archivo == "2":
        resultados = controller.loadShootoutsOrd(control, "Data/shootouts-utf8-50pct.csv", opcion_array, sort_option)
    elif archivo == "3":
        resultados = controller.loadShootoutsOrd(control, "Data/shootouts-utf8-large.csv", opcion_array, sort_option)
    return resultados

def loadGoalscorersOrd(control, archivo, opcion_array, sort_option):
    if archivo == "1":
        resultados = controller.loadGoalscorersOrd(control, "Data/goalscorers-utf8-20pct.csv", opcion_array, sort_option)
    elif archivo == "2":
        resultados = controller.loadGoalscorersOrd(control, "Data/goalscorers-utf8-50pct.csv", opcion_array, sort_option)
    elif archivo == "3":
        resultados = controller.loadGoalscorersOrd(control, "Data/goalscorers-utf8-large.csv", opcion_array, sort_option)
    return resultados



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    printable = controller.get_data(control, id)
    print(printable)

#--------------------------------------------------------------------------------------------------   
#----------------------------------------Requerimiento 1-------------------------------------------

def print_req_1(control, matches, team, condition):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print("==========Req No. 1 outputs==========")
    results, resultados, tiempo = controller.getMatchbyTeam(control, team, condition)
    if matches > 6:
        print("Total matches found: " + str(resultados) )
        print("Selecting " + str(matches) + " matches...\n")
        print("Primeros tres resultados:")
        print(tabulate(results[:matches][:3], headers="keys", tablefmt="grid"))
        print("\n")
        print("Ultimos tres resultados: ")
        print(tabulate(results[:matches][-3:], headers="keys", tablefmt="grid"))
    else:
        print("Se han cargado " + str(resultados) + " resultados...\n")
        print(tabulate(results[:matches], headers="keys", tablefmt="grid"))

#--------------------------------------------------------------------------------------------------
#----------------------------------------Requerimiento 2-------------------------------------------

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print("==========Req No. 2 outputs==========")
    printable, tiempo = controller.getGoalsbyPlayer(control, nombre, int(size))
    
    print(f"=============== Req 2 Inputs ===============\n\nNombre del jugador: {nombre}\nNumero de goles: {size}\n")
    print(f"=============== Req 2 Results ===============\n\nNumero de goles encontrados: {len(printable)}\n")
        
        
    if len(printable) > 6:
        print("Se han encontrado más de 6 registros...")
        ult = printable[:3]
        prim = printable[-3:]
        print(tabulate(ult+prim, headers="keys", tablefmt="grid"))
    else:
        print("Se han encontrado menos de 6 registros...")
        print(tabulate(printable, headers="keys", tablefmt="grid"))

#-------------------------------------------------------------------------------------------------        
#----------------------------------------Requerimiento 3------------------------------------------

def print_req_3(control, team, fecha_inicio, fecha_fin):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print("==========Req No. 3 outputs==========")
    results, local, visitante, resultados_total = controller.getResultsbyTeam(control, team, fecha_inicio, fecha_fin)
    
    if resultados_total > 6:
        print(str(team) + " Total games: " + str(resultados_total))
        print(str(team) + " Total home games: " + str(local))
        print(str(team) + " Total away games: " + str(visitante))
        print("Primeros tres resultados:")
        print(tabulate(results[:3], headers="keys", tablefmt="grid"))
        print("\n")
        print("Ultimos tres resultados: ")
        print(tabulate(results[-3:], headers="keys", tablefmt="grid"))
    else:
        print(str(team) + " Total games: " + str(resultados_total))
        print(str(team) + " Total home games: " + str(local))
        print(str(team) + " Total away games: " + str(visitante))
        print(tabulate(results, headers="keys", tablefmt="grid"))

#-------------------------------------------------------------------------------------------------       
#-----------------------------------------Requerimiento 4-----------------------------------------

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print("==========Req No. 4 outputs==========")
    printable, paises, ciudades, tiempo = controller.getDatabyTournament(control, nombre_torneo, fecha_inicio, fecha_fin)
    list = []
    for i in lt.iterator(printable):
        i.pop("neutral")
        list.append(i)
        
    print(f"=============== Req 4 Inputs ===============\n\nTournament: {nombre_torneo}\nFecha inicio: {fecha_inicio}\nFecha final: {fecha_fin}\n")
    print(f"=============== Req 4 Results ===============\n\n{nombre_torneo} partidos totales: {lt.size(printable)}\n{nombre_torneo} paises totales:{len(paises)}\n{nombre_torneo} total de ciudades: {len(ciudades)}\n")
    
    if len(list) > 6:
        print("Se han encontrado mas de 6 resultados: ")
        ult = list[:3]
        prim = list[-3:]
        print(tabulate(ult + prim, headers="keys", tablefmt="grid"))
    else:
        print("se han encontrado los siguientes resultados: ")
        print(tabulate(list, headers="keys", tablefmt="grid"))

#-------------------------------------------------------------------------------------------------    
#------------------------------------------Requerimiento 5----------------------------------------

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print("==========Req No. 5 outputs==========")
    printable, penaltis, autogoles, torneos, tiempo = controller.getDatabyPlayer(control, nombre, fecha_inicio, fecha_fin)
      
    list = []
    for i in lt.iterator(printable):
        i.pop("scorer")
        list.append(i)
    
    print(f"=============== Req 5 Inputs ===============\n\nJugador: {nombre}\nFecha inicio: {fecha_inicio}\nFecha final: {fecha_fin}\n")
    print(f"=============== Req 5 Results ===============\n\n{nombre} goles totales: {lt.size(printable)}\n{nombre} torneos totales:{torneos}\n{nombre} total de penalties: {penaltis}\n{nombre} total de autogoles: {autogoles}\n")
    
    if len(list) > 6:
        print("Se han encontrado mas de 6 resultados: ")
        ult = list[:3]
        prim = list[-3:]
        print(tabulate(ult+prim, headers="keys", tablefmt="grid"))
    else: 
        print("Se han encontrado los siguientes resultados: ")
        print(tabulate(list, headers="keys", tablefmt="grid"))
        
    print("Goles", lt.size(printable), "Penales", penaltis, "Autos", autogoles)

#-----------------------------------------------------------------------------------------------
#------------------------------------------Requerimiento 6--------------------------------------

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print("==========Req No. 6 outputs==========")
    partidos_total, partidos_torneo, paises, ciudades, city, respuesta_final, tiempo = controller.getBestTeams(control, numero_equipos, fecha_inicio, fecha_fin)
    
    if lt.size(respuesta_final) > 6:
        print(respuesta_final)
    else: 
        print(tabulate(respuesta_final["elements"], headers = "keys", tablefmt="grid"))
        

#-----------------------------------------------------------------------------------------------
#------------------------------------------Requerimiento 7--------------------------------------

def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print("==========Req No. 4 outputs==========")
    printable = controller.getBestPlayers(control)
    print(printable)

#-----------------------------------------------------------------------------------------------
#------------------------------------------Requerimiento 8--------------------------------------

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    n_years1, n_matches1, home_matches1, away_matches1, oldest_date1, newest_match1, elements1, n_years2, n_matches2, home_matches2, away_matches2, oldest_date2, newest_match2, elements2, n_joint_matches, joint_wins1, joint_losses1, joint_wins2, joint_losses2, joint_draws, newest_joint_match, scores, team1, team2 =controller.req_8(control)
    for element in elements1:
        if type(element['top_scorer'])==dict:
            element['top_scorer']=tabulate([element['top_scorer']], headers="keys", tablefmt="grid")
    for element in elements2:
        if type(element['top_scorer'])==dict:
            element['top_scorer']=tabulate([element['top_scorer']], headers="keys", tablefmt="grid")
    print(f'{"-"*5}{team1} Statistics{"-"*50}')
    print(f'{"-"*5}Years: {n_years1}{"-"*50}')
    print(f'{"-"*5}Total matches: {n_matches1}{"-"*50}')
    print(f'{"-"*5}Total home matches: {home_matches1}{"-"*50}')
    print(f'{"-"*5}Total away matches: {away_matches1}{"-"*50}')
    print(f'{"-"*5}Oldest match date: {oldest_date1}{"-"*50}')
    print(f'{"-"*5} Newest match data {"-"*50}')
    print(f'{tabulate([newest_match1], headers="keys", tablefmt="grid")}')
    print(f'{"-"*5} Yearly statistics {"-"*50}')
    print(f'{tabulate(elements1, headers="keys", tablefmt="grid")}')

    print(f'{"-"*5}{team2} Statistics{"-"*50}')
    print(f'{"-"*5}Years: {n_years2}{"-"*50}')
    print(f'{"-"*5}Total matches: {n_matches2}{"-"*50}')
    print(f'{"-"*5}Total home matches: {home_matches2}{"-"*50}')
    print(f'{"-"*5}Total away matches: {away_matches2}{"-"*50}')
    print(f'{"-"*5}Oldest match date: {oldest_date2}{"-"*50}')
    print(f'{"-"*5} Newest match data {"-"*50}')
    print(f'{tabulate([newest_match2], headers="keys", tablefmt="grid")}')
    print(f'{"-"*5} Yearly statistics {"-"*50}')
    print(f'{tabulate(elements2, headers="keys", tablefmt="grid")}')

    print(f'{"-"*5}{team1} vs {team2} Statistics{"-"*50}')
    print(f'{"-"*5}Total matches: {n_joint_matches}{"-"*50}')
    print(f'{"-"*5}Total wins for {team1}: {joint_wins1}{"-"*50}')
    print(f'{"-"*5}Total losses for {team1}: {joint_losses1}{"-"*50}')
    print(f'{"-"*5}Total wins for {team2}: {joint_wins2}{"-"*50}')
    print(f'{"-"*5}Total losses for {team2}: {joint_losses2}{"-"*50}')
    print(f'{"-"*5}Total draws: {joint_draws}{"-"*50}')
    print(f'{"-"*5} Newest match data {"-"*50}')
    print(f'{tabulate([newest_joint_match], headers="keys", tablefmt="grid")}')
    print(f'{"-"*5} Match scores {"-"*50}')
    print(f'{tabulate(scores, headers="keys", tablefmt="grid")}')
    
#-----------------------------------------------------------------------------------------------
#------------------------------------------Menu principal---------------------------------------

# Se crea el controlador asociado a la vista
control = new_controller()
control_array = new_controller()

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
            resultados1, results = loadResults(control)
            resultados2, shootouts = loadShootouts(control)
            resultados3, goalscorers = loadGoalsco(control)
            
            print(f"=============== Resultados ===============\n\nNumero resultados cargados: {resultados1}\nNumero de goleadores cargados: {resultados2}\nNumero de partidos definidos por penalty-shootouts cargados: {resultados3}\n")
            print(f"==========================================\n========== FIFA RECORDS REPORT ===========\n==========================================\n")  
            
            lista_python = []
            
            for i in lt.iterator(results):
                lista_python.append(i)
                
            
            print("Se han cargado " + str(resultados1) + "resultados de partidos: \n")
            print("Existen mas de 6 resultados...")
            print(tabulate(lista_python[:3]+lista_python[-3:], headers="keys", tablefmt="grid"))
            print("\n")
            
            
            print("Se han cargado " + str(resultados2) + "Definiciones desde el punto penal: \n")
            print("Existen mas de 6 resultados...")
            
            lista_python = []
            for i in lt.iterator(shootouts):
                lista_python.append(i)
            
            print(tabulate(lista_python[:3] + lista_python[-3:], headers="keys", tablefmt="grid"))
            print("\n") 
            print("Se cargaron " + str(resultados3) + "goleadores: \n")
            print("Existen mas de 6 resultados...")
            
            lista_python = []
            for i in lt.iterator(goalscorers):
                lista_python.append(i)
            
            print(tabulate(lista_python[:3] + lista_python[-3:], headers="keys", tablefmt="grid"))
            print("\n")
            
        elif int(inputs) == 2:                                                          # Req. 1 : COMPLETADO
            print("==========Req No. 1 inputs==========")
            matches = int(input("Cantidad de partidos: "))
            team = input("Team name: ")
            condition = input("Condicion del equipo: ")
            print("\n")
            results, resultados, tiempo = controller.getMatchbyTeam(control, team, condition)
            print_req_1(control, matches, team, condition)
            delta_time = f"{tiempo:.3}"
            print("El tiempo de ejecucion del requerimiento 1 fue de: " + str(delta_time) + " " + "ms")
            print("\n")

        elif int(inputs) == 3:                                                          # Req. 2 : COMPLETADO
            print("==========Req No. 2 inputs==========")
            nombre = input("Nombre del jugador: ")
            size = input("Numero de goles: ")
            print("\n")
            printable, tiempo = controller.getGoalsbyPlayer(control, nombre, int(size))
            print_req_2(control)
            delta_time = f"{tiempo:.3}"
            print("El tiempo de ejecucion del requerimiento 2 fue de: " + str(delta_time) + " " + "ms")

        elif int(inputs) == 4:                                                          # Req. 3 : COMPLETADO
            print("==========Req No. 3 inputs==========")
            team = input("Nombre del equipo: ")
            fecha_inicio = input("Fecha de Inicio: ")
            fecha_fin = input("Fecha de Finalizacion: ")
            print("\n")
            print_req_3(control, team, fecha_inicio, fecha_fin)

        elif int(inputs) == 5:                                                          # Req. 4 : COMPLETADO
            print("==========Req No. 4 inputs==========")
            nombre_torneo = input("Nombre del torneo: ")
            fecha_inicio = input("Fecha de inicio: ")
            fecha_fin = input("Fecha de finalizacion: ")
            print("\n")
            printable, paises, ciudades, tiempo = controller.getDatabyTournament(control, nombre_torneo, fecha_inicio, fecha_fin)
            print_req_4(control)
            delta_time = f"{tiempo:.3}"
            print("El tiempo de ejecucion del requerimiento 4 fue de: " + str(delta_time) + " " + "ms")

        elif int(inputs) == 6:                                                          # Req. 5 : COMPLETADO
            print("==========Req No. 5 inputs==========")
            nombre = input("ingrese el nombre del jugador que desea conocer: ")
            fecha_inicio = input("Fecha de inicio: ")
            fecha_fin = input("Fecha de finalizacion: ")
            print("\n")
            printable, penaltis, autogoles, torneos, tiempo = controller.getDatabyPlayer(control, nombre, fecha_inicio, fecha_fin)
            print_req_5(control)
            delta_time = f"{tiempo:.3}"
            print("El tiempo de ejecucion del requerimiento 5 fue de: " + str(delta_time) + " " + "ms")

        elif int(inputs) == 7:                                                          # Req. 6 : EN PROCESO
            print("==========Req No. 6 inputs==========")
            scorers = input("TOP scorer ranking: ")
            fecha_inicio = input("Start date: ")
            fecha_fin = input("End date: ")
            lim_inf = input("Limite inferior: ")
            lim_sup = input("Limite superior: ")
            numero_equipos = input("Numero de equipos: ")
            torneo = input("Nombre del torneo: ")
            print("\n")
            partidos_total, partidos_torneo, paises, ciudades, city, respuesta_final = controller.getBestTeams(control, numero_equipos, torneo, lim_inf, lim_sup)
            print_req_6(control)
            delta_time = f"{tiempo:.3}"
            print("El tiempo de ejecucion del requerimiento 6 fue de: " + str(delta_time) + " " + "ms")

        elif int(inputs) == 8:                                                          # Req. 7 : COMPLETADO
            print("==========Req No. 7 inputs==========")
            printable, tiempo = controller.getBestPlayers(control)
            print_req_7(control)
            delta_time = f"{tiempo:.3}"
            print("El tiempo de ejecucion del requerimiento 7 fue de: " + str(delta_time) + " " + "ms")

        elif int(inputs) == 9:
            print_req_8(control)
            
        elif int(inputs) == 10:
            print("Seleccione el tipo de representacion de lista que desea:")
            print("1. ARRAY_LIST")
            print("2. LINKED_LIST")
            opcion = input("Seleccione una opcion") 
            if opcion == "1":
                tipo = "ARRAY_LIST"
            elif opcion == "2":
                tipo = "LINKED_LIST"
            else:
                print("No ha seleccionado una opcion valida. Se ejecutara la representacion por defecto:")
                tipo = "ARRAY_LIST"
                
            print("Seleccione el tamaño del archivo que desea manejar:")
            print("1. -20pct")
            print("2. -50pct")
            print("3. -large")
            
            tamaño = input("Elija una opcion:")
            
            if tamaño == "1":
                muestra = "-20pct"
            elif tamaño == "2":
                muestra = "-50pct"
            elif tamaño == "3":
                muestra = "-large"
            else:
                print("No ha seleccionado una opcion valida: Se seleccionara el archivo mas pequeño:")
                muestra = "-20pct"
                
            print("Elija el tipo de ordenamiento que desea utilizar: ")
            print("1- Insertion")
            print("2- Shell")
            print("3- Selection")
            sort_type = input("Elija una opcion de ordenamiento: ")
            
            if sort_type == "1":
                sort_option = "insertion"
            elif sort_type == "2":
                sort_option= "shell"
            elif sort_type == "3":
                sort_option = "selection"
            else:
                print("No ha escogido una opcion valida: Se ejecutara el ordamiento por defecto: ")
                muestra = "shell"
                
            resultados, results = loadResultsOrd(control, opcion, muestra, sort_option)
            lista_python = list_python(results)
            print("Cargando archivos...")
            print("Se cargaron" + str(resultados) + "resultados de partidos. ")
            print("Primeros 3 resultados de partidos: ")
            print(tabulate(lista_python[:3], headers="keys", tablefmt="grid"))
            print("\n")
            print("Ultimos 3 resultados de partidos: ")
            print(tabulate(lista_python[-3:], headers="keys", tablefmt="grid"))
            print("\n")
            
            resultados, goalscorers = loadGoalscorersOrd(control, opcion, muestra, sort_option)
            lista_python = list_python(goalscorers)
            print("Cargando archivos...")
            print("Se cargaron" + str(resultados) + "goleadores de torneos. ")
            print("Primeros 3 goleadores de torneos: ")
            print(tabulate(lista_python[:3], headers="keys", tablefmt="grid"))
            print("\n")
            print("Ultimos 3 goleadores de torneos: ")
            print(tabulate(lista_python[-3:], headers="keys", tablefmt="grid"))
            print("\n")
            
            resultados, shootouts = loadShootoutsOrd(control, opcion, muestra, sort_option)
            lista_python = list_python(shootouts)
            print("Cargando archivos...")
            print("Se cargaron" + str(resultados) + "resultados de partidos desde el punto penal. ")
            print("Primeros 3 resultados de partidos desde el punto penal: ")
            print(tabulate(lista_python[:3], headers="keys", tablefmt="grid"))
            print("\n")
            print("Ultimos 3 resultados de partidos desde el punto penal: ")
            print(tabulate(lista_python[-3:], headers="keys", tablefmt="grid"))
            print("\n")
            
            size = input("Indique tamaño de la muestra: ")
            time, result = controller.sort_data(int(size), control["results"], sort_option)
            print("Para", size, "elementos, delta tiempo:",
                  str(time), "[ms]\n")
                
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
