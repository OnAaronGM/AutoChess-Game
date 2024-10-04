import pandas as pd

#colors = {0:"red",1:"blue"}
positions = {"A1":(0,0),"A2":(1,0),"A3":(2,0),"A4":(3,0),"A5":(4,0),
             "B1":(0,1),"B2":(1,1),"B3":(2,1),"B4":(3,1),"B5":(4,1),
             "C1":(0,2),"C2":(1,2),"C3":(2,2),"C4":(3,2),"C5":(4,2),
             "D1":(0,3),"D2":(1,3),"D3":(2,3),"D4":(3,3),"D5":(4,3),
             "E1":(0,4),"E2":(1,4),"E3":(2,4),"E4":(3,4),"E5":(4,4)}

possible_moves = {(0,0):{(0,1):[(0,2)],(1,0):[(2,0)],(1,1):[(2,1),(1,2)]},
                  (0,1):{(0,0):[(1,0),(1,1)],(0,2):[(0,3),(1,3)]},
                  (0,2):{(0,1):[(0,0)],(0,3):[(0,4)],(1,3):[(0,4),(2,3),(1,2)]},
                  (0,3):{(0,4):[(1,4),(1,3)],(0,2):[(0,1),(1,3)]},
                  (0,4):{(0,3):[(0,2)],(1,4):[(2,4)],(1,3):[(0,2),(1,2),(2,3)]},
                  (1,0):{(0,0):[(0,1),(1,1)],(2,0):[3,0]},
                  (1,1):{(0,0):[(1,0),(0,1)],(2,1):[(3,1)],(1,2):[(1,3)]},
                  (1,2):{(1,1):[(0,0),(2,1)],(1,3):[(0,2),(0,4),(2,3)]},
                  (1,3):{(1,2):[(1,1)],(2,3):[(3,3)],(0,2):[(0,1),(0,3)],(0,4):[(0,3),(1,4)]},
                  (1,4):{(2,4):[(3,4)],(0,4):[(0,3),(1,3)]},
                  (2,0):{(1,0):[(0,0)],(3,0):[(4,0)]},
                  (2,1):{(1,1):[(0,0),(1,2)],(3,1):[(3,2),(4,0),(4,2)]},
                  (2,3):{(1,3):[(1,2),(0,2),(0,4)],(3,3):[(3,2),(4,4)]},
                  (2,4):{(1,4):[(0,4)],(3,4):[(4,4)]},
                  (3,0):{(2,0):[(1,0)],(4,0):[(3,1),(4,1)]},
                  (3,1):{(2,1):[(1,1)],(3,2):[(3,3)],(4,0):[(3,0),(4,1)],(4,2):[(4,1),(4,3)]},
                  (3,2):{(3,1):[(2,1),(4,0),(4,2)],(3,3):[(2,3),(4,4)]},
                  (3,3):{(2,3):[(1,3)],(3,2):[(3,1)],(4,4):[(3,4),(4,3)]},
                  (3,4):{(2,4):[(1,4)],(4,4):[(3,3),(4,3)]},
                  (4,0):{(3,0):[(2,0)],(3,1):[(2,1),(3,2),(4,2)],(4,1):[(4,2)]},
                  (4,1):{(4,0):[(3,0),(3,1)],(4,2):[(3,1),(4,3)]},
                  (4,2):{(4,1):[(4,0)],(4,3):[(4,4)],(3,1):[(4,0),(2,1),(3,2)]},
                  (4,3):{(4,2):[(3,1),(4,1)],(4,4):[(3,4),(3,3)]},
                  (4,4):{(3,4):[(2,4)],(3,3):[(2,3),(3,2)],(4,3):[(4,2)]}
}


types_poke = ["acero","agua","bicho","dragón","eléctrico","fantasma","fuego","hada","hielo",
                           "lucha","normal","planta","psiquico","roca","siniestro","tierra","veneno","volador"]


multiplicadores = [[0.5,0.5,1,1,0.5,1,0.5,2,2,1,1,1,1,2,1,1,1,1],
     [1,0.5,1,0.5,1,1,2,1,1,1,1,0.5,1,2,1,2,1,1],
     [0.5,1,1,1,1,0.5,0.5,0.5,1,0.5,1,2,2,1,2,1,0.5,0.5],
     [0.5,1,1,2,1,1,1,0.25,1,1,1,1,1,1,1,1,1,1],
     [1,2,1,0.5,0.5,1,1,1,1,1,1,0.5,1,1,1,0.25,1,2],
     [1,1,1,1,1,2,1,1,1,1,0.25,1,2,1,0.5,1,1,1],
     [2,0.5,2,0.5,1,1,0.5,1,2,1,1,2,1,0.5,1,1,1,1],
     [0.5,1,1,2,1,1,0.5,1,1,2,1,1,1,1,2,1,0.5,1],
     [0.5,0.5,1,2,1,1,0.5,1,0.5,1,1,2,1,1,1,2,1,2],
     [2,1,0.5,1,1,0.25,1,0.5,2,1,2,1,0.5,2,2,1,0.5,0.5],
     [0.5,1,1,1,1,0.25,1,1,1,1,1,1,1,0.5,1,1,1,1],
     [0.5,2,0.5,0.5,1,1,0.5,1,1,1,1,0.5,1,2,1,2,0.5,0.5],
     [0.5,1,1,1,1,1,1,1,1,2,1,1,0.5,1,0.25,1,2,1],
     [0.5,1,2,1,1,1,2,1,2,0.5,1,1,1,1,1,0.5,1,2],
     [1,1,1,1,1,2,1,0.5,1,0.5,1,1,2,1,0.5,1,1,1],
     [2,1,0.5,1,2,1,2,1,1,1,1,0.5,1,2,1,1,2,0.25],
     [0.25,1,1,1,1,0.5,1,2,1,1,1,2,1,0.5,1,0.5,0.5,1],
     [0.5,1,2,1,0.5,1,1,1,1,2,1,2,1,0.5,1,1,1,1]
     ]

multiplicadores_df = pd.DataFrame(multiplicadores,columns=types_poke).set_index([types_poke])


fill_matrix_elem = "*" * 21
bar = '----------------------'