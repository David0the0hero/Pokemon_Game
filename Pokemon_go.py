
import random



class pokemon:
    def __init__(self,hp,a1_name,a1_dam,a2_name,a2_dam,a3_name,a3_dam,type,weakness,trainer=None):
        self.hp = hp
        self.attack = {a1_name:a1_dam,a2_name:a2_dam,a3_name:a3_dam}
        self.type = type
        self.weakness = weakness
        self.trainer = trainer
       
Pikachu = pokemon(90,"quick attack",40,"iron tail",100,"thunderbolt",100,["electric"],["ground"],"Ash")



Springatito = pokemon(90,"scratch", 10,"leafage",20,"trailblaze",50,["grass"],["fire","ice","flying","poison","bug"],"Goh")



Glaceon = pokemon(110,"freeze-dry",70 ,"ice-fang",65,"quick-attack",40,["water"],["fire","fighting","rock","steel"],"Rea")



Eevee = pokemon(90,"tackle",60,"covet",40,"bite",60,["normal"],["fighting"],"Chloe")



Charmander= pokemon(90,"fire-spin",40,"false-swipe",40,"ember",40,["fire"],["water","ground","rock"],"Leon")



Charmeleon= pokemon(100,"slash",70,"flamethrower",90,"firefang",65,["fire"],["water","ground","rock"],"Leon")



Charizard = pokemon( 140,"flame-thrower",100,"heat-wave",85,"thunder-punch",75,["fire","flying"],["rock","electric","water"],"Leon")



Blastoise = pokemon(120,"hydro-crash",120,"water-pump",110,"shell-crack",70,["water"],["grass","electric"],"Garry")



Lucario = pokemon(130,"aura-sphere",80,"detect",0,"force palm",60,["fighting","steel"],["fighting","fire","ground"],"Ash")



Riolu = pokemon(80,"Vacuum-Wave",40,"force-palm",60,"detect",0,["fighting"],["pyschic","fairy","flying"],"Ash")



Umbreon = pokemon(120,"crunch",80,"dark-pulse",80,"swift",60,["dark"],["fighting","fairy","bug"],"Piers")



Flareon = pokemon(100,"flare-blitz",120,"temper flare",75,"ember",50,["fire"],["ground","rock","water"],"kiwave")



Heracross = pokemon(130,"Mega-horn",120,"brick-break",75,"Aerial-ace",60,["bug","fighting"],["psychic","flying","fairy","fire"],"Goh")



Pinsir = pokemon(130,"x-scissor",80,"bug-bite",60,"stone edge",100,["bug"],["rock","fire","flying"],"Goh")



Arceus  = pokemon(140,"hyper-beam",150,"judgment",100,"future-sight",120,["normal"],["fighting"],"better then the best, I am the best of the best")



dialga = pokemon,140,"",,"",,"",,["fighting"],["ground"],"")





print("Welcome to the world coranation series where trainers from all over the world battle to raise their rankings")

what_name = input("Welcome trainer what is your name ->")

y = 0
pokedex = {"charizard":Charizard,"pikachu":Pikachu,"springatito":Springatito,"glaceon":Glaceon,"eevee":Eevee,"charmander":Charmander,"charmeleon":Charmeleon,"blastoise":Blastoise,"lucario":Lucario,"riolu":Riolu,"umbreon":Umbreon,"flareon":Flareon,"heracross":Heracross,"pinsir":Pinsir}
while y == 0: 
    for i in pokedex:
        print(i,"a",pokedex[i].type,"type pokemon")

    what_pokemon = input("what pokemon would you like to use? Your options are listed above ->").lower()
    if what_pokemon == Arceus:
        x = Arceus
    count = 1

    try:
         x=pokedex[what_pokemon]
         y=1
    except KeyError:
         print(what_pokemon,"doesn't exist")


opponent = random.choice(list(pokedex.keys()))
print(pokedex[opponent].trainer , "set out a", opponent, "a" , pokedex[opponent].type, "type," , opponent, "has" ,pokedex[opponent].hp , "hp")
print(what_pokemon,"has the moves")


while pokedex[opponent].hp>0 and pokedex[what_pokemon].hp>0:


    for i in pokedex[what_pokemon].attack:
        print(f"{count}.) {i}:{pokedex[what_pokemon].attack[i]}")
        count=count+1

    attack_choice = int(input("what attack would you like to use? (choose 1-3) ->"))
    while attack_choice <1 or attack_choice>3:
        print("that is no one of",what_pokemon+"'s attacks")
        attack_choice = int(input("what attack would you like to use? (choose 1-3) ->"))

    my_att = (list(pokedex[what_pokemon].attack)[attack_choice-1])
    if pokedex[what_pokemon].type in pokedex[opponent].weakness:
        my_dam = (pokedex[what_pokemon].attack)[my_att] *1.5
        
    else:
        my_dam = (pokedex[what_pokemon].attack)[my_att]
    if my_att != "detect":
        print(what_pokemon,"used",my_att,"and dealt",pokedex[what_pokemon].attack[my_att],)
    else:
        print(what_pokemon,"used detect")
        print(what_pokemon,"is now protected")
    pokedex[opponent].hp = pokedex[opponent].hp - my_dam
    print ("your opponent has",pokedex[opponent].hp,"hp")

    if pokedex[what_pokemon].type in pokedex[what_pokemon].weakness:
        my_dam = (pokedex[what_pokemon].attack)[my_att] *1.5
    else:
         my_dam = (pokedex[what_pokemon].attack)[my_att]


    if my_att != "detect":
        if  pokedex[opponent].hp >0:
                attack_choice = random.randrange(1,3)
                opp_att = (list(pokedex[opponent].attack)[attack_choice-1])
                opp_dam = (pokedex[opponent].attack)[opp_att]
                print(opponent,"used",opp_att,"and dealt",opp_dam,"damage" )


         
                pokedex[what_pokemon].hp = pokedex[what_pokemon].hp - opp_dam
                print ("your pokemon has",pokedex[what_pokemon].hp,"hp")

        else:
            print(opponent,"fainted wich means that the win goes to", what_name)
    else:
        print(what_pokemon,"used detect.",opponent,"did 0 damage")
    if  pokedex[what_pokemon].hp <=0:  
            

        print(what_pokemon,"fainted wich means that the win goes to", pokedex[opponent].trainer)
    count=1
