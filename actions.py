from utils import fill_str
import common_vars, conditions
from classes import Player, Pokemon
import numpy as np


def calculate_dmg(pokemon_attacker_type: str, power_attk: int, type_attk:str, 
                  pokemon_defender_type: str, power_def: int, type_def: str):
    # Poder base del ataque. Si el tipo del ataque coincide con el tipo del poke -> *1.5. Comparar eficacias contra el tipo del otro poke
    power_attk *= common_vars.multiplicadores_df.loc[pokemon_attacker_type][pokemon_defender_type]
    power_def *= common_vars.multiplicadores_df.loc[pokemon_defender_type][pokemon_attacker_type]
    
    if type_attk == pokemon_attacker_type:
        power_attk = power_attk * 1.5
    if type_def == pokemon_defender_type:
        power_def = power_def * 1.5
        
    if power_attk > power_def:
        return "WIN"
    elif power_attk == power_def:
        return "Draw"
    return "LOSE"

def fight(pokemon_attacker: Pokemon, pokemon_defender: Pokemon):
    # Obtenemos movimiento de cada pokemon por probabilidad en base a sus probs
    pokemon_attacker_mov = np.random.choice(pokemon_attacker.movs,1,pokemon_attacker.probs)
    pokemon_defender_mov = np.random.choice(pokemon_defender.movs,1,pokemon_defender.probs)
    # Obtenemos el index en las listas correspondientes
    index_attk = pokemon_attacker.movs.index(pokemon_attacker_mov)
    index_def = pokemon_defender.movs.index(pokemon_defender_mov)
    # Si alguno de los 2 ataques es SPE, se acaba la pelea sin ganador.
    if pokemon_attacker.categories[index_attk] == "SPE" or pokemon_defender.categories[index_def] == "SPE":
        return "DRAW"
    # Si los 2 tienen prioridad, se calcula daño
    elif pokemon_attacker.categories[index_attk] == "PRI" and pokemon_defender.categories[index_def] == "PRI":
        # calcular daño
        resultado = calculate_dmg(pokemon_attacker.type_poke, pokemon_attacker.powers[index_attk], pokemon_attacker.types[index_attk], 
                        pokemon_defender.type_poke, pokemon_defender.powers[index_def], pokemon_defender.types[index_def])
        return resultado
    # Si atacante tiene prioridad y defensor no, gana atacante
    elif pokemon_attacker.categories[index_attk] == "PRI" and pokemon_defender.categories[index_def] == "ATK":
        return "WIN"
    # Si defensor tiene prioridad y atacante no, pierde atacante
    elif pokemon_attacker.categories[index_attk] == "ATK" and pokemon_defender.categories[index_def] == "PRI":
        return "LOSE"
    else:
    # Si los 2 tiene ataques normales, se calcula daño
        resultado = calculate_dmg(pokemon_attacker.type_poke, pokemon_attacker.powers[index_attk], pokemon_attacker.types[index_attk], 
                        pokemon_defender.type_poke, pokemon_defender.powers[index_def], pokemon_defender.types[index_def])
        return resultado

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