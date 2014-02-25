##############################################
# A Lord of the Flies Text Adventure Game    #
# Programming: Dawson Diaz, Jesse Doke       #
# Writing: Nicholas Pilgrim                  #
# Colorama: By Jonathan Hartley              #
# Version 1.6, Written in Python 2.7.6       #
##############################################
                                             #
# Take care of the wonderful imports #       #
import time                                  #
import sys                                   #
from random import randrange                 #
                                             #
# Engine Imports from Game Directory #       #
from engine import beach                     #
from engine import clear                     #
from engine import conch                     #
from engine import sun                       #
from engine import title                     #
from engine import island                    #
from colorama import init                    #
from colorama import Fore, Back, Style       #
init()                                       #
##############################################
title.title()
text = "Your plane has crashed on a remote island.\nYou have been trying to find your way out of the jungle for the past hour.\nYou have not seen any other human being or adult since the plane crash.\nYou have no food or water."

for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 2, 1))
    seconds = float(seconds)
    time.sleep(seconds)


# Wait one second before executing next line
time.sleep(1)



# First Quest
obj1 =raw_input('\nDo you \na.) Rest on the ground \nb.) Find a way out of the jungle\n').lower()

while obj1 not in ('a', 'b'):
    obj1 = raw_input("Invallid. Please Enter again: ").lower()

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
    print('You emerge out of the jungle and walk along the shoreline of a sunny beach.')
    # PRINT BEACH #
    beach.beach()
    time.sleep(1)
    print('** Objective One Completed **')
    time.sleep(2)
    # PRESS KEY #
    raw_input("Press enter to continue...")
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
        name =raw_input('Piggy: What is your name?\n').strip()
        if len(name.split()) == 1:
            name = name.title()
            break
        else:
            print("Ahhhj Make it shorter or actually enter a name. If you have a name like 'Mary Joe', please seperate it by using a '-'")
    if name ==('Kelly'):
        print('Heyy Bffl.')
    if name == ('Sarah'):
        print('AHHHHHHHJ, sorry I needed to say that. Continue :)')
    time.sleep(1)
    print('Hello, {}. Piggy is what they call me at school. Please do not tell anyone!'.format(name))
    time.sleep(1)
    print('{}: responds with HAHA PIGGY!'.format(name))
    time.sleep(1)
    print('** Objective Two Completed **')
    time.sleep(2)
    # PRINT KEY #
    raw_input('Press enter to continue...')
    print("==========================")
    ## NEXT OBJECTIVE #
    print('You and Piggy walk over to the beack and begin to swim.\nYou notice his heavy breathing, what do you ask him?')
    time.sleep(1)
    obj2 =raw_input("a.) Why are you breathing hard?\nb.) Have you seen anyone else?\nc.) Why don't you swim\n").lower()
    while obj2 not in ('a', 'b','c'):
        obj2 = raw_input("Invallid. Please Enter again: ").lower()
    if obj2 == 'a':
        print('Piggy: Because I have asthma.')
    elif obj2 == 'b':
        print('Piggy: I am afriad I have not seen any other people.')
    elif obj2 == 'c':
        print('Piggy: Because of my asthma, and my auntie does not allow me to.')
    print('** Objective Three Completed **')
    time.sleep(2)
    raw_input('Press enter to continue...')
    print("==========================")
    # NEXT OBJECTIVE #
    print('You walk over to a pond with that is being emptied by a large waterfall.\nYou see a shell. What do you do with it?')
    time.sleep(1)
    obj3 =raw_input('a.) Pick it up\nb.) Continue to swim\n').lower()
    while obj3 not in ('a', 'b'):
        obj3 =raw_input("Invallid. Please Enter Again: ").lower()
    if obj3 == 'a':
        print('You pick up the shell.')
    elif obj3 == 'b':
        print('You swim for awhile and then your attention is grabbed by Piggys admiration for the shell.')
        time.sleep(1)
        print('You pick up the shell.')
# Path 2 #

elif obj1 == 'b':
    print('You manage to find a path out of the jungle and discover a beach.')
    beach.beach()
    time.sleep(1)
    print('** Objective One Completed **')
    raw_input('Press enter to continue...')
    print('==========================')
    time.sleep(1)
    text = "You hear a ruffle in the bushes behind and you turn around\nYou are approached by a fat kid\nHe identifies himself as Piggy.\n"

# Script for Slow Text
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0." + str(randrange(1, 2, 1))
        seconds = float(seconds)
        time.sleep(seconds)

    while True:
        name =raw_input('Piggy: What is your name?\n').strip()
        if len(name.split()) == 1:
            name = name.title()
            break
        else:
            print("Ahhhj Make it shorter or actually enter a name. If you have a name like 'Mary Joe', please seperate it by using a '-'")
    if name == ('Kelly'):
        print('Hey Bffl, ily.')
    if name == ('Sarah'):
        print('AHHHHHHHJ, sorry I needed to say that. Continue :)')
    time.sleep(1)
    print('Hello, {}. Piggy is what they call me at school. Please do not tell anyone!'.format(name))
    time.sleep(1)
    print('{}: responds with HAHA, PIGGY!'.format(name))
    time.sleep(1)
    print('** Objective Two Completed **')
    time.sleep(2)
    # PRINT KEY #
    raw_input('Press enter to continue...')
    print("==========================")
    ## NEXT OBJECTIVE #
    print('You and Piggy walk over to the beack and begin to swim.\nYou notice his heavy breathing, what do you ask him?')
    time.sleep(1)
    obj2 =raw_input("a.) Why are you breathing hard?\nb.) Have you seen anyone else?\nc.) Why don't you swim\n").lower()
    while obj2 not in ('a', 'b','c'):
        obj2 = raw_input("Invallid. Please Enter again: ").lower()
    if obj2 == 'a':
        print('Piggy: Because I have asthma.')
    elif obj2 == 'b':
        print('Piggy: I am afriad I have not seen any other people.')
    elif obj2 == 'c':
        print('Piggy: Because of my asthma, and my auntie does not allow me to.')
    print('** Objective Three Completed **')
    time.sleep(2)
    raw_input('Press enter to continue...')
    print("==========================")
    # NEXT OBJECTIVE #
    print('You walk over to a pond with that is being emptied by a large waterfall.\nYou see a shell. What do you do with it?')
    time.sleep(1)
    obj3 =raw_input('a.) Pick it up\nb.) Continue to swim\n').lower()
    while obj3 not in ('a', 'b'):
        obj3 =raw_input("Invallid. Please Enter Again: ").lower()
    if obj3 == 'a':
        print('You pick up the shell.')
    elif obj3 == 'b':
        print('You swim for awhile and then your attention is grabbed by Piggys admiration for the shell.')
        time.sleep(1)
        print('You pick up the shell.')
# PRINT SHELL #
conch.conch()
# PRINT SHELL #
print('** Objective Four Completed **')
raw_input('Press enter to continue...')
print("==========================")   
# NEXT OBJECTIVE #
text = "Piggy: Ooh! It's a conch, I remember when I had one.\nI think if you blow through the bottom sound comes out of it.\n"
for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 2, 1))
    
    seconds = float(seconds)
    time.sleep(seconds)
obj4= raw_input('Do you\na.) Blow through the bottom of the shell\nb.) Ask piggy to blow the shell\n').lower()
while obj4 not in ('a','b'):
    obj4 =raw_input("Invalid. Please Enter Again: ").lower()
if obj4 == 'a':
    print('You blow through the bottom of the shell, and a loud noise comes out of it.')
elif obj4 == 'b':
    print('You ask piggy to blow the conch.')
    time.sleep(1)
    print("Piggy: I can't remember?, You're going to have to blow it.")
    time.sleep(1)
    print("You blow through the bottom of the shell, and a loud noise comes out of it.")
print('** Objective Five Completed **')
raw_input('Press enter to continue...')
print("==========================")
time.sleep(2)
print('Within the next few moments, boys begin to emerge all around you.\nThe nearest to you appear to be twins, what do you do?')
time.sleep(1)
obj5 =raw_input('Do you\na.) Ask for their names\nb.) Begin to gather all of the boys\nc.) Cower into the forest.\n').lower()
while obj5 not in ('a','b','c'):
    obj5 =raw_input("Invalid. Please Enter Again: ").lower()
if obj5 == 'a':
    print('You ask for their names')
    time.sleep(1)
    print('Twins: My name is Sam, and my name is Eric')
elif obj5 == 'b':
    print('You attempt to gather all of the boys, however, there are too many')
    time.sleep(1)
    print('The two twins approach you and ask for your name, you tell them your name is {}, and then they respond by telling you their names are Sam and Eric.'.format(name))
    time.sleep(1)
    print('You three hear the fait noise of that seems like marching.')
elif obj5 == 'c':
    print('You cower into the forest.')
    time.sleep(1)
    print('You get deep into the forest, however you decide to return outside because you heard a faint noise of what seems to be a large group of marching people')
    time.sleep(1)
    print('The two twins approach you and ask for your name, you tell them your name is {}, and then they respond by telling you their names are Sam and Eric.'.format(name))
    time.sleep(1)
print('** Objective Six Completed **')
raw_input('Press enter to continue...')
print("==========================")
time.sleep(1)
print('All of a sudden, you see a large group of boys marching in your direction.\nWhen they arrive, a person in the group faints.')
time.sleep(2)
print('The leader of the group (distinusged by an ornament on his cloak) asks\n"Who is the man with the trumpet"')
time.sleep(2)
print('You hesitate, but you respond with "I"\nYou follow by asking him a question')
time.sleep(2)
obj6 =raw_input('Do you\na.) Ask for his name\nb.) Ask who fainted, and if they are alright\n').lower()
while obj6 not in ('a','b'):
    obj6 =raw_input("Invalid. Please Enter Again: ").lower()
if obj6 == 'a':
    print('My name is Jack, Jack Marridew to be exact.')
elif obj6 == 'b':
    print('Oh yes, Simon is alright. That happens to him quite often\nMy name is Jack Marridew, and I am lead boy of the chior')
time.sleep(1)
print('Jack: I suppose if we have all of these kids on this island, we need a leader')
time.sleep(1)
print('You volunteer to be chief')
time.sleep(1)
print('Jack: Who thinks I should be chief?')
time.sleep(3)
print('Only three boys raise their hands.')
time.sleep(1)
print('Jack: Who thinks {} should be chief?'.format(name))
time.sleep(3)
print('The rest of the boys raise their hands')
time.sleep(1)
print('Jack: All right then, it is settled. {} will be cheif.'.format(name))
print('** Objective Seven Completed **')
raw_input('Press enter to continue...')
print("==========================")
time.sleep(1)

obj7 =raw_input('What is your first order as chief?\na.) Call a meeting\nb.) Assign Positions\nc.) Eliminate your rival Jack\nd.) Explore the island\n').lower()
while obj7 not in ('a','b','c','d'):
    obj7 =raw_input('Invalid. Please Enter Again:').lower()
if obj7 =='a':
    print('You call a meeting by blowing into the conch one more time')
    print('You begin by saying how important rescue is, and that a fire should be kept on at all times.')
    time.sleep(1)
    print('You give rules, the most important being whoever has the conch can talk, whoever does not may not speak')
    time.sleep(1)
    print('You also mention that shelter must be built, and that food must be aqquired.')
    time.sleep(1)
    print('You begin to assign roles,')
elif obj7 == 'b':
    print('You begin to assign roles,')
elif obj7 == 'c':
    #LOL#
    print('You charge towards Jack and begin to punch him. \nYou take the knife from its holder and attempt to stab him.')
    time.sleep(2)
    print('Unfortunatley, his chior steps in, and they MURDER you.')
    time.sleep(1)
    text = 'GAME OVER\n'
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0." + str(randrange(1, 2, 1))
        seconds = float(seconds)
        time.sleep(seconds)
    raw_input('Press enter to continue...')
    print("==========================")
    sys.exit()
    #LOL#
elif obj7 == 'd':
    print('You start talking about further exploration of the island, but piggy stops you.')
    time.sleep(1)
    print('Piggy: If we are going to explore, we must atlest give people jobs.')
    time.sleep(1)
    print('Piggy: We need ways to get food, water, shelter, and fire!')
    time.sleep(1)
    print('You begin to assign roles,')
time.sleep(2)
print('{}: Jack, you and your chior will be the hunters.'.format(name))
time.sleep(2)
print('{}: Piggy, you can collect names.'.format(name))
time.sleep(2)
print('{}: SamnEric, you can keep a fire going once we obtain one.'.format(name))
time.sleep(2)
print('{}: Now, we can explore the island.\n{}: How about Jack, and Simon come with me to explore'.format(name,name))
print('You go out with Jack and Simon to explore the island')
time.sleep(1)
sun.sun()
print('** Objective Eight Completed **')
raw_input('Press enter to continue...')
print("==========================")
time.sleep(1)
print('You explore the island.')
time.sleep(1)
print('THE ISLAND')
island.island()
time.sleep(2)
print('THE JUNGLE')
island.jungle()
time.sleep(2)
print('THE CASTLE ROCK')
island.castlerock()
time.sleep(2)
print('THE MOUNTAIN')
island.mountain()
time.sleep(2)
print('\n')
print('You have determined the three main parts of the island\nThe Jungle, The Castle Rock, and the Mountain.')
print('** Objective Nine Completed **')
raw_input('Press enter to continue...')
print("==========================")
print('You return back to Piggy at the camp.\nHe is startled by your arrival, what do you do?')
time.sleep(1)
obj8 =raw_input('a.) Ask Piggy what happened.\nb.) Order others to gather firewood, and start a fire.\nc.) Attempt to eliminate Jack, your competition.\n').lower()
while obj8 not in ('a','b','c'):
    obj8 =raw_input('Invalid. Please Enter Again:').lower()
if obj8 =='a':
    print('You proceed to ask piggy.')
elif obj8 == 'b':
    print('You order others to get wood, however they are not as many people here as there was before.')
    time.sleep(1)
    print('You proceed to ask piggy.')
elif obj8 == 'c':
    print('You charge towards Jack and begin to punch him. \nYou take the knife from its holder and attempt to stab him.')
    time.sleep(2)
    print('Unfortunatley, his chior steps in, and they MURDER you.')
    time.sleep(1)
    text = 'GAME OVER\n'
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0." + str(randrange(1, 2, 1))
        seconds = float(seconds)
        time.sleep(seconds)
    raw_input('Press enter to continue...')
    print("==========================")
    sys.exit()
time.sleep(2)
obj9 =raw_input('Do you ask\na.) Where did the kids go?\nb.) How many kids where here?\n')
while obj9 not in ('a', 'b'):
    obj9 =raw_input('Invalid. Please Enter Again:').lower()
if obj9 == 'a':
    print('Piggy: As soon as you left, the kids ran off, so I could not count how many there were.')
if obj9 == 'b':
    print('Piggy: The kids ran off, so I could not count how many there were.')
time.sleep(1)
print('Piggy: However, I did get a few. There was Robert, and Maurice, and Henry, and Simon.')
time.sleep(1)
print('** Objective Nine Completed **')
raw_input('Press enter to continue...')
print("==========================")
print('SamnEric emerge from the jungle carrying logs')
print('Suddenly an aircraft comes crashing down on you')
time.sleep(1)
print('The plane starts a fire, and everyone is left to starve to death on the island')
time.sleep(1)
print('No one is ever rescued, there are no survivors')
