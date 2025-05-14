
import random



class pokemon:
    def __init__(self,hp,a1_name,a1_dam,a2_name,a2_dam,a3_name,a3_dam,type,weakness,trainer=None):
        self.hp = hp
        self.attack = {a1_name:a1_dam,a2_name:a2_dam,a3_name:a3_dam}
        self.type = type
        self.weakness = weakness
        self.trainer = trainer
       
Pikachu = pokemon(90,"quick attack",40,"iron tail",100,"thunderbolt",100,"electric",["ground"],"Ash")



Springatito = pokemon(90,"scratch", 10,"leafage",20,"trailblaze",50,"grass",["fire","ice","flying","poison","bug"],"Goh")



Glaceon = pokemon(110,"freeze-dry",70 ,"ice-fang",65,"quick-attack",40,"water",["fire","fighting","rock","steel"],"Rea")



Eevee = pokemon(90,"tackle",60,"covet",40,"bite",60,"normal",["fighting"],"Chloe")



Charmander= pokemon(90,"fire-spin",40,"false-swipe",40,"ember",40,"fire",["water","ground","rock"],"Leon")



Charmeleon= pokemon(100,"slash",70,"flamethrower",90,"firefang",65,"fire",["water","ground","rock"],"Leon")



Charizard = pokemon( 140,"flame-thrower",100,"heat-wave",85,"thunder-punch",75,"fire",["rock","electric","water"],"Leon")



Blastoise = pokemon(120,"hydro-crash",120,"water-pump",110,"shell-crack",70,"water",["grass","electric"],"Garry")


print("Welcome to the world coranation series where trainers from all over the world battle to raise their rankings")

what_name = input("What is your name ->")


pokedex={"charizard":Charizard,"pikachu":Pikachu,"springatito":Springatito,"glaceon":Glaceon,"eevee":Eevee,"charmander":Charmander,"charmeleon":Charmeleon,"blastoise":Blastoise,}
what_pokemon = input("what pokemon would you like to use? ->").lower()
opponent = random.choice(list(pokedex.keys()))
print(pokedex[opponent].trainer , "set out a", opponent, "a" , pokedex[opponent].type, "type," , opponent, "has" ,pokedex[opponent].hp , "hp")
print(what_pokemon)
count = 1





while pokedex[opponent].hp>0 and pokedex[what_pokemon].hp>0:


    for i in pokedex[what_pokemon].attack:
        print(f"{count}.) {i}:{pokedex[what_pokemon].attack[i]}")
        count=count+1

    attack_choice = int(input("what attack would you like to use? (choose 1-3) ->"))
    my_att = (list(pokedex[what_pokemon].attack)[attack_choice-1])
    if pokedex[what_pokemon].type in pokedex[opponent].weakness:
        my_dam = (pokedex[what_pokemon].attack)[my_att] *1.5
        
    else:
        my_dam = (pokedex[what_pokemon].attack)[my_att]
    print(what_pokemon,"used",my_att,"and dealt",pokedex[what_pokemon].attack[my_att],)
    pokedex[opponent].hp = pokedex[opponent].hp - my_dam
    print ("your opponent has",pokedex[opponent].hp,"hp")

    if pokedex[what_pokemon].type in pokedex[what_pokemon].weakness:
        my_dam = (pokedex[what_pokemon].attack)[my_att] *1.5
    else:
         my_dam = (pokedex[what_pokemon].attack)[my_att]



    if  pokedex[opponent].hp >0:
            attack_choice = random.randrange(1,3)
            opp_att = (list(pokedex[opponent].attack)[attack_choice-1])
            opp_dam = (pokedex[opponent].attack)[opp_att]
            print(opponent,"used",opp_att,"and dealt",opp_dam,"damage" )


         
            pokedex[what_pokemon].hp = pokedex[what_pokemon].hp - opp_dam
            print ("your pokemon has",pokedex[what_pokemon].hp,"hp")

    else:
        print(opponent,"fainted wich means that the win goes to", what_name)

    if  pokedex[what_pokemon].hp <=0:  
        

         print(what_pokemon,"fainted wich means that the win goes to", pokedex[opponent].trainer)
