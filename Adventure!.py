# Python Text RPG
#

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# PLAYER SETUP


class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.job = ''
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


myPlayer = Player()

# TITLE SCREEN


def title_screen_selections():
    option = input('> ')
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def title_screen():
    os.system('cls')
    print('############################')
    print('# Welcome to the text RPG! #')
    print('############################')
    print('         --Play--           ')
    print('         --Help--           ')
    print('         --Quit--           ')
    print('____________________________')
    title_screen_selections()


def help_menu():
    print('####################################')
    print('##### Welcome to the text RPG! #####')
    print('####################################')
    print(' Use up, down, left, right to move  ')
    print('      Type commands to do them      ')
    print('  Use "Look" to inspect something   ')

    print('Best of luck and thanks for playing ')
    print('____________________________________')
    title_screen_selections()


# MAP


"""
# Player Starts at B2

a1-a2-a3-a4
b1-b2-b3-b4
c1-c2-c3-c4
d1-d2-d3-d4
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
        },
    'a2': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home!',
        EXAMINATION: 'Your home looks the same.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: '',
    },
}

# GAME INTERACTIVITY


def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print("\n" + "==========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())


def player_move(action):
    ask = "where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone")
    else:
        print("")

# GAME FUNCTIONALITY


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # Here is where you handle if puzzles have been solved, boss defeated etc


def setup_game():
    os.system('cls')
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    # JOB HANDLING
    question2 = "What role do you wish to play?\n"
    question2added = "(You can play as a warrior, mage or a priest)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    myPlayer.job = player_job
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        print("The only valid classes are Warrior, Mage or Priest")
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")

    # PLAYER STATS

    if myPlayer.job == 'Warrior':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job == 'Mage':
        self.hp = 60
        self.mp = 100
    elif myPlayer.job == 'Priest':
        self.hp = 60
        self.mp = 60

    # INTRODUCTION
    question3 = "Welcome " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "Welcome to this fantasy world\n"
    speech2 = "I hope it greets you well\n"
    speech3 = "Just make sure you don't get too lost\n"
    speech4 = "Hehehehe...\n"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    time.sleep(5)
    os.system('cls')
    print("##########################")
    print("#    Let's start now    #!")
    print("##########################")
    main_game_loop()


title_screen()
