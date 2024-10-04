from termcolor import colored
import common_vars
from classes import Pokemon


def create_table() -> list:
    return [list([common_vars.fill_matrix_elem] * 5) for _ in range(5)]
    
def fill_str(name: str) -> str:
    len_name = len(name)
    diff_len = len(common_vars.fill_matrix_elem) - len_name
    if diff_len % 2 == 0:    
        name = ("*" * int(diff_len / 2)) + name + ("*" * int(diff_len / 2))
    else:
        name = ("*" * (int(diff_len / 2))) + name + ("*" * round((diff_len / 2)))
    return name

def format_row_to_print(row: list, colors: dict) -> list:
    return [colored(fill_str(elem.name),colors[elem.id_user]) if type(elem) == Pokemon else elem for elem in row]

def print_table(table: list, equipo1: list, equipo2: list, colors) -> str:
    space = int((124 - len(str(equipo1))) / 2)
    print((" "*space) + colored(str(equipo1),"red") + "\n")
    for index, row in enumerate(table):
        row = format_row_to_print(row,colors)
        if index == 0:
            print((" "*13) + "A" + (" "*24) + "B" + (" "*24) + "C" + (" "*24) + "D" + (" "*25) + "E")
            print((" "*63) + "|" + (" "*60))
            print('1  {:^4} -- {:^4} -- {:^4} -- {:^4} -- {:^4}'.format(*row))
            print((" "*13) + "|" + (" "*12) + "\\" + (" "*49) + "\\" + (" "*23) + "/" + (" "*13) + "|" + (" "*10))
        elif index == 1:
            print('2  {:^4}    {:^4} -- {:^4} -- {:^4}    {:^4}'.format(*row))
            print((" "*13) + "|" + (" "*24) + "|" + (" "*49) + "|" + (" "*25) + "|" + (" "*10))
        elif index == 2:
            print('3  {:^4}    {:^4}    {:^4}    {:^4}    {:^4}'.format(*row))
            print((" "*13) + "|" + (" "*24) + "|" + (" "*49) + "|" + (" "*25) + "|" + (" "*10))
        elif index == 3:
            print('4  {:^4}    {:^4} -- {:^4} -- {:^4}    {:^4}'.format(*row))
            print((" "*13) + "|" + (" "*11) + "/" + (" "*25) + "\\" + (" "*49) + "\\" + (" "*12) + "|" + (" "*10))
        else:
            print('5  {:^4} -- {:^4} -- {:^4} -- {:^4} -- {:^4}'.format(*row))
            print((" "*63) + "|" + (" "*60))
    print((" "*space) + colored(str(equipo2),"blue") + "\n")
