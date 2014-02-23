##############################################
# A Lord of the Flies Text Adventure Game    #
# Programming: Dawson Diaz, Jesse Doke       #
# Writing: Nicholas Pilgrim, Raymond Sweeney #
# Version 1.0, Written in Pythoon 3.3.4      #
##############################################


# Take care of the wonderful imports #
import time
import sys
from random import randrange

# Engine Imports from Game Directory #
from engine import beach
from engine import clear


text = "** Execute Long Intro **"

for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 2, 1))
    seconds = float(seconds)
    time.sleep(seconds)


# Wait one second before executing next line
time.sleep(1)



# First Quest
obj1 =input('\nDo you \na.) Rest on the ground \nb.) Find a way out of the jungle\n').lower()

while obj1 not in ('a', 'b'):
    obj1 = input("Invallid. Please Enter again: ").lower()

# Path 1 #
if obj1 == 'a':
    print('You find a comfortable spot on the ground and drift into sleep...')
    time.sleep(1)
    text = ('Zzz.\nZzz..\nZzz...\n')
    # Script
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0." + str(randrange(1, 2, 1))
        seconds = float(seconds)
        time.sleep(seconds)
    print('You wake to a strange noise, and work your way out of the jungle.') 
    time.sleep(1)
    
# Second Quest    
    print('You emerge out of the jungle and walk along the shoreline of a sunny beach')
    # PRINT BEACH #
    beach.beach()
    time.sleep(1)
    print('** Objective One Completed **')
    time.sleep(2)
    # PRESS KEY #
    input("Press enter to continue...")
    print("==========================")
    text = "You hear a ruffle in the bushes behind you and you turn around\nYou are approached by a fat kid\nHe identifies himself as Piggy.\n"

# Script for Slow Text
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0." + str(randrange(1, 2, 1))
        seconds = float(seconds)
        time.sleep(seconds)
    while True:
        name =input('Piggy: What is your name?\n').strip()
        if len(name.split()) == 1:
            name = name.title()
            break
        else:
            print("Too Long! Make it shorter, if you have a name like 'Mary Joe', please seperate it by using a '-'")
    time.sleep(1)
    print('Hello, {}. Piggy is what they call me at school. Please do not tell anyone!'.format(name))
    time.sleep(1)
    print('{}: responds with HAHA PIGGY!'.format(name))
    time.sleep(1)
    print('** Objective Two Completed **')
    time.sleep(2)
    # PRINT KEY #
    input('Press enter to continue...')
    print("==========================")
    ## NEXT OBJECTIVE #
    print('You and Piggy walk over to the beack and begin to swim.\nYou notice his heavy breathing, what do you ask him?')
    time.sleep(1)
    obj2 =input("a.) Why are you breathing hard?\nb.) Have you seen anyone else?\nc.) Why don't you swim\n")
    while obj2 not in ('a', 'b','c'):
        obj2 = input("Invallid. Please Enter again: ")
    if obj2 == 'a':
        print('Piggy: Because I have asthma')
    elif obj2 == 'b':
        print('Piggy: I am afriad I have not seen any other people')
    elif obj2 == 'c':
        print('Piggy: Because of my asthma, and my auntie does not allow me to.')
    print('** Objective Three Completed **')
    time.sleep(2)
    input('Press enter to continue...')
    print("==========================")
    # NEXT OBJECTIVE #
    print('You walk over to a pond with that is being emptied by a large waterfall.\nYou see a shell. What do you do with it?')
    time.sleep(1)
    obj3 =input('a.) Pick it up\nb.) Continue to swim\n') 
    while obj3 not in ('a', 'b'):
        obj3 =input("Invallid. Please Enter Again: ")
    if obj3 == 'a':
        print('You pick up the shell')
    elif obj3 == 'b':
        print('You swim for awhile and then your attention is grabbed by Piggys admiration for the shell.')
        time.sleep(1)
        print('You pick up the shell')
# Path 2 #

elif obj1 == 'b':
    print('You manage to find a path out of the jungle and discover a beach,')
    beach.beach()
    time.sleep(1)
    print('** Objective One Completed **')
    input('Press enter to continue...')
    print('==========================')
    time.sleep(1)
    text = "You hear a ruffle in the bushes behind you and your turn around\nYou are approached by a fat kid\nHe identifies himself as Piggy.\n"

# Script for Slow Text
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0." + str(randrange(1, 2, 1))
        seconds = float(seconds)
        time.sleep(seconds)

    while True:
        name =input('Piggy: What is your name?\n').strip()
        if len(name.split()) == 1:
            name = name.title()
            break
        else:
            print("Too Long! Make it shorter, if you have a name like 'Mary Joe', please seperate it by using a '-'")
    time.sleep(1)
    print('Hello, {}. Piggy is what they call me at school. Please do not tell anyone!'.format(name))
    time.sleep(1)
    print('{}: responds with HAHA, PIGGY!'.format(name))
    time.sleep(1)
    print('** Objective Two Completed **')
    time.sleep(2)
    # PRINT KEY #
    input('Press enter to continue...')
    print("==========================")
    ## NEXT OBJECTIVE #
    print('You and Piggy walk over to the beack and begin to swim.\nYou notice his heavy breathing, what do you ask him?')
    time.sleep(1)
    obj2 =input("a.) Why are you breathing hard?\nb.) Have you seen anyone else?\nc.) Why don't you swim\n")
    while obj2 not in ('a', 'b','c'):
        obj2 = input("Invallid. Please Enter again: ")
    if obj2 == 'a':
        print('Piggy: Because I have asthma')
    elif obj2 == 'b':
        print('Piggy: I am afriad I have not seen any other people')
    elif obj2 == 'c':
        print('Piggy: Because of my asthma, and my auntie does not allow me to.')
    print('** Objective Three Completed **')
    time.sleep(2)
    input('Press enter to continue...')
    print("==========================")
    # NEXT OBJECTIVE #
    print('You walk over to a pond with that is being emptied by a large waterfall.\nYou see a shell. What do you do with it?')
    time.sleep(1)
    obj3 =input('a.) Pick it up\nb.) Continue to swim\n') 
    while obj3 not in ('a', 'b'):
        obj3 =input("Invallid. Please Enter Again: ")
    if obj3 == 'a':
        print('You pick up the shell')
    elif obj3 == 'b':
        print('You swim for awhile and then your attention is grabbed by Piggys admiration for the shell.')
        time.sleep(1)
        print('You pick up the shell')
    
    
print('Piggy: Tells me about the conch')
time.sleep(1)
print('You take the conch, and die.')
quit
