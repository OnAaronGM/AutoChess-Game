from termcolor import colored
import common_vars

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

def format_row_to_print(row: list) -> list:
    return [colored(elem[0],common_vars.colors[elem[1]]) if type(elem) == list else elem for elem in row]

def print_table(table: list, equipo1: list, equipo2: list) -> str:
    print(colored(str(equipo1),"red") + "\n")
    for index, row in enumerate(table):
        row = format_row_to_print(row)
        if index == 0:
            print((" "*60) + "|" + (" "*60))
            print('{:^4} -- {:^4} -- {:^4} -- {:^4} -- {:^4}'.format(*row))
            print((" "*10) + "|" + (" "*12) + "\\" + (" "*49) + "\\" + (" "*23) + "/" + (" "*13) + "|" + (" "*10))
        elif index == 1:
            print('{:^4}    {:^4} -- {:^4} -- {:^4}    {:^4}'.format(*row))
            print((" "*10) + "|" + (" "*24) + "|" + (" "*49) + "|" + (" "*25) + "|" + (" "*10))
        elif index == 2:
            print('{:^4}    {:^4}    {:^4}    {:^4}    {:^4}'.format(*row))
            print((" "*10) + "|" + (" "*24) + "|" + (" "*49) + "|" + (" "*25) + "|" + (" "*10))
        elif index == 3:
            print('{:^4}    {:^4} -- {:^4} -- {:^4}    {:^4}'.format(*row))
            print((" "*10) + "|" + (" "*11) + "/" + (" "*25) + "\\" + (" "*49) + "\\" + (" "*12) + "|" + (" "*10))
        else:
            print('{:^4} -- {:^4} -- {:^4} -- {:^4} -- {:^4}'.format(*row))
            print((" "*60) + "|" + (" "*60))
    print(colored(str(equipo2),"blue") + "\n")
