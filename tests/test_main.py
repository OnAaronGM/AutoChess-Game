import pytest
from actions import move_unidad, sacar_unidad
from utils import create_table
from classes import Player, Pokemon
from database import queries


@pytest.mark.parametrize(
    "input_x, input_y, input_z,input_y2, input_z2",
    [(create_table(), Player(id=1, team=[Pokemon(*unity) for unity in queries.select_team(1)]), 0,
      Player(id=2, team=[Pokemon(*unity) for unity in queries.select_team(2)]), 1)
        
    ]
)
def test_sacar_unidad(input_x,input_y, input_z, input_y2, input_z2):
    assert(sacar_unidad(input_x, input_y, input_z) == True)
    assert(sacar_unidad(input_x, input_y2, input_z2) == True)
    assert(sacar_unidad(input_x, input_y, input_z) == True)