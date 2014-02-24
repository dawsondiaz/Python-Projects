##############################################
# A Lord of the Flies Text Adventure Game    #
# Programming: Dawson Diaz, Jesse Doke       #
# Writing: Nicholas Pilgrim, Raymond Sweeney #
# Version 1.0, Written in Pythoon 3.3.4      #
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
                                             #
##############################################

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
    obj2 =input("a.) Why are you breathing hard?\nb.) Have you seen anyone else?\nc.) Why don't you swim\n").lower()
    while obj2 not in ('a', 'b','c'):
        obj2 = input("Invallid. Please Enter again: ").lower()
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
    obj3 =input('a.) Pick it up\nb.) Continue to swim\n').lower()
    while obj3 not in ('a', 'b'):
        obj3 =input("Invallid. Please Enter Again: ").lower()
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
    obj2 =input("a.) Why are you breathing hard?\nb.) Have you seen anyone else?\nc.) Why don't you swim\n").lower()
    while obj2 not in ('a', 'b','c'):
        obj2 = input("Invallid. Please Enter again: ").lower()
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
    obj3 =input('a.) Pick it up\nb.) Continue to swim\n').lower()
    while obj3 not in ('a', 'b'):
        obj3 =input("Invallid. Please Enter Again: ").lower()
    if obj3 == 'a':
        print('You pick up the shell')
    elif obj3 == 'b':
        print('You swim for awhile and then your attention is grabbed by Piggys admiration for the shell.')
        time.sleep(1)
        print('You pick up the shell')
# PRINT SHELL #
conch.conch()
# PRINT SHELL #
print('** Objective Four Completed **')
input('Press enter to continue...')
print("==========================")   
# NEXT OBJECTIVE #
text = "Piggy: Ooh! It's a conch, I remember when I had one.\nI think if you blow through the bottom sound comes out of it.\n"
for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 2, 1))
    
    seconds = float(seconds)
    time.sleep(seconds)
obj4= input('Do you\na.) Blow through the bottom of the shell\nb.) Ask piggy to blow the shell\n').lower()
while obj4 not in ('a','b'):
    obj4 =input("Invalid. Please Enter Again: ").lower()
if obj4 == 'a':
    print('You blow through the bottom of the shell, and a loud noise comes out of it.')
elif obj4 == 'b':
    print('You ask piggy to blow the conch')
    time.sleep(1)
    print("Piggy: I can't remember?, You're going to have to blow it")
    time.sleep(1)
    print("You blow through the bottom of the shell, and a loud noise comes out of it.")
print('** Objective Five Completed **')
input('Press enter to continue...')
print("==========================")
time.sleep(1)
print('Within the next few moments, boys begin to emerge all around you.\nThe nearest to you appear to be twins, what do you do?')
time.sleep(1)
obj5 =input('Do you\na.) Ask for their names\nb.) Begin to gather all of the boys\nc.) Cower into the forest.\n').lower()
while obj5 not in ('a','b','c'):
    obj5 =input("Invalid. Please Enter Again: ").lower()
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
    print('You get deep into the forest, however you decide to return outside because you heard a faint noise of what seems to be a large group of marching people')
    print('The two twins approach you and ask for your name, you tell them your name is {}, and then they respond by telling you their names are Sam and Eric.'.format(name))
print('** Objective Six Completed **')
input('Press enter to continue...')
print("==========================")
time.sleep(1)
print('All of a sudden, you see a large group of boys marching in your direction.\nWhen they arrive, a person in the group faints.')
time.sleep(1)
print('The leader of the group (distinusged by an ornament on his cloak) asks "Who is the man with the trumpet"')
time.sleep(2)
print('You hesitate, but you respond with "I"\n You follow by asking him a question')
obj6 =input('Do you\na.) Ask for his name\nb.) Ask who fainted, and if they are alright\n').lower()
while obj6 not in ('a','b'):
    obj6 =input("Invalid. Please Enter Again: ").lower()
if obj6 == 'a':
    print('My name is Jack, Jack Marridew to be exact.')
elif obj6 == 'b':
    print('Oh yes, Simon is alright. That happens to him quite often\nMy name is Jack Marridew, and I am lead boy of the chior')
time.sleep(1)
print('Jack: I suppose if we have all of these kids on this island, we need a leader')
