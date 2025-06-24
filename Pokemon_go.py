import sqlite3
import random


connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE users (username VARCHAR(255),password VARCHAR(255),pokemon VARCHAR(255), xp INT);")

signup=0
ask_acc = input("Do you have an account? (y/n)->")
while signup == 0:
    if ask_acc == "n":
        print("Hmm, looks like you don't have an account. Lets make you one. Follow the steps to make an account.")
        username = input("Step.1 Enter username->")
    
        cursor.execute("SELECT username FROM users;")
        all_users = cursor.fetchall()
        all_users1=[]
        for i in all_users:
            all_users1.append(i[0])
        print(all_users)
        if username not in all_users1:
            password = input("Step.2 Create your password ->")
            new_user = ("INSERT INTO users VALUES (?,?,?,?);")
            print("your all done with the acount setup, now enjoy yourself and climb the trainer rankings to become the best pokemon trainer you can be")
            cursor.execute(new_user, (username, password, "", 5))
            connection.commit()
            signup = 1
        else:
            print("Username already exists")
    else:
        print("Cool lets sign in to your account")
        username = input("What is your username ->")
        password = input("What is your password ->")




class pokemon:
    def __init__(self,hp,a1_name,a1_dam,a2_name,a2_dam,a3_name,a3_dam,type,weakness,trainer=None):
        self.hp = hp
        self.attack = {a1_name:a1_dam,a2_name:a2_dam,a3_name:a3_dam}
        self.type = type
        self.weakness = weakness
        self.trainer = trainer
       

# STARTER TYPE POKEMON


# ELECTRIC TYPE STARTER POKEMON AND EVOLUTIONS IN ORDER
Pikachu = pokemon(90,"quick attack",40,"iron tail",100,"thunderbolt",100,["electric"],["ground"],"Ash")


# LEAF TYPE STARTER POKEMON AND EVOLUTIONS IN ORDER
Springatito = pokemon(90,"scratch", 10,"leafage",20,"trailblaze",50,["grass"],["fire","ice","flying","poison","bug"],"Goh")


Bulbasaur = pokemon(80,"leech-seed",50,"razor leaf",70,"bite",50,["grass,poison"],["flying,psychic,ice,fire"],"milo")

# WATER TYPE STARTER POKEMON AND EVOLUTIONS IN ORDER
Squirtle = pokemon(90,"hydro-pump",110,"aqua-tail",90,"muddy-water",90,["water"],["electric","grass"],"Garry")


Wartortle = pokemon(100,"surf",90,"take-down",90,"water-pulse",65,["water"],["elecrtic","grass"],"Garry")


Blastoise = pokemon(120,"hydro-crash",120,"water-pump",110,"shell-crack",70,["water"],["grass","electric"],"Garry")

# FIRE TYPE STARTER POKEMON AND EVOLUTIONS IN ORDER
Fuecoco = pokemon(100,"incinerate",95,"tackle",70,"bite",50,["fire"],["water,ground,rock"],"kiwave")


Charmander= pokemon(90,"fire-spin",40,"false-swipe",40,"ember",40,["fire"],["water","ground","rock"],"Leon")


Charmeleon= pokemon(100,"slash",90,"flamethrower",90,"firefang",65,["fire"],["water","ground","rock"],"Leon")


Charizard = pokemon( 140,"flame-thrower",100,"heat-wave",85,"thunder-punch",75,["fire","flying"],["rock","electric","water"],"Leon")

# NORMAL TYPE STARTER POKEMON AND EVOLUTIONS 
Eevee = pokemon(90,"tackle",60,"covet",40,"bite",60,["normal"],["fighting"],"Chloe")


Glaceon = pokemon(110,"freeze-dry",70 ,"ice-fang",65,"quick-attack",40,["water"],["fire","fighting","rock","steel"],"Rea")


Umbreon = pokemon(120,"crunch",80,"dark-pulse",80,"swift",60,["dark"],["fighting","fairy","bug"],"Piers")


Flareon = pokemon(100,"flare-blitz",120,"temper flare",75,"ember",50,["fire"],["ground","rock","water"],"kiwave")

# LEVEL 3 WILD POKEMON AND EVOLUTIONS
Nicket = pokemon(80,"swift",50,"dark-pulse ",70,"bite",50,["dark"],["fighting,fairy,bug"],"piers")



# LEVEL 40 WILD POKEMON AND EVOLUTIONS
Riolu = pokemon(80,"Vacuum-Wave",40,"force-palm",60,"detect",0,["fighting"],["pyschic","fairy","flying"],"Ash")


Lucario = pokemon(130,"aura-sphere",80,"detect",0,"force palm",60,["fighting","steel"],["fighting","fire","ground"],"Ash")


Heracross = pokemon(130,"Mega-horn",120,"brick-break",75,"Aerial-ace",60,["bug","fighting"],["psychic","flying","fairy","fire"],"Goh")


Pinsir = pokemon(130,"x-scissor",80,"bug-bite",60,"stone edge",100,["bug"],["rock","fire","flying"],"Goh")


Gyrados = pokemon(130,"ice-fang",90,"hyper-beam",110,"aqua-tail",90,["water","flying"],["fighting","grass","bug"],"lance")








# FORBIDDEN POKEMON
Arceus  = pokemon(140,"hyper-beam",150,"judgment",100,"future-sight",120,["normal"],["fighting"],"better then the best, I am the best of the best")


Dialga = pokemon(140,"roars-of-time",150,"dragon-claw",80,"draco-meteor",120,["steel","dragon"],["fighting","ground"],"")


Palkia = pokemon(140,"hydro-pump",110,"hyper-beam",150,"draco-meteor",120,["water","dragon"],["dragon","fairy"])


print("Welcome to the world coranation series where trainers from all over the world battle to raise their rankings")

what_name = input("Welcome trainer what is your name ->")

y = 1
pokemon_levels = {1:[Charmander,Squirtle,Pikachu],3:[Springatito,Eevee],6:[]}
pokedex = {"charizard":Charizard,"pikachu":Pikachu,"springatito":Springatito,"glaceon":Glaceon,"eevee":Eevee,"charmander":Charmander,"charmeleon":Charmeleon,"blastoise":Blastoise,"lucario":Lucario,"riolu":Riolu,"umbreon":Umbreon,"flareon":Flareon,"heracross":Heracross,"pinsir":Pinsir,"squirtle":Squirtle,"gryados":Gyrados,"nicket":Nicket,"bulbasaur":Bulbasaur,"fuecoco":Fuecoco,"wartortle":Wartortle}
while y == 0: 
    for i in pokedex:
        print(i,"a",pokedex[i].type,"type pokemon")

    what_pokemon = input("what pokemon would you like to use? Your options are listed above ->").lower()
    if what_pokemon == "Arceus" or what_pokemon == "Dialga" or what_pokemon == "Palkia":
        x = Arceus,Dialga,Palkia
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
        my_dam = (pokedex[what_pokemon].attack)[my_att] *1.2
        
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
        my_dam = (pokedex[what_pokemon].attack)[my_att] *1.2
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
