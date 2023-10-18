
#<Made By James mills>
import cmd, textwrap, sys, os, time, random
import mapsRPG
import dialogue_mod


screen_width = 100

settings_color = "0"
gameOver = False

#### Player setup ####
class player:
    def __init__(self):
        self.name = ""
        self.job = ""
        self.hp = 0
        self.Ip = 0 # Inteligence
        self.location = 'Inn'
        self.status_effects = []
        self.inv = [""]
        self.equiped = [] # There will only be two lots
        self.money_cp = 150
        self.money_sp = 30
        self.money_gp = 7
        self.ac = 10 # Armor class
        self.quest = [""]

class weapons(): # the way this works is how may times a dice is rowled
    def __init__(self):
        self.dagger = 1  # Damage: 1d6
        self.pike = 3    # Damage: 3d6
        self.bow = 2     # Damage: 2d6
        self.longsword = 4  # Damage: 4d6
        self.mace = 2    # Damage: 2d6
        self.rapier = 4  # Damage: 4d6
        self.staff = 2   # Damage: 2d6
        self.axe = 3     # Damage: 3d6
        self.hammer = 2  # Damage: 2d6
        self.spear = 2   # Damage: 2d6
    
    def get_damage(self, weapon):
        if weapon.lower() == 'dagger':
            return self.dagger
        elif weapon.lower() == 'pike':
            return self.pike
        elif weapon.lower() == 'bow':
            return self.bow
        elif weapon.lower() == 'longsword':
            return self.longsword
        elif weapon.lower() == 'mace':
            return self.mace
        elif weapon.lower() == 'rapier':
            return self.rapier
        elif weapon.lower() == 'staff':
            return self.staff
        elif weapon.lower() == 'axe':
            return self.axe
        elif weapon.lower() == 'hammer':
            return self.hammer
        elif weapon.lower() == 'spear':
            return self.spear
        else:
            print("error")


weapons_ = weapons()
myPlayer = player()
##### title Scrren ####

def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("settings"):
        settings_menu()
    elif option.lower() == ("quit"):
        sys.exit()
        ### settings ###

    elif option.lower() == ("color"):

            print("")
            print("""    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White""")
            settings_color = str(input("Number?> "))
            os.system(f'color {settings_color}')
    while option.lower() not in ["play", "help", "quit"]: # mean the player cant accsidently quit if wrong imput.
        print("Error enter a valid comand.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("settings"):
            settings_menu()
        elif option.lower() == ("quit"):
            sys.exit()
        ### settings ###

        elif option.lower() == ("color"):
            print("")
            print("""    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White""")
            settings_color = input("Number?> ")
            os.system(f'color {settings_color}')
            title_screen_selection()

def title_screen():
    os.system('cls')

    print("+—————————————————————————————————————+")
    print("| welcome to Plaguepunk the Text RPG! |")
    print("+—————————————————————————————————————+")
    print("             #   Play   #              ")
    print("             #   Help   #              ")
    print("             # settings #              ")
    print("             #   Quit   #              ")
    print(" (WIP) - Made by James :).")
    title_screen_selection()

def help_menu():
    os.system('cls')
    print("+—————————————————————————————————————+")
    print("| welcome to Plaguepunk the Text RPG! |")
    print("+—————————————————————————————————————+")
    print("# Use up, down, left, right to move")
    print("# Type your commands to do them")
    print("# Use 'look' to inspect somthing ")
    print("# Good look!")
    print("#Is there is a * befor a diolog option it is a integrel question.")
    title_screen_selection()

def settings_menu():
    os.system('cls')
    print("+—————————————————————————————————————+")
    print("| welcome to Plaguepunk the Text RPG! |")
    print("+—————————————————————————————————————+")
    print("             #   color   #         ")
    print("             # Difficulty #        ")
    title_screen_selection()



#### MAP VARS ####

ZONENAME = ""
DESCRIPTION = "Description"
EXAMINATION = "examine"
EXPLORED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"
explored_place = {"T": False, "H": False, "?": False,
                    "P": False, "C": False, "M": False,
                    "Shop": False, "Inn": False, "Moun": False,
                    }


zone_map = {
    "TC": {
        ZONENAME: "Tesla City",
        DESCRIPTION: "(Central city of the realm, advanced in steam technology)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "TC",
        DOWN: "FH",
        LEFT:"TC",
        RIGHT: "MW",
        },
    "RR": {
        ZONENAME: "Rusty Ruins",
        DESCRIPTION: "(Remnants of an ancient steampunk civilization)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "RR",
        DOWN: "SS",
        LEFT:"SW",
        RIGHT: "RR",
        },
    "FH": {
        ZONENAME: "Foggy Harbor",
        DESCRIPTION: "(A harbor area with perpetual mist and steam)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "TC",
        DOWN: "HH",
        LEFT:"FH",
        RIGHT: "MW",
        },
    "MW": {
        ZONENAME: "Misty Woods",
        DESCRIPTION: "(A forest covered in mist with mysterious creatures)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "MW",
        DOWN: "T",
        LEFT:"FH",
        RIGHT: "SW",
        },
    "SW": {
        ZONENAME: "Steam Works",
        DESCRIPTION: "(Industrial area with factories and steam-powered machines)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "RR",
        DOWN: "MH",
        LEFT:"MW",
        RIGHT: "SS",
        },
    "SS": {
        ZONENAME: "Skyport Station",
        DESCRIPTION: "(A station for airships to dock and refuel)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "RR",
        DOWN: "PD",
        LEFT:"SW",
        RIGHT: "SS",
        },
    "HH": {
        ZONENAME: "Hydraulic Haven",
        DESCRIPTION: "(A secluded area with hydraulic-powered mechanisms)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "SW",
        DOWN: "T",
        LEFT:"HH",
        RIGHT: "MH",
        },
    "PD": {
        ZONENAME: "Pulling Distinct",
        DESCRIPTION: "(An area with massive steam pumps regulating the realm's steam supply)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "SS",
        DOWN: "T2",
        LEFT:"MH",
        RIGHT: "PD",
        },
    "LS": {
        ZONENAME: "Lakeside Settlement",
        DESCRIPTION: "(A small settlement by the lakeside)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "T",
        DOWN: "Ls",
        LEFT:"LS",
        RIGHT: "LS",
        },
    "BM": {
        ZONENAME: "Blacksmith's Market",
        DESCRIPTION: "(A bustling market specializing in steampunk metalworks)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "T",
        DOWN: "BM",
        LEFT:"BM",
        RIGHT: "LC",
        },
    "LC": {
        ZONENAME: "Library Courtyard",
        DESCRIPTION: "(A serene courtyard outside the kingdom's grand library)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "T",
        DOWN: "LC",
        LEFT:"BM",
        RIGHT: "LC",
        },
    "WP": {
        ZONENAME: "Windmill Plaza",
        DESCRIPTION: "(A plaza with large windmills harnessing wind energy)",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "T2",
        DOWN: "WP",
        LEFT:"WP",
        RIGHT: "IC",
        },
    "IC": {
        ZONENAME: "Ironclad Tower",
        DESCRIPTION: "(A towering structure made of iron, housing advanced steam-powered technology))",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "T2",
        DOWN: "IC",
        LEFT:"WP",
        RIGHT: "WP",
        },
    "T": {
        ZONENAME: "Ironclad Tower",
        DESCRIPTION: "(A towering structure made of iron, housing advanced steam-powered technology))",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "T2",
        DOWN: "IC",
        LEFT:"WP",
        RIGHT: "WP",
        },
    "T2": {
        ZONENAME: "Turning in the road ",
        DESCRIPTION: "(A towering structure made of iron, housing advanced steam-powered technology))",
        EXAMINATION: "examine",
        EXPLORED: False,
        UP: "T2",
        DOWN: "IC",
        LEFT:"WP",
        RIGHT: "WP",
        },
    }
#### Game Interactivity ####
def inventory():
    print("You open up your bag and you see...")
    for item in myPlayer.inv:
        print(item)
    print(f"\nYou open up your purse and see {myPlayer.money_gp} gold pieces, {myPlayer.money_sp} silver pieces and {myPlayer.money_cp} copper pieces.")
    print(f"\nYou have in equipped items, {myPlayer.equiped}")
    swapInput = str(input("\nWould you like to swap(or add) your equipped items y/n?: "))
    if swapInput == "y":
        swapequiped()

def print_location():
    print("\n" + ("—" * (4+ len(myPlayer.location))))
    print(f"- {zone_map [myPlayer.location] [ZONENAME]} #")
    print(f"- {zone_map [myPlayer.location] [DESCRIPTION]} #")
    print("\n" + ("—" * (4+ len(myPlayer.location))))

def quests():
    print("========================")
    print(myPlayer.quest)
def prompt():
    print(f"\n=================================")
    print("What would you like to do")
    action = input("> ")
    acceptable_actions = ["use","inv","inventory","move", "go", "travle", "walk", "quit", "examine", "inspect", "look", "map", "look at map", "speek", "talk", "speek to someone", "quests"]
    while action.lower() not in acceptable_actions:
        print("Error Unknown action.\n")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travle", "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "look"]:
        player_examine(action.lower)
    elif action.lower() in ["map", "look at map"]:
        MAP_look()
    elif action.lower() in ["talk", "speek to someone", "speek"]:
        dialogue(action)
    elif action.lower() in ["inv", "inventory"]:
        inventory()
    elif action.lower() in ["use"]:
        use_Item()
def player_move(myAction):
    dest = input("Were would you like to move to?\n>")
    if dest in ["up", "north"]:
        destination = zone_map[myPlayer.location][UP]
        movement_handeler(destination)
    elif dest in ["left", "west"]:
        destination = zone_map[myPlayer.location][LEFT]
        movement_handeler(destination)
    elif dest in ["east", "right"]:
        destination = zone_map[myPlayer.location][RIGHT]
        movement_handeler(destination)
    elif dest in ["down", "south"]:
        destination = zone_map[myPlayer.location][DOWN]
        movement_handeler(destination)


def movement_handeler(destination):
    print(f"\nYou have moved to the {destination}.")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zone_map[myPlayer.location][EXPLORED] == True:
        print("You have explored this location.")
    else:
        if zone_map[myPlayer.location][ZONENAME] == "The Drunken Inn (Inn/home)":
            print()

        if zone_map[myPlayer.location][ZONENAME] == "shop":
            print()
def diologue_style(name_0):
    print("\n")
    print("*" * (len(name_0)))
    print("*   "+name_0+"  *")
    print("*"* (len(name_0)))

def dialogue(action):
    ###############—-—INN—-—###############


    if zone_map[myPlayer.location][ZONENAME] == "The Drunken Inn (Inn/home)":
        dialogue_ans = input("There are a few people in the inn it is quiet. people:\n The bar maid(1)\n The stranger(2)\n The knight(3)\n The inn keep(4)\n The drunk(5)\nPick a number to speek to.> ")
        if dialogue_ans == "1":
            name_0 = "The Bar maid"
            
            print("\n")
            valid_questions = ["*What is this place? (1)", "Is there anything i can do?(2)", "What do you have for sale?(3)"]
            diologue_style(name_0)
            bm_speach = "The bar maid: Hi what can i get startd for you, love?\nIf you've any quearys love don't hesitate to ask?"

            print("\n")
            for character in bm_speach:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)


            print("\n\nQuestions to ask:")
            for i in range(3):
                print(valid_questions[i])
            print("\n")
            questions = input("> ")
            if questions == "1":
                dialogue_mod.Barmaid_d1()

            elif questions == "2":
                dialogue_mod.Barmaid_d2(myPlayer.name)
            elif questions == "3":
                dialogue_mod.Barmaid_shop()
    ###############—-—INN—-—###############

    elif zone_map[myPlayer.location][ZONENAME] == "shop":
        print("No one is here.")

    else:
        print("True")

def MAP_look():
    print("\n====================================================================\n")
    mapsRPG.SteamBlackfall_map()
    print("\n====================================================================\n")







#### GAME ####
def swapequiped():
    try:
        print("Current Equips:\n")
        print(f"(1) = {myPlayer.equiped[0]}")
        print(f"(2) = {myPlayer.equiped[1]}")
        
        item = str(input("which item would you like to swap? Type (1) or (0)> "))
        if item == "1":
            myPlayer.inv.append(myPlayer.equiped[0])
            myPlayer.equiped.remove(myPlayer.equiped[0])
            print(f"{myPlayer.equiped[0]}(x1) added to inventory.")
        elif item == "2":
            myPlayer.inv.append(myPlayer.equiped[1])
            myPlayer.equiped.remove(myPlayer.equiped[1])
            print(f"{myPlayer.equiped[1]}(x1) added to invinventory.")
        item = str(input("what item would you like to equiped?: "))
        if item in myPlayer.inv:
            myPlayer.equiped.append(item)
            myPlayer.inv.remove(item)

        print()
        print(myPlayer.inv)
        print(myPlayer.equiped)
    except:
        print(myPlayer.equiped)
        print("you may have 1 or no items in, you must be carying 2 items to swap.")
        item = str(input("what item would you like to equiped?: "))
        if item in myPlayer.inv:
            myPlayer.equiped.append(item)
            myPlayer.inv.remove(item)


def main_game_loop():
    while gameOver is False:
        prompt()

### Name Colecting ####





def setup_game():
    os.system('cls')
    
    q1 = "Hello, Whats your name?\n"
    for character in q1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name
    q2 = "What is your class?\n"
    q2_added = "(You can choose Machanic, Welder, Steam-forger)\n"
    for character in q2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in q2_added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)            
    player_job = input("> ")
    valid_jobs = ["Machanic", "Welder", "Steam-forger"]
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print(f"You choose {player_job}.\n")
        while player_job.lower() not in valid_jobs:
            player_job = input("> ")
            if player_job.lower() in valid_jobs:
                myPlayer.job = player_job
    
        
    if myPlayer.job == "machanic":
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job == "welder":
        myPlayer.hp = 40
        myPlayer.Ip = 120
    elif myPlayer.job == "steam-forger":
        myPlayer.hp = 65
        myPlayer.mp = 60

    
    
    q3 = f"welcome {player_name} the {player_job}\n"
    for character in q3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speach1 = "\n\n"

    for character in speach1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.031)

    input("To continue Press enter.")
    os.system('cls')
    msg = ("+——————————————————————————+\n|       -=start=-          |\n+——————————————————————————+")
    for character in msg:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    main_game_loop()

######################################### —- USE -— #########################################
def use_Item():
    item = str(input("Item You want to use: "))
    if item in myPlayer.equiped:
        print(f"You use you're {item}")

    elif item in myPlayer.inv:
        print("swap your item to equips")


#### Shop ####
def Inn_shop():
    while True:
        ans = input("> ")
        if ans.lower == "mead":
                if myPlayer.money_sp >= 15:
                    print("Health restored")
                    if myPlayer.job == "fighter":
                        myPlayer.hp = 120
                        myPlayer.mp = 20
                    elif myPlayer.job == "mage":
                        myPlayer.hp = 40
                        myPlayer.mp = 120
                    elif myPlayer.job == "priest":
                        myPlayer.hp = 65
                    myPlayer.mp = 60
        else:
            print("Error wrong input") 



#### THE GAME START ####    
title_screen()
