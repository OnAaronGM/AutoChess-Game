import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ratillas97",
  database="autochesspoke"
)

def insert_pokemon():
    pokemon = input("Ingrese nombre del pokemon\n")
    tipo = input("Ingrese tipo del pokemon\n")
    mov1 = input("Ingrese movimiento1 del pokemon\n")
    prob1 = input("Ingrese prob1 del pokemon\n")
    mov2 = input("Ingrese movimiento2 del pokemon\n")
    prob2 = input("Ingrese prob2 del pokemon\n")
    mov3 = input("Ingrese movimiento3 del pokemon\n")
    prob3 = input("Ingrese prob3 del pokemon\n")
    
    query = """insert into autochesspoke.pokemon (name, type, move1, prob1, move2, prob2, move3, prob3) 
    values ('{}','{}',(select idmovements from movements where name = '{}'),{}, 
    (select idmovements from movements where name = '{}'),{},(select idmovements from movements where name = '{}'),
    {});""".format(pokemon,tipo,mov1,prob1,mov2,prob2,mov3,prob3)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    
def insert_pokemon_in_profile(id_user: int, name_pokemon: str):
    query = """insert into autochesspoke.pokemon_own (id_user, id_pokemon) 
    values ({},(select id from pokemon where name = '{}'));""".format(id_user,name_pokemon)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    
def select_team(id_user: int):
    query = """select pokemon.name, pokemon.type, mov1.name as mov1, mov1.power as power1, mov1.category,
    mov1.type, prob1, mov2.name as mov2, mov2.power as power2, mov2.category, mov2.type, prob2,
    mov3.name as mov3, mov3.power as power3, mov3.category, mov3.type, prob3 
    from pokemon inner join movements mov1 on mov1.idmovements = pokemon.move1 
    inner join movements mov2 on mov2.idmovements = pokemon.move2 
    left join movements mov3 on mov3.idmovements = pokemon.move3 
    where pokemon.id in (select id_pokemon from pokemon_own where id_user={});""".format(id_user)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult
    
if __name__ == "__main__":
    #insert_pokemon()
    #insert_pokemon_in_profile()
    select_team(1)