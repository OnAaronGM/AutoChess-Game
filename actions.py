from utils import fill_str
import common_vars, utils, conditions
from player import Player

def calcular_opciones_mov(table: list, id_user: int, pos_ini):
    dict_poss_moves_from_ini = common_vars.possible_moves[pos_ini]
    moves = []
    ## Check all the possible moves from ini
    for key, value in dict_poss_moves_from_ini.items():
        ## Si posición nueva está ocupada por unidad rival, combate
        if type(table[key[0]][key[1]]) == list and table[key[0]][key[1]][1] != id_user:
            move = list(common_vars.positions.keys())[list(common_vars.positions.values()).index(key)]
            moves.append(move)
        else:
        ## Si posición libre, se ven los movimientos adyacentes.
            move = list(common_vars.positions.keys())[list(common_vars.positions.values()).index(key)]
            moves.append(move)
            for moves_2 in value:
                if type(table[moves_2[0]][moves_2[1]]) == str or \
                    (type(table[moves_2[0]][moves_2[1]]) == list and table[moves_2[0]][moves_2[1]][1] != id_user):
                    move = list(common_vars.positions.keys())[list(common_vars.positions.values()).index(moves_2)]
                    moves.append(move)
    return moves

def move_unidad(table: list, player: Player):
    ## PRINTEAR TODOS LAS UNIDADES QUE PUEDE MOVER
    position_ini_to_move = conditions.position_and_unity_valid(player.unity_on_game)
    
    ## Obtenemos la unidad a mover
    unidad = table[position_ini_to_move[0]][position_ini_to_move[1]]
    ## CALCULAR TODAS LAS POSIBLES OPCIONES DE MOVIMIENTO PARA EVITAR ERRORES
    moves = set(calcular_opciones_mov(table, player.id, position_ini_to_move))
    position_to_move = conditions.validate_move(moves)
    ## Una vez comprobado la posición final, hay que actualizar la tabla. Eliminar la posición inicial y \
        # update con nueva posición
        
    ### IMPORTANTE TODO: HAY QUE ANALIZAR SI HAY UNA UNIDAD RIVAL EN POSICION FINAL. EN CUYO CASO \
        # HAY QUE HACER LA LOGICA DE PELEA.
    
    table[position_ini_to_move[0]][position_ini_to_move[1]] = common_vars.fill_matrix_elem ## ELIMINAR
    table[position_to_move[0]][position_to_move[1]] = unidad                               ## UPDATE
    ## ELIMINAMOS DE LA LISTA DE UNIDADES EN JUEGO DEL USUARIO LA POSICIÓN VIEJA
    player.unity_on_game.remove(position_ini_to_move)
    ## UPDATE DE LA LISTA DE UNIDADES EN JUEGO DEL USUARIO CON LA POSICIÓN NUEVA
    player.unity_on_game.append(position_to_move)
    return True


def sacar_unidad(table: list, player: Player) -> list:
    position_ini = (0,2) if player.id == 0 else (4,2)
    ## Si existe una unidad en la posición de origen no se puede sacar otra hasta quedar libre.
    if type(table[position_ini[0]][position_ini[1]]) == list:
        print("Ya existe una unidad en la posición de inicio")
    else:
        print("Seleccione que unidad quiere sacer del banco")
        unidad = input()
        if unidad not in ["1","2","3","4","5","6"] or int(unidad) not in range(0,len(player.team_bench) + 1):
            print("No tiene una unidad en esa posición del banco")
        else:
            unidad = player.team_bench.pop(int(unidad) - 1)
            table[position_ini[0]][position_ini[1]] = [fill_str(unidad),player.id,100]
            player.unity_on_game.append((position_ini[0],position_ini[1]))
            return True
    return False