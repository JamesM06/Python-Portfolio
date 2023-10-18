import cmd, textwrap, sys, os, time, random
import mapsRPG
import dialogue_mod


screen_width = 100

settings_color = "0"
gameOver = False
mage_spells = ["Fireball", "Frost Nova", "Arcane Missile", "Teleport", "Invisibility", "Lightning Bolt", "Ice Shield", "Summon Familiar", "Mana Drain", "Blink"]
priest_spells = ["Heal", "Divine Shield", "Smite", "Holy Nova", "Blessing of Strength", "Resurrection", "Purify", "Divine Wrath", "Guardian Spirit", "Spiritual Renewal"]




class player:
    def __init__(self):
        self.name = ""
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.location = 'Inn'
        self.status_effects = []
        self.inv = ["dagger", "pike", "axe"]
        self.equiped = [] # There will only be two lots
        self.money_cp = 150
        self.money_sp = 30
        self.money_gp = 7
        self.ac = 10 # Armor class
        self.quest = ["Investigate the land"]

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

    print("+——————————————————————————+")
    print("|   welcome to Chapter 2   |")
    print("+——————————————————————————+")
    print("      #   Play   #           ")
    print("      #   Help   #           ")
    print("      # settings #       ")
    print("      #   Quit   #           ")
    print(" (WIP) - Made by James :).")
    title_screen_selection()

def help_menu():
    os.system('cls')
    print("+——————————————————————————+")
    print("|   welcome to Chapter 2   |")
    print("+——————————————————————————+")
    print("# Use up, down, left, right to move")
    print("# Type your commands to do them")
    print("# Use 'look' to inspect somthing ")
    print("# Good look!")
    print("#Is there is a * befor a diolog option it is a integrel question.")
    title_screen_selection()

def settings_menu():
    os.system('cls')
    print("+——————————————————————————+")
    print("|   welcome to Chapter 2   |")
    print("+——————————————————————————+")
    print("      #   color   #         ")
    print("      # Difficulty #        ")