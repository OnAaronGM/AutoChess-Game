import random
import numpy as np
import actions
import utils, common_vars
from classes import Player, Pokemon
from database import queries
from collections import Counter
## NOTAS:
## CADA POKEMON EN EL TABLERO SE TIENE QUE GUARDAR EN LA MATRIZ ASI: NOMBRE_POKE:(ID USER, HP)
## random_turno = 0 -> arriba (rojo), random_turno = 1 -> abajo (azul)


def getAction() -> str:
    print("¿Qué qieres hacer?: 1: Mover Unidad, 2: Sacar Unidad, 3: Rendirse")
    action = input()
    while action not in ["1","2","3"]:
        print("Acción no valida")
        print("¿Qué qieres hacer?: 1: Mover Unidad, 2: Sacar Unidad, 3: Rendirse")
        action = input()
    return action
    

def doAction(table: list, player_att: Player, player_def: Player, turno: int) -> bool:
    finish_turn = False
    while not finish_turn:
        action = getAction()
        if action == "1": ## Si acción mover unidad, preguntar desde que posición y posición final.
            finish_turn = actions.move_unidad(table,player_att, player_def)
        elif action == "2":
            finish_turn = actions.sacar_unidad(table, player_att, turno)
        else:
            finish_turn = True

def jugar_partida():
    ## Bucle principal de la partida    
    finish_game = False
    table = utils.create_table() ## Generamos el tablero inicial con los equipos
    p1 = Player(id=1, team=[Pokemon(*unity + (1,)) for unity in queries.select_team(1)])
    p2 = Player(id=2, team=[Pokemon(*unity+(2,)) for unity in queries.select_team(2)])
    colors = {p1.id:"red",p2.id:"blue"}
    utils.print_table(table,p1.get_team_bench(),p2.get_team_bench(),colors)
    
    random_orden_turno = random.randint(0, 1)
    random_orden_turno = 0
    while not finish_game:
        #random_turno = 0 -> arriba (rojo), random_turno = 1 -> abajo (azul). Arriba siempre p1, abajo siempre p2
        if random_orden_turno == 0:
            print("Jugador rojo es su turno \n")
            doAction(table,p1,p2,random_orden_turno)
            utils.print_table(table,p1.get_team_bench(),p2.get_team_bench(),colors)
            print("Jugador azul es su turno \n")
            doAction(table,p2,p1,random_orden_turno + 1)
            utils.print_table(table,p1.get_team_bench(),p2.get_team_bench(),colors)
        else:
            doAction(table,p2,p1, random_orden_turno)
            doAction(table,p1,p2, random_orden_turno - 1)
        #utils.print_table(table,p1.team_bench,p2.team_bench)
        #finish_game = True
        
def invocar(id_user: int):
    list_of_rarities_summoned = np.random.choice(common_vars.rarity_pokemon[0],10, p = common_vars.rarity_pokemon[1])
    counter = Counter(list_of_rarities_summoned)
    print("ENHORABUENA, HAS OBTENIDO A:\n")
    for key, value in counter.items():
        l_poke_key = queries.get_list_poke_by_rarity(key)
        indexes= np.random.choice(len(l_poke_key),value,[100 / len(l_poke_key)] * len(l_poke_key))
        for index in indexes:
            print(l_poke_key[index][1])
            queries.check_poke_exists_in_inventory(id_user, int(l_poke_key[index][0]))
    return
    
def login():
    print("Inserte usuario: ")
    user = input()
    id_user = queries.get_user(user)
    while not id_user:
        print("Usuario incorrecto\n")
        print("Inserte usuario: ")
        user = input()
        id_user = queries.get_user(user)
    return id_user[0][0]
        
    
def main():
    print("Bienvenido a AutoChessPoke\n".center(70))
    id_user = login()
    #print("Inserte password: ")
    #password = input()
    
    print("Indique que quiere hacer:\n".center(70))
    print("1: Invocar   2: Jugar\n".center(70))
    accion = input()
    if accion == "1":
        invocar(id_user)
    elif accion == "2":
        jugar_partida()
    
    

if __name__ == "__main__":
    main()
    #start_game()