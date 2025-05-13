import random




class pokemon:
    def __init__(self,hp,a1_name,a1_dam,a2_name,a2_dam,a3_name,a3_dam,type,weakness):
        self.hp = hp
        self.attack = {a1_name:a1_dam,a2_name:a2_dam,a3_name:a3_dam}
        self.type = type
        self.weakness = weakness
       
Pikachu = pokemon(90,"quick attack",40,"iron tail",100,"thunderbolt",100,"electric",["ground"])




Springatito = pokemon(90,"scratch", 10,"leafage",20,"trailblaze",50,"grass",["fire","ice","flying","poison","bug"])




Glaceon= pokemon(110,"freeze-dry",70 ,"ice-fang",65,"quick-attack",40,"water",["fire","fighting","rock","steel"])




Eevee = pokemon(90,"tackle",60,"covet",40,"bite",60,"normal",["fighting"])




Charmander= pokemon(90,"fire-spin",40,"false-swipe",40,"ember",40,"fire",["water","ground","rock"])




Charmeleon= pokemon(100,"slash",70,"flamethrower",90,"firefang",65,"fire",["water","ground","rock"])






blastoise = pokemon(140,"hydro_crash",120,"water_pump",110,"shell_crack",70,"water",["grass","electric"])





Charizard = pokemon( 140,"flame-thrower",100,"heat-wave",85,"thunder-punch",75,"fire",["rock","electric","water"])
pokedex = {"Pikachu":Pikachu,"Springatito":Springatito,"Glaceon":Glaceon,"Eevee":Eevee,"Charmander":Charmander,"Charmeleon":Charmeleon,"Blastoise":blastoise,"Charizard":Charizard,}
what_pokemon = input("what pokemon would you like to use? ->")
opponent = random.choice(list(pokedex.keys()))
print("Your opponent is", opponent, ":", pokedex[opponent].type,":",pokedex[opponent].hp)
print(what_pokemon)
count = 1
for i in pokedex[what_pokemon].attack:
    print(f"{count}.) {i}:{pokedex[what_pokemon].attack[i]}")
    count=count+1


while pokedex[opponent].hp>0 and pokedex[what_pokemon].hp>0:






    attack_choice = int(input("what attack would you like to use? (choose 1-3) ->"))
    my_att = (list(pokedex[what_pokemon].attack)[attack_choice-1])
    if pokedex[what_pokemon].type in pokedex[opponent].weakness:

        my_dam = (pokedex[what_pokemon].attack)[my_att] *2
    else:
        my_dam = (pokedex[what_pokemon].attack)[my_att]
    pokedex[opponent].hp = pokedex[opponent].hp - my_dam
    print ("your opponent has",pokedex[opponent].hp,"hp")
    if pokedex[what_pokemon].type in pokedex[what_pokemon].weakness:






        if pokedex[opponent].hp >0:
            attack_choice = random.randrange(1,3)
            opp_att = (list(pokedex[opponent].attack)[attack_choice-1])
            opp_dam = (pokedex[opponent].attack)[opp_att]
            print("Your opponent used",opp_att,"and dealt",opp_dam,"damage" )


         
            pokedex[what_pokemon].hp = pokedex[what_pokemon].hp - opp_dam
            print ("your pokemon has",pokedex[what_pokemon].hp,"hp")
