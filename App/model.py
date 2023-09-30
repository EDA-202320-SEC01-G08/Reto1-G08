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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from datetime import datetime as dt
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from tabulate import tabulate

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
    
    catalog["results"] = lt.newList("ARRAY_LIST", cmpfunction=compareresults)
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
    if opcion_array == "1":
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

def date_filter(data_struct, fechainicio:str, fechafin:str):
    fecha_inicio = fechainicio.split("-")
    fecha_fin = fechafin.split("-")
    
    filtered_data = lt.newList("SINGLE_LINKED", cmpfunction=comparetournament)
    
    for each in lt.iterator(data_struct):
        date = each["date"].split("-")
        if date >= fecha_inicio and date <= fecha_fin:
            lt.addLast(filtered_data, each)
        
    return filtered_data

def date_filter_player(data_struct, fechainicio:str, fechafin:str):
    fecha_inicio = fechainicio.split("-")
    fecha_fin = fechafin.split("-")
    
    filtered_data = lt.newList("SINGLE_LINKED", cmpfunction=compareresults)
    
    for each in lt.iterator(data_struct):
        date = each["date"].split("-")
        if date >= fecha_inicio and date <= fecha_fin:
            lt.addLast(filtered_data, each)
        
    return filtered_data

def rango_by_fecha(fecha, limite_inferior, limite_superior):
    """
    Devuelve verdadero (True) si la fecha esta dentro del rango estipulado.
    Args:
        Fecha: fecha a comparar
        limite_inferior: fecha en la que incia el rango.
        imite_superior: fecha en la que termina el rango. 
    """
    rta = False
    fecha = ((dt.strptime(fecha,"%Y-%m-%d")).date()).toordinal()
    limite_inferior = ((dt.strptime(limite_inferior,"%Y-%m-%d")).date()).toordinal()
    limite_superior = ((dt.strptime(limite_superior,"%Y-%m-%d")).date()).toordinal()
    if (fecha >= limite_inferior) and (fecha <= limite_superior):
        rta = True
    return rta

def find_goal_scorers_2(goal_scorers, partidos):

    rta = lt.newList("ARRAY_LIST")

    for partido in lt.iterator(partidos):
        for anotacion in lt.iterator(goal_scorers):
            if (anotacion["date"] == partido["date"]) and (anotacion["home_team"] == partido["home_team"]) and (anotacion["away_team"] == partido["away_team"]):
                lt.addFirst(rta, anotacion)

    return rta

def find_teams(goal_scorers, teams):
    teams_final = lt.newList("ARRAY_LIST")
    for team in lt.iterator(teams):
        for s in lt.iterator(goal_scorers):
            if lt.isPresent(teams_final, s["team"]) == 0:
                        lt.addLast(teams_final, s["team"])

    return teams_final

def calcular_puntos_victorias_empates_derrotas(partido, team):
    """Funcion que calcula las victorias, derrotas o empates de 
    un equipo, a la vez que calcula sus puntos por cada una de estas"""
    puntos = 0
    victoria = 0
    derrota = 0
    empate = 0

    if ((int(partido["away_score"]) > int(partido["home_score"])) and partido["away_team"] == team) or ((int(partido["home_score"]) > int(partido["away_score"])) and partido["home_team"] == team):
        puntos = 3
        victoria = 1
    elif int(partido["away_score"]) == int(partido["home_score"]):
        puntos = 1
        empate = 1
    else:
        derrota = 1
    return puntos, victoria, empate, derrota

def diferencia_goles (partido, team):
    """Funcion que calcula los goles a favor y en contra de un equipo,
    con los cuales cacula la diferencia"""

    if partido["home_team"]== team:
        favor = int(partido["home_score"])
        contra = int(partido["away_score"])
    else:
        favor = int(partido["away_score"])
        contra = int(partido["home_score"])
    diferencia = favor - contra
    return favor, contra, diferencia

def find_best_player_own_goals_penalties_req_6(goal_scorers, team):

    """Funcion que calcula los autogoles, los penales y busca el mejor
    jugador a partir de un equipo y una isto filtrada de goal scorers"""

    autogoles = 0
    penales = 0
    goleadores = {}
    rta = lt.newList("ARRAY_LIST")

    for jugador in lt.iterator(goal_scorers):
        if jugador["away_team"] == team or jugador["home_team"] == team:

            if jugador["own_goal"] == "True" and jugador["team"] == team:
                autogoles += 1
            if jugador["penalty"] == "True"  and jugador["team"] == team:
                penales += 1
        
            if jugador["own_goal"] != "True":

                if jugador["scorer"] not in goleadores:
                    goleadores[jugador["scorer"]] = {}
                    goleadores[jugador["scorer"]]["goles"] = 1
                    goleadores[jugador["scorer"]]["partidos"] = [jugador["date"]]
                    goleadores[jugador["scorer"]]["minutos"] = float(jugador["minute"])
                    
                else:
                    goleadores[jugador["scorer"]]["goles"] += 1
                    if jugador["date"] not in goleadores[jugador["scorer"]]["partidos"]:
                        goleadores[jugador["scorer"]]["partidos"].append(jugador["date"])
                    goleadores[jugador["scorer"]]["minutos"] += float(jugador["minute"])

    if len(goleadores) > 1:
        mayor = -1
        for scorer, data in goleadores.items():
            if data["goles"] > mayor:
                mayor = data["goles"]
                top = scorer
        

        for scorer, data in goleadores.items():
            if (data["goles"] == mayor) and (scorer == top):
                promedio = round( data["minutos"]/ data["goles"])

                top_scorer = {"scorer": scorer,
                            "goals" : data["goles"],
                            "matches" : len(data["partidos"]),
                            "avg_time" : promedio
                            }
                lt.addFirst(rta, top_scorer)
    
    else:
        for scorer, data in goleadores.items():
                promedio = round( data["minutos"]/ data["goles"])

                top_scorer = {"scorer": scorer,
                            "goals" : data["goles"],
                            "matches" : len(data["partidos"]),
                            "avg_time" : promedio
                            }
                lt.addFirst(rta, top_scorer)

    return autogoles, penales, rta

def cmp_total_point(points_1, points_2):
    rta = False
    puntos_1 = points_1["total_points"]
    puntos_2 = points_2["total_points"]
    diferencia_1 = points_1["goal_difference"]
    diferencia_2 = points_2["goal_difference"]
    penal_1 = points_1["penalty_points"]
    penal_2 = points_2["penalty_points"]
    if puntos_1 > puntos_2:
        rta = True
    elif puntos_1 == puntos_2:
        if diferencia_1 > diferencia_2:
            rta = True
        elif diferencia_1 == diferencia_2:
            if penal_1 > penal_2:
                rta = True
    return rta

#-------------------------------------------------------------------------------------------
#--------------------------------------Requerimiento 1--------------------------------------

def getMatchbyTeam(data_structs, team, condition):
    
    results = lt.newList("ARRAY_LIST")
    for data in lt.iterator(data_structs):
        if condition == "local":
            if data["home_team"] == team:
                lt.addLast(results, data)
        elif condition == "visitante":
            if data["away_team"] == team:
                lt.addLast(results, data)
        elif condition == "indiferente":
            if data["neutral"] == True:
                lt.addLast(results, data)

    list_results = []
    
    for i in lt.iterator(results):
        list_results.append(i)
    return list_results

#-------------------------------------------------------------------------------------------
#---------------------------------------Requerimiento 2-------------------------------------

def getGoalsbyPlayer(data_structs, nombre, size):
    data_player = lt.newList("SINGLE_LINKED", cmpfunction=compareresults)
    counting = 0
    
    for resultado in lt.iterator(data_structs):
        if resultado["scorer"] == nombre:
            lt.addLast(data_player, resultado)
            
    sort(data_player)
    list = []
    
    for i in lt.iterator(data_player):
        list.append(i)
        
    return list[:size]

#--------------------------------------------------------------------------------------------
#---------------------------------------Requerimiento 3--------------------------------------

def getResultsbyTeam(data_structs_results, data_structs_goalscorers, team, fecha_inicio, fecha_fin):
    
    results = lt.newList("ARRAY_LIST")
    list_results=[]
    
    for data1 in lt.iterator(data_structs_results):
        if (team not in (data1["home_team"], data1["away_team"])):
            continue
        if not (getDate(fecha_inicio) <= getDate(data1["date"]) <= getDate(fecha_fin)):
            continue
        
        del data1["neutral"]
        data1["penalty"] = data1["own_goal"] = "Unknown"
        for data2 in lt.iterator(data_structs_goalscorers):
             if data1['date'] == data2['date'] and data1['home_team'] == data2['home_team']:
                data1["own_goal"], data1["penalty"] = data2["own_goal"], data2["penalty"]
        data1["own_goal"] = True
        list_results.append(data1)
    
    counting_home=0
    counting_away=0  
    
    for data in list_results:
        if data["home_team"] == team:
            counting_home += 1
        else:
            counting_away += 1
        
    return list_results, counting_home, counting_away

#--------------------------------------------------------------------------------------------
#--------------------------------------Requerimiento 4---------------------------------------

def getDatabyTournament(data_structs_results, data_structs_shootouts, id, fecha_inicio, fecha_fin):
    data = lt.newList("ARRAY_LIST", cmpfunction=comparetournament)
    countries = []
    cities = []
    
    for register in lt.iterator(data_structs_results):
        if register["tournament"].lower() == id.lower():
            lt.addLast(data, register)
    
    sort(data)
    
    for each1 in lt.iterator(data):
        each1['winner'] = "Unknown"
        for each2 in lt.iterator(data_structs_shootouts):
            if each1['date'] == each2['date'] and each1['home_team'] == each2['home_team'] and each1['home_team'] == each2['home_team']:
                each1['winner'] = each2['winner']
                
    new_data = date_filter(data, fecha_inicio, fecha_fin)
    for i in lt.iterator(new_data):
        if i['country'] not in countries:
            countries.append(i["country"])
        if i['city'] not in cities:
            cities.append(i['city'])
    
    return new_data, countries, cities

#--------------------------------------------------------------------------------------------
#--------------------------------------Requerimiento 5---------------------------------------

def getDatabyPlayer(data_structs_goalscorers, data_structs_results, id, fecha_inicio, fecha_fin):
    data_player = lt.newList("SINGLE_LINKED", cmpfunction=compareresults)
    data_results = lt.newList("SINGLE_LINKED", cmpfunction=comparetournament)
    
    tournaments = []
    penalties = []
    own_goals = []
    
    for register in lt.iterator(data_structs_goalscorers):
        if register["scorer"].lower() == id.lower():
            lt.addLast(data_player, register)
            
    for each1 in lt.iterator(data_player):
        each1['home_score'] = "Unknown"
        each1['away_score'] = "Unknown"
        each1['tournament'] = "Unknown" 
        for each2 in lt.iterator(data_structs_results):
            if each1['date'] == each2['date'] and each1['home_team'] == each2['home_team'] and each1['home_team'] == each2['home_team']:
                each1['home_score'] = each2['home_score']
                each1['away_score'] = each2['away_score']
                each1['tournament'] = each2['tournament'] 
                
    sort(data_player)
    new_data = date_filter_player(data_player, fecha_inicio, fecha_fin)
    
    for i in lt.iterator(new_data):
        if i['tournament'] not in tournaments:
            tournaments.append(i["tournament"])
        if i['penalty'] == "True":
            penalties.append(1)
        if i['own_goal'] == "True":
            own_goals.append(1)
            
    return new_data, len(penalties), len(own_goals), len(tournaments)

#--------------------------------------------------------------------------------------------
#--------------------------------------Requerimiento 6---------------------------------------

def req_6(control, numero_equipos, torneo, lim_inf, lim_sup):

    current_date = ((dt.strptime(lim_sup,"%Y-%m-%d")).date()).toordinal()
    top_date = ((dt.strptime(lim_inf,"%Y-%m-%d")).date()).toordinal()
    resultados = control["results"]
    partidos_torneo = lt.newList("ARRAY_LIST")
    paises = lt.newList("ARRAY_LIST")
    ciudades = lt.newList("ARRAY_LIST")
    ciudades_mas_partidos = {}
    maximo = 0
    scorers = control["goal_scorers"]
    scorers_2 = lt.newList("ARRAY_LIST")
    teams = lt.newList("ARRAY_LIST")
    rta = lt.newList("ARRAY_LIST")
    i = 1

    while current_date >= top_date:
        r = lt.getElement(control["results"], i)
        if r["tournament"] == torneo:
            fecha = r["date"]
            if rango_by_fecha(fecha, lim_inf, lim_sup) == True:
                lt.addLast(partidos_torneo, r)
                if lt.isPresent(paises, r["country"]) == 0:
                    lt.addLast(paises, r["country"])
                if lt.isPresent(ciudades, r["city"]) == 0: 
                    lt.addLast(ciudades, r["city"])
                if r["city"]  not in ciudades_mas_partidos:
                    ciudades_mas_partidos[r["city"]] = 1
                else: 
                    ciudades_mas_partidos[r["city"]] +=1 

                if ciudades_mas_partidos[r["city"]] > maximo:
                    maximo = ciudades_mas_partidos[r["city"]]
                if ciudades_mas_partidos[r["city"]] == maximo:
                    ciudad = r["city"]

                lt.addLast(teams, r["home_team"])


        current_date = ((dt.strptime( r["date"],"%Y-%m-%d")).date()).toordinal()
        i += 1

    scorers = find_goal_scorers_2(control["goal_scorers"], partidos_torneo)
    teams_final = find_teams(scorers, teams)

    for equipo in lt.iterator(teams_final):
        puntos = 0
        diferencia = 0
        victorias = 0
        empates = 0
        derrotas = 0
        favor = 0
        contra = 0
        autogoles = 0
        penales = 0
        maximo = 0
        jugador = "Unknown"
        matches = 0
        for partido in lt.iterator(partidos_torneo):
                
                if partido["away_team"]== equipo or partido["home_team"]== equipo:
                    matches += 1
                    punto, victoria, empate, derrota = calcular_puntos_victorias_empates_derrotas(partido, equipo)
                    puntos += punto
                    victorias += victoria
                    empates += empate
                    derrotas += derrota 
                    favor_1, contra_1, diferencia_1 = diferencia_goles(partido, equipo)
                    favor += favor_1
                    contra += contra_1
                    diferencia += diferencia_1
        autogoles, penales, jugador = find_best_player_own_goals_penalties_req_6(scorers, equipo)

        dict_equipo = {
            "team" : equipo,
            "total_points" : puntos,
            "goal_difference" : diferencia,
            "penalty_points" : penales,
            "matches" : matches,
            "own_goal_points" : autogoles,
            "wins" : victorias,
            "draws" : empates,
            "losses" : derrotas,
            "goals_for" : favor,
            "goals_against" : contra,
            "top_scorer" : tabulate(jugador["elements"], headers="keys",tablefmt="grid")
        }

        lt.addLast(rta, dict_equipo)
    
    respuesta_final = sa.sort(rta, cmp_total_point)
    if lt.size(rta) > int(numero_equipos):
        respuesta_final = lt.subList(rta, 1, int(numero_equipos))
    return lt.size(teams_final), lt.size(partidos_torneo), lt.size(paises), lt.size(ciudades), ciudad, respuesta_final

#--------------------------------------------------------------------------------------------
#--------------------------------------Requerimiento 7---------------------------------------

def getBestPlayers(data_structs, fecha_inicio, fecha_fin, amount):
    
    relevant_matches = lt.newList(datastructure="ARRAY_LIST")
    matches_position = {}

    fecha_inicio = getDate(fecha_inicio)
    fecha_fin = getDate(fecha_fin)

    for i in lt.iterator(data_structs["results"]):
        if i["tournament"] != "Friendly" and (fecha_inicio <= getDate(i["date"]) <= fecha_fin):
            lt.addLast(relevant_matches, i)
            matches_position[f"{i['date']}={i['home_team']}={i['away_team']}"] = lt.size(relevant_matches)

    scorers = lt.newList(datastructure="ARRAY_LIST")
    scorers_position = {}

    for i in lt.iterator(data_structs["goalscorers"]):
        matchPosition = matches_position.get(f"{i['date']}={i['home_team']}={i['away_team']}", 0)

        if matchPosition == 0:
            continue

        match = lt.getElement(relevant_matches, matchPosition)

        player = {
            "name": i["scorer"],
            "score": 0,
            "goals": 0,
            "own_goals": 0,
            "penalties": 0,
            "times": [],
        }

        position = scorers_position.get(i["scorer"], -1)

        if position == -1:
            lt.addLast(scorers, player)
            scorers_position[i["scorer"]] = lt.size(scorers)
            position = scorers_position[i["scorer"]]

        player = lt.getElement(scorers, position)

        player["goals"] += 0 if i["own_goal"] else 1
        player["own_goals"] += 1 if i["own_goal"] else 0
        player["penalties"] += 1 if i["penalty"] else 0
        player["score"] = player["goals"] + player["penalties"]
        if i["minute"] != "":
            player["times"].append(float(i["minute"]))

        lt.changeInfo(scorers, position, player)

    merg.sort(scorers, sort_by_score)

    amount = min(amount, lt.size(scorers))

    scorers = lt.subList(scorers, 1, amount)

    print(scorers)
    return scorers

#-------------------------------------------------------------------------------------------

def getDate(date):
    return dt.strptime(date, "%Y-%m-%d")

def convert_to_list(data_structs):
    lista_structs=[]
    for i in lt.iterator(data_structs):
        lista_structs.append(i)
        
    return lista_structs

def req_1(numero_partidos, nombre_equipo, condicion):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    


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


def req_8(data_structs, team1, team2, start_d, end_d):
    """
    Función que soluciona el requerimiento 8
    """
   
    date_frmt1 = ([int(x) for x in (start_d.split('-'))])
    date_frmt2 = ([int(x) for x in (end_d.split('-'))])
    start_d = date(*date_frmt1)
    end_d=date(*date_frmt2)
    years_1 = lt.newList('ARRAY_LIST', cmpfunction=compare_years)
    matches_1 = lt.newList('ARRAY_LIST',cmpfunction=compare_matches)
    home_matches1=0
    away_matches1=0
    years_2 = lt.newList('ARRAY_LIST', cmpfunction=compare_years)
    matches_2 = lt.newList('ARRAY_LIST',cmpfunction=compare_matches)
    home_matches2=0
    away_matches2=0
    joint_wins1=0
    joint_wins2=0
    joint_losses1=0
    joint_losses2=0
    joint_draws=0
    joint_matches = lt.newList('ARRAY_LIST',cmpfunction=compare_matches)
    joint_scores = lt.newList('ARRAY_LIST')
    for match in lt.iterator(data_structs['match_results']):
        if match['tournament']!='Friendly' and start_d<match['date']<end_d:
            if (match['away_team'] == team1 or match['home_team']==team1):
                lt.addLast(matches_1, match)
                year_comp = {'year':match['date'].year}
                year = lt.isPresent(years_1, year_comp)
                if not year:
                    new_year = {'year':match['date'].year,'matches':0, 'total_points':0, 'goal_difference':0, 'penalties':0, 'own_goals':0, 'wins':0, 'draws':0, 'losses':0, 'goals_for':0, 'goals_against':0, 'top_scorer':lt.newList('ARRAY_LIST',compare_players)}
                    lt.addLast(years_1, new_year)
                    year = lt.size(years_1)
                winner = winner_determiner(match)
                modify_year = lt.getElement(years_1, year)
                modify_year['matches']+=1
                if match['away_team']==team1:
                    away_matches1+=1
                    if winner == 'away':
                        modify_year['total_points']+=3
                        modify_year['wins']+=1
                    elif winner =='draw':
                        modify_year['total_points']+=1
                        modify_year['draws']+=1
                    elif winner =='home':
                        modify_year['losses']+=1
                    modify_year['goals_for']+=int(match['away_score'])
                    modify_year['goals_against']+=int(match['home_score'])
                    modify_year['goal_difference']+=int((match['away_score']))-int(match['home_score'])
                elif match['home_team']==team1:
                    home_matches1+=1
                    if winner == 'away':
                        modify_year['losses']+=1
                    elif winner =='draw':
                        modify_year['total_points']+=1
                        modify_year['draws']+=1
                    elif winner =='home':
                        modify_year['wins']+=1
                        modify_year['total_points']+=3
                    modify_year['goals_for']+=int(match['home_score'])
                    modify_year['goals_against']+=int(match['away_score'])
                    modify_year['goal_difference']+=int((match['home_score']))-int(match['away_score'])
                lt.changeInfo(years_1,year, modify_year)

            if (match['away_team'] == team2 or match['home_team']==team2):
                lt.addLast(matches_2, match)
                year_comp = {'year':match['date'].year}
                year = lt.isPresent(years_2, year_comp)
                if not year:
                    new_year = {'year':match['date'].year,'matches':0, 'total_points':0, 'goal_difference':0, 'penalties':0, 'own_goals':0, 'wins':0, 'draws':0, 'losses':0, 'goals_for':0, 'goals_against':0, 'top_scorer':lt.newList('ARRAY_LIST',compare_players)}
                    lt.addLast(years_2, new_year)
                    year = lt.size(years_2)
                winner = winner_determiner(match)
                modify_year = lt.getElement(years_2, year)
                modify_year['matches']+=1
                if match['away_team']==team2:
                    away_matches2+=1
                    if winner == 'away':
                        modify_year['total_points']+=3
                        modify_year['wins']+=1
                    elif winner =='draw':
                        modify_year['total_points']+=1
                        modify_year['draws']+=1
                    elif winner =='home':
                        modify_year['losses']+=1
                    modify_year['goals_for']+=int(match['away_score'])
                    modify_year['goals_against']+=int(match['home_score'])
                    modify_year['goal_difference']+=int((match['away_score']))-int(match['home_score'])
                elif match['home_team']==team2:
                    home_matches2+=1
                    if winner == 'away':
                        modify_year['losses']+=1
                    elif winner =='draw':
                        modify_year['total_points']+=1
                        modify_year['draws']+=1
                    elif winner =='home':
                        modify_year['wins']+=1
                        modify_year['total_points']+=3
                    modify_year['goals_for']+=int(match['home_score'])
                    modify_year['goals_against']+=int(match['away_score'])
                    modify_year['goal_difference']+=int((match['home_score']))-int(match['away_score'])
                lt.changeInfo(years_2,year, modify_year)
            
            if (match['away_team']==team1 or match['home_team']==team1) and (match['away_team']==team2 or match['home_team']==team2):    
                winner = winner_determiner(match)  
                lt.addLast(joint_matches, match)  
                if winner == 'draw':
                    joint_draws+=1
                elif match['away_team']==team1:
                    if winner=='away':
                        joint_wins1+=1
                        joint_losses2+=1
                    elif winner =='home':
                        joint_wins2+=1
                        joint_losses1+=1
                elif match['home_team']==team1:
                    if winner=='away':
                        joint_wins2+=1
                        joint_losses1+=1
                    elif winner =='home':
                        joint_wins1+=1
                        joint_losses2+=1

    for score in lt.iterator(data_structs['scores']):
        if start_d<score['date']<end_d:
                if score['team']==team1:
                    pos = lt.isPresent(matches_1,score)
                    if pos:
                        score_yr = {'year':score['date'].year}
                        year = lt.isPresent(years_1, score_yr)
                        if year:
                            modify_year = lt.getElement(years_1, year)
                            if score['own_goal']=='True':
                                modify_year['own_goals']+=1
                            if score['penalty']=='True':
                                modify_year['penalties']+=1
                            player = lt.isPresent(modify_year['top_scorer'],score)
                            if not player:
                                new_player = {'scorer':score['scorer'],'goals':1,'matches':lt.newList('ARRAY_LIST',compare_matches), 'avg_time':float(score['minute'])}
                                lt.addLast(new_player['matches'], score)
                                lt.addLast(modify_year['top_scorer'],new_player)
                            else:
                                modify_player =  lt.getElement(modify_year['top_scorer'],player)
                                modify_player['goals']+=1
                                player_match = lt.isPresent(modify_player['matches'],score)
                                if not player_match:
                                    lt.addLast(modify_player['matches'],score)
                                modify_player['avg_time']= (modify_player['avg_time']*(modify_player['goals']-1)+float(score['minute']))/modify_player['goals']
                                lt.changeInfo(modify_year['top_scorer'],player,modify_player)
                            lt.changeInfo(years_1, year, modify_year)

                if score['team']==team2:
                    pos = lt.isPresent(matches_2,score)
                    if pos:
                        score_yr = {'year':score['date'].year}
                        year = lt.isPresent(years_2, score_yr)
                        if year:
                            modify_year = lt.getElement(years_2, year)
                            if score['own_goal']=='True':
                                modify_year['own_goals']+=1
                            if score['penalty']=='True':
                                modify_year['penalties']+=1
                            
                            player = lt.isPresent(modify_year['top_scorer'],score)
                            if not player:
                                new_player = {'scorer':score['scorer'],'goals':1,'matches':lt.newList('ARRAY_LIST',compare_matches), 'avg_time':float(score['minute'])}
                                lt.addLast(new_player['matches'], score)
                                lt.addLast(modify_year['top_scorer'],new_player)
                            else:
                                modify_player =  lt.getElement(modify_year['top_scorer'],player)
                                modify_player['goals']+=1
                                player_match = lt.isPresent(modify_player['matches'],score)
                                if not player_match:
                                    lt.addLast(modify_player['matches'],score)
                                modify_player['avg_time']= (modify_player['avg_time']*(modify_player['goals']-1)+float(score['minute']))/modify_player['goals']
                                lt.changeInfo(modify_year['top_scorer'],player,modify_player)  
                            lt.changeInfo(years_2, year, modify_year) 
                if (score['away_team']==team1 or score['home_team']==team1)and (score['away_team']==team2 or score['home_team']==team2):
                    pos = lt.isPresent(joint_matches,score)
                    if pos:
                        lt.addLast(joint_scores, score)
    length1 = lt.size(years_1)
    if lt.size(years_1)>6:
        firstelements1 = [(lt.getElement(years_1, x))for x in range(1,4) ]
        lastelements1 = [(lt.getElement(years_1, x))for x in range(length1-2,length1+1) ]
        elements1 = firstelements1+lastelements1
    else: 
        elements1 = [x for x in lt.iterator(years_1)]    

    length2 = lt.size(years_2)
    if lt.size(years_2)>6:
        firstelements2 = [(lt.getElement(years_2, x))for x in range(1,4) ]
        lastelements2 = [(lt.getElement(years_2, x))for x in range(length2-2,length2+1) ]
        elements2 = firstelements2+lastelements2
    else: 
        elements2 = [x for x in lt.iterator(years_2)] 

    for element in elements1:
        if lt.size(element['top_scorer']):
            element['top_scorer']=lt.firstElement(element['top_scorer'])
            element['top_scorer']['matches']=lt.size(element['top_scorer']['matches'])
        else:
            element['top_scorer']='No scores registered for this year.'
    for element in elements2:
        if lt.size(element['top_scorer']):
            element['top_scorer']=lt.firstElement(element['top_scorer'])
            element['top_scorer']['matches']=lt.size(element['top_scorer']['matches'])
        else:
            element['top_scorer']='No scores registered for this year.'

    n_years1=lt.size(years_1)
    n_years2=lt.size(years_2)
    n_matches1 = lt.size(matches_1)
    n_matches2 = lt.size(matches_2)
    oldest_date1= lt.lastElement(matches_1)['date']
    oldest_date2= lt.lastElement(matches_2)['date']
    newest_match1= lt.firstElement(matches_1)
    newest_match2= lt.firstElement(matches_2)
    n_joint_matches = lt.size(joint_matches)
    newest_joint_match = lt.firstElement(joint_matches)

    length_score = lt.size(joint_scores)
    if length_score>6:
        firstelements = [(lt.getElement(joint_scores, x))for x in range(1,4) ]
        lastelements = [(lt.getElement(joint_scores, x))for x in range(length_score-2,length_score+1) ]
        scores = firstelements+lastelements
    else: 
        scores = [x for x in lt.iterator(joint_scores)] 
    
    return n_years1, n_matches1, home_matches1, away_matches1, oldest_date1, newest_match1, elements1, n_years2, n_matches2, home_matches2, away_matches2, oldest_date2, newest_match2, elements2, n_joint_matches, joint_wins1, joint_losses1, joint_wins2, joint_losses2, joint_draws, newest_joint_match, scores



# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento

def sortThings(catalog, sort_criteria, size):
    numero = lt.size(catalog)
    if size > numero:
        return "Tamaño demasiado grande"
    
    sub_lista = lt.subList(catalog, 1, size)
    sort(sub_lista, sort_criteria)


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    return (str(data_1["date"]) > str(data_2["date"]))

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
        
def comparetournament(name, result):
    if name.lower() == result["tournament"].lower():
        return 0
    elif name.lower() > result["tournament"].lower():
        return 1
    return -1

def compareresults(name, result):
    if name.lower() == result["scorer"].lower():
        return 0
    elif name.lower() > result["scorer"].lower():
        return 1
    return -1

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