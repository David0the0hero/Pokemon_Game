import sqlite3
import random


# --- Setup SQLite Connection ---
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Create table if not exists (updated to store pokemon_name and level)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    pokemon_name TEXT,
    pokemon_level INTEGER,
    xp INTEGER
);
""")
connection.commit()

# --- Account Management ---
signup = False
ask_acc = input("Welcome Pokémon Trainer! Do you have an account? (y/n) -> ").lower()

while not signup:
    if ask_acc == "n":
        print("Let's create your account.")
        username = input("Username -> ")
        cursor.execute("SELECT username FROM users WHERE username = ?;", (username,))
        if cursor.fetchone() is None:
            password = input("Create a password -> ")
            # New user starts with a default Pokemon Pikachu at level 1, xp 0
            cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?);",
                           (username, password, "pikachu", 1, 1))  # Set level to 1 and xp to 0
            connection.commit()
            print("Account created! Time to begin your journey.")
            signup = True
        else:
            print("Username already exists.")
    else:
        username = input("Enter username -> ")
        cursor.execute("SELECT password FROM users WHERE username = ?;", (username,))
        record = cursor.fetchone()
        if record:
            password = input("Password -> ")
            if password == record[0]:
                print("Login successful.")
                signup = True
            else:
                print("Wrong password.")
        else:
            print("Username not found.")

# --- Pokémon Class ---
class Pokemon:
    def __init__(self, name, base_hp, attacks, types, weakness, trainer=None,
                 level=1, evolution=None):
        self.name = name
        self.level = level
        self.base_hp = base_hp
        self.max_hp = base_hp + (level * 5)
        self.hp = self.max_hp
        self.attacks = attacks
        self.types = types
        self.weakness = weakness
        self.trainer = trainer
        self.evolution = evolution

    def level_up(self):
        self.level += 1
        self.max_hp += 5
        self.hp = self.max_hp
        if self.evolution and self.level >= self.evolution[1]:
            self.evolve()

    def evolve(self):
        next_evo_name = self.evolution[0]
        print(f"\n🎉 Your {self.name} is evolving into {next_evo_name.title()}!")
        evo_pokemon = pokedex[next_evo_name]
        self.name = evo_pokemon.name
        self.base_hp = evo_pokemon.base_hp
        self.max_hp = self.base_hp + (self.level * 5)
        self.hp = self.max_hp
        self.attacks = evo_pokemon.attacks
        self.types = evo_pokemon.types
        self.weakness = evo_pokemon.weakness
        self.trainer = evo_pokemon.trainer
        self.evolution = evo_pokemon.evolution
        print(f"Your Pokémon evolved to {self.name}!")

# --- Pokémon Data: full list with base stats, moves, and evolutions ---
pokedex = {
    "pikachu": Pokemon(
        "Pikachu", 90,
        {"quick attack": 40, "iron tail": 100, "thunderbolt": 100},
        ["electric"], ["ground"], "Ash",
        evolution=("raichu", 16)
    ),
    "raichu": Pokemon(
        "Raichu", 120,
        {"quick attack": 50, "iron tail": 100, "thunderbolt": 120},
        ["electric"], ["ground"], "Ash",
        evolution=None
    ),
    "charmander": Pokemon(
        "Charmander", 90,
        {"ember": 40, "scratch": 40, "flamethrower": 90},
        ["fire"], ["water", "rock"], "Leon",
        evolution=("charmeleon", 16)
    ),
    "charmeleon": Pokemon(
        "Charmeleon", 110,
        {"ember": 50, "scratch": 50, "flamethrower": 100},
        ["fire"], ["water", "rock"], "Leon",
        evolution=("charizard", 36)
    ),
    "charizard": Pokemon(
        "Charizard", 150,
        {"flamethrower": 120, "wing attack": 80, "fire blast": 140},
        ["fire", "flying"], ["water", "rock", "electric"], "Leon",
        evolution=None
    ),
    "squirtle": Pokemon(
        "Squirtle", 90,
        {"water gun": 40, "aqua tail": 90, "hydro pump": 110},
        ["water"], ["grass", "electric"], "Garry",
        evolution=("wartortle", 16)
    ),
    "wartortle": Pokemon(
        "Wartortle", 110,
        {"water gun": 50, "aqua tail": 100, "hydro pump": 120},
        ["water"], ["grass", "electric"], "Garry",
        evolution=("blastoise", 36)
    ),
    "blastoise": Pokemon(
        "Blastoise", 150,
        {"hydro pump": 140, "aqua tail": 110, "shell smash": 0},
        ["water"], ["grass", "electric"], "Garry",
        evolution=None
    ),
    "eevee": Pokemon(
        "Eevee", 90,
        {"tackle": 60, "bite": 60, "covet": 40},
        ["normal"], ["fighting"], "Chloe",
        evolution=("vaporeon", 20)
    ),
    "vaporeon": Pokemon(
        "Vaporeon", 130,
        {"water gun": 60, "hydro pump": 130, "aqua ring": 0},
        ["water"], ["grass", "electric"], "Chloe",
        evolution=None
    ),
    "jolteon": Pokemon(
        "Jolteon", 110,
        {"thunderbolt": 100, "volt switch": 80, "shadow ball": 90},
        ["electric"], ["ground"], "Chloe",
        evolution=None
    ),
    "flareon": Pokemon(
        "Flareon", 130,
        {"fire blast": 120, "flamethrower": 100, "quick attack": 40},
        ["fire"], ["water", "rock"], "Chloe",
        evolution=None
    ),
    "espeon": Pokemon(
        "Espeon", 110,
        {"psychic": 90, "shadow ball": 80, "dazzling gleam": 80},
        ["psychic"], ["dark", "ghost"], "Chloe",
        evolution=None
    ),
    "umbreon": Pokemon(
        "Umbreon", 130,
        {"foul play": 80, "moonlight": 0, "toxic": 0},
        ["dark"], ["fighting", "bug"], "Chloe",
        evolution=None
    ),
    "leafeon": Pokemon(
        "Leafeon", 130,
        {"leaf blade": 90, "solar beam": 150, "synthesis": 0},
        ["grass"], ["fire", "ice", "poison"], "Chloe",
        evolution=None
    ),
    "glaceon": Pokemon(
        "Glaceon", 130,
        {"ice beam": 90, "blizzard": 120, "snow cloak": 0},
        ["ice"], ["fire", "steel", "rock"], "Chloe",
        evolution=None
    ),
    "sylveon": Pokemon(
        "Sylveon", 130,
        {"moonblast": 95, "hyper voice": 90, "calm mind": 0},
        ["fairy"], ["steel", "poison"], "Chloe",
        evolution=None
    ),
    "bulbasaur": Pokemon(
        "Bulbasaur", 90,
        {"vine-whip": 70, "poison-powder": 25, "seed-bomb": 90},
        ["grass"], ["fire" ,"ice"]
    )
}

# --- Level-based unlocks ---
level_unlocks = {
    1: ["bulbasaur", "charmander","squirtle"],
    3: ["pikachu","eevee"],
    5: ["leafeon","sylveon","glaceon","umbreon","espeon","flareon","jolteon","vaporeon"]
}

# --- Load Player Data (XP, Pokemon Name, Pokemon Level) ---
cursor.execute("SELECT xp, pokemon_name, pokemon_level FROM users WHERE username = ?;", (username,))
xp, poke_name, poke_level = cursor.fetchone()

# Force lowercase on poke_name to avoid mismatch
poke_name = poke_name.lower()
if poke_name not in pokedex:
    print(f"Error: Pokémon '{poke_name}' not found in pokedex. Defaulting to Pikachu.")
    poke_name = "pikachu"

base_pokemon = pokedex[poke_name]
player_pokemon = Pokemon(
    base_pokemon.name,
    base_pokemon.base_hp,
    base_pokemon.attacks,
    base_pokemon.types,
    base_pokemon.weakness,
    base_pokemon.trainer,
    level=poke_level,
    evolution=base_pokemon.evolution
)
player_pokemon.max_hp = player_pokemon.base_hp + (poke_level * 5)
player_pokemon.hp = player_pokemon.max_hp
quit_game = 'y'
while quit_game=='y':
    # --- Unlock Pokémon Based on XP ---
    available_pokemon = []
    for lvl_req, names in level_unlocks.items():
        if xp >= lvl_req:
            available_pokemon.extend(names)

    print("\n🎮 Welcome to the Pokémon League!\nAvailable Pokémon based on your XP:")
    for name in available_pokemon:
        print(f"- {name.title()}")

    # --- Choose Pokémon ---

    while True:
        choice = input("Which Pokémon would you like to use? -> ").lower()
        if choice in available_pokemon:
            base_poke = pokedex[choice]
            player_pokemon = Pokemon(
                base_poke.name,
                base_poke.base_hp,
                base_poke.attacks,
                base_poke.types,
                base_poke.weakness,
                base_poke.trainer,
                level=1,  # Start selected Pokémon at level 1
                evolution=base_poke.evolution
            )
            break
        print("Invalid choice or Pokémon not unlocked yet.")

    # --- Battle Setup ---
    opponent_name = random.choice(list(pokedex.keys()))
    opponent_pokemon = pokedex[opponent_name]
    print(f"\n⚔️ Battle Begins! {opponent_pokemon.trainer} sent out {opponent_name.title()}!")
    print(f"{opponent_name.title()} (Type: {opponent_pokemon.types}) has {opponent_pokemon.hp} HP.\n")

    # --- Battle Loop ---
    while player_pokemon.hp > 0 and opponent_pokemon.hp > 0:
        print("\nYour moves:")
        for idx, move in enumerate(player_pokemon.attacks):
            print(f"{idx+1}. {move.title()} ({player_pokemon.attacks[move]} dmg)")

        # Player Attack
        try:
            move_index = int(input("Choose your move (1-3) -> ")) - 1
            move_name = list(player_pokemon.attacks.keys())[move_index]
        except (ValueError, IndexError):
            print("Invalid choice.")
            continue

        move_dmg = player_pokemon.attacks[move_name]
        if any(t in opponent_pokemon.weakness for t in player_pokemon.types):
            move_dmg *= 1.2

        print(f"\n{player_pokemon.name} used {move_name.title()} and dealt {int(move_dmg)} damage!")
        opponent_pokemon.hp -= move_dmg
        opponent_pokemon.hp = max(opponent_pokemon.hp, 0)
        print(f"{opponent_pokemon.name} now has {int(opponent_pokemon.hp)} HP.")

        if opponent_pokemon.hp <= 0:
            print(f"\n✅ You defeated {opponent_pokemon.name}!")
            xp_gain = 2
            xp += xp_gain
            print(f"You gained {xp_gain} XP! Total XP: {xp}")
            temp_list = []
            # Level up player Pokémon for XP gain
            while xp >= player_pokemon.level * 5:
                player_pokemon.level_up()
                temp_list.append(f"{player_pokemon.name} leveled up to level {player_pokemon.level}!")
            print(temp_list[-1])
            # Update XP and Pokémon info in DB
            cursor.execute(
                "UPDATE users SET xp = ?, pokemon_name = ?, pokemon_level = ? WHERE username = ?;",
                (xp, player_pokemon.name.lower(), player_pokemon.level, username)
            )
            connection.commit()
            break

        # Opponent Attack
        opp_move = random.choice(list(opponent_pokemon.attacks.keys()))
        opp_dmg = opponent_pokemon.attacks[opp_move]
        print(f"\n{opponent_pokemon.name} used {opp_move.title()} and dealt {opp_dmg} damage!")
        player_pokemon.hp -= opp_dmg
        player_pokemon.hp = max(player_pokemon.hp, 0)
        print(f"{player_pokemon.name} has {int(player_pokemon.hp)} HP remaining.")

        if player_pokemon.hp <= 0:
            print(f"\n❌ {player_pokemon.name} fainted! You lost the battle.")
            break
    quit_game = input("Do you want to battle again? (y/n): ")
