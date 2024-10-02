import common_vars


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
    print("Indique el lugar de destino de la unidad selecciona")
    s = ""
    for move in moves:
        s += move + ", "
    print(s[:-2])
    position_to_move = input().upper()
    while position_to_move not in moves:
        print("Movimiento no válido")
        print("Indique el lugar de destino de la unidad selecciona")
        position_to_move = input().upper()
    return common_vars.positions[position_to_move]