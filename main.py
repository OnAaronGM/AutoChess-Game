import random
import actions
import utils
from classes import Player, Pokemon
from database import queries
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

def start_game():
    ## Bucle principal de la partida    
    finish_game = False
    table = utils.create_table() ## Generamos el tablero inicial con los equipos
    p1 = Player(id=1, team=[Pokemon(*unity + (1,)) for unity in queries.select_team(1)])
    p2 = Player(id=2, team=[Pokemon(*unity+(2,)) for unity in queries.select_team(2)])
    colors = {p1.id:"red",p2.id:"blue"}
    utils.print_table(table,p1.team_bench,p2.team_bench,colors)
    
    random_orden_turno = random.randint(0, 1)
    random_orden_turno = 0
    while not finish_game:
        #random_turno = 0 -> arriba (rojo), random_turno = 1 -> abajo (azul). Arriba siempre p1, abajo siempre p2
        if random_orden_turno == 0:
            print("Jugador rojo es su turno \n")
            doAction(table,p1,p2,random_orden_turno)
            utils.print_table(table,p1.team_bench,p2.team_bench,colors)
            print("Jugador azul es su turno \n")
            doAction(table,p2,p1,random_orden_turno + 1)
            utils.print_table(table,p1.team_bench,p2.team_bench,colors)
        else:
            doAction(table,p2,p1, random_orden_turno)
            doAction(table,p1,p2, random_orden_turno - 1)
        #utils.print_table(table,p1.team_bench,p2.team_bench)
        #finish_game = True
        
        

if __name__ == "__main__":
    start_game()