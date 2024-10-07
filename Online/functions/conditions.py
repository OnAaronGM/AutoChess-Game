from functions import common_vars


def position_and_unity_valid(list_units: list):
    print("Indique que unidad quiere mover (formato ajedrez)")
    s = ""
    for unidad_game in list_units:
        s += list(common_vars.positions.keys())[list(common_vars.positions.values()).index(unidad_game)] + ", "
    print(s[:-2])
    position = input().upper()
    while common_vars.positions[position] not in list_units:
        print("No tienes ninguna unidad en esa posición")
        print("Indique que unidad quiere mover (formato ajedrez)")
        position = input().upper()
    return common_vars.positions[position]


def validate_move(moves: set):
    valid = False
    print("Indique el lugar de destino de la unidad selecciona")
    s = ""
    # Es necesario formatear la lista de movimientos para el usuario.
    # El formato debe ser -> 1: mov1, 2: mov2, etc
    for i, move in enumerate(moves):
        s += str(i+1) + ": " + move + ", "
    print(s[:-2])
    while not valid:
        position_to_move = input()
        try:
            position_to_move = int(position_to_move)
            valid = position_to_move in range(1,len(moves)+1)
            if not valid:
                print("Movimiento no válido")
                print("Indique el lugar de destino de la unidad selecciona")
        except ValueError:
            print("Movimiento no válido")
            print("Indique el lugar de destino de la unidad selecciona")
            continue
        
    return [common_vars.positions[elem] for elem in moves[position_to_move - 1].split(" -> ")]