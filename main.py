import numpy as np
from termcolor import colored
import random
import actions
import common_vars
import utils
from classes import Player, Pokemon
from database import queries
## NOTAS:
## CADA POKEMON EN EL TABLERO SE TIENE QUE GUARDAR EN LA MATRIZ ASI: NOMBRE_POKE:(ID USER, HP)
## id_user = 0 -> arriba (rojo), id_user = 1 -> abajo (azul)


def getAction() -> str:
    print("¿Qué qieres hacer?: 1: Mover Unidad, 2: Sacar Unidad, 3: Rendirse")
    action = input()
    while action not in ["1","2","3"]:
        print("Acción no valida")
        print("¿Qué qieres hacer?: 1: Mover Unidad, 2: Sacar Unidad, 3: Rendirse")
        action = input()
    return action
    

def doAction(table: list, player: Player):
    finish_turn = False
    while not finish_turn:
        action = getAction()
        if action == "1": ## Si acción mover unidad, preguntar desque que posición y posición final.
            finish_turn = actions.move_unidad(table,player)
        elif action == "2":
            finish_turn = actions.sacar_unidad(table, player)
        else:
            finish_turn = True

def start_game():
    ## Bucle principal de la partida    
    finish_game = False
    table = utils.create_table() ## Generamos el tablero inicial con los equipos
    p1 = Player(id=1, team=[Pokemon(*unity) for unity in queries.select_team(1)])
    p2 = Player(id=2, team=[Pokemon(*unity) for unity in queries.select_team(2)])
    
    utils.print_table(table,p1.team_bench,p2.team_bench)
    
    random_orden_turno = random.randint(0, 1)
    random_orden_turno = 0
    while not finish_game:
        ## 1 en random_turno -> Empieza usuario, 2 en random_turno -> Empieza IA
        if random_orden_turno == 0:
            print("Jugador rojo es su turno \n")
            doAction(table,p1)
            utils.print_table(table,p1.team_bench,p2.team_bench)
            print("Jugador azul es su turno \n")
            doAction(table,p2)
            utils.print_table(table,p1.team_bench,p2.team_bench)
        else:
            doAction(table,p2)
            doAction(table,p1)
        #utils.print_table(table,p1.team_bench,p2.team_bench)
        #finish_game = True
        
        

if __name__ == "__main__":
    start_game()