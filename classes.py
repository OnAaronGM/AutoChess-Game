class Pokemon():
    def __init__(self, name, type_poke, mov1, power1, category1, type1, prob1, 
                mov2, power2, category2, type2, prob2, mov3, power3, category3, type3, prob3, id_user):
        self.name = name
        self.type_poke = type_poke
        self.movs = [mov1,mov2,mov3]
        self.powers = [power1,power2,power3]
        self.categories = [category1,category2,category3]
        self.types = [type1,type2,type3]
        self.probs = [prob1,prob2,prob3]
        self.id_user = id_user

class Player():
    def __init__(self, id, team):
        self.id = id
        self.team = team
        self.team_bench = [unity.name for unity in self.team]
        self.unity_on_game = []
