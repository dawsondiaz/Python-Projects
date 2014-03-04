##############################################
# A Lord of the Flies Text Adventure Game    #
# Programming: Dawson Diaz, Jesse Doke       #
# Writing: Nicholas Pilgrim                  #
# Colorama: By Jonathan Hartley              #
# Version 1.7.2, Written in Python 2.7.6     #
##############################################
                                             #
# Take care of the wonderful imports #       #
import time                                  #
import sys                                   #
from random import randrange                 #
import os                                    #
                                             #
# Engine Imports from Game Directory #       #
from engine import beach                     #
from engine import text                      #
from engine import conch                     #
from engine import sun                       #
from engine import title                     #
from engine import island                    #
from engine import init                      #
from engine import Fore, Back, Style         #
from engine import names                     #
from engine import license                   #
init(autoreset=True)                         #
##############################################

# INTRODUCTION #
title.title() # This will print the title defined in /engine/title.py
text.print_fast("""Programming: Dawson Diaz, Jesse Doke
Writing: Nicholas Pilgrim\n
""")
title = raw_input(Fore.GREEN + Style.BRIGHT + "Press enter to begin or enter " + Style.BRIGHT + Fore.RED + "'l'" + Style.BRIGHT + Fore.GREEN + " to view licenses and disclaimers... ") # This will require the player to press enter before printing next line
os.system('cls' if os.name == 'nt' else 'clear') # This will clear the window
# INTRODUCTION #
if title == 'l':
    license.license()
    raw_input(Fore.CYAN + Style.BRIGHT +'Press enter to continue...')

os.system('cls' if os.name == 'nt' else 'clear') # This will clear the window
# The following line will print using a method defined in /engine/text.py
text.print_slow("""Your plane has crashed on a remote island.
You have been trying to find your way out of the jungle for the past hour.
You have not seen any other human being since the plane crash.
You have no food or water.""")

time.sleep(1) # Wait one second before executing next line
obj1 =raw_input(Fore.CYAN + Style.BRIGHT + '\nDo you \na.) Rest on the ground \nb.) Find a way out of the jungle\n').lower()
while obj1 not in ('a', 'b'):
    obj1 = raw_input(Fore.CYAN + Style.BRIGHT + "Invallid. Please Enter again: ").lower()

# Objective 1 #
if obj1 == 'a':
    text.print_slow('You find a comfortable spot on the ground and drift into sleep...\n')
    time.sleep(1)
    text.print_slow('Zzz.\nZzz..\nZzz...\n')
    text.print_slow('You wake to a strange noise, and work your way out of the jungle.\n') 
    time.sleep(1) # Wait one second before executing next line       
    text.print_slow('You emerge out of the jungle and walk along the shoreline of a sunny beach.') 
elif obj1 == 'b':
    text.print_slow('You manage to find a path out of the jungle and discover a beach.')

time.sleep(2) # Wait two seconds before executing next line
beach.beach() # This will print the image defined in /engine/beach.py
time.sleep(1) # Wait one second before executing next line
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective One Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)
text.print_slow("You hear a ruffle in the bushes behind and you turn around.\nYou are approached by a fat kid.\nHe identifies himself as Piggy.\n")
while True:
    name =raw_input(Fore.MAGENTA + Style.BRIGHT +'Piggy: What is your name?\n').strip()
    if len(name.split()) == 1:
        name = name.title()
        break
    else:
        print(Fore.RED + Style.BRIGHT +"Ahhj. Please make your name shorter or actually enter a name. If you have a name like 'Mary Joe', please seperate it by using a '-'")
# Custom Messages for people that play the game #
if name == ('Kelly'):
        names.kelly_auth()
if name == ('Sarah'):
        names.sarah()
if name == ('Dawson'):
        names.dawson()
# Custom Messages for people that play the game #
time.sleep(1)
text.print_slow_pink('Piggy: Hello, {}. Piggy is what they call me at school.\nPiggy: Please do not tell anyone!\n'.format(name))
time.sleep(1)
text.print_slow_red('{}: HAHA, PIGGY!\n'.format(name))
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Two Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1
           )
## NEXT OBJECTIVE #
text.print_slow('You and Piggy walk over to the beach and begin to swim.\nYou notice his heavy breathing, what do you ask him?\n')
time.sleep(1)
obj2 =raw_input(Fore.CYAN + Style.BRIGHT + "a.) Why are you breathing hard?\nb.) Have you seen anyone else?\nc.) Why don't you swim\n").lower()
while obj2 not in ('a', 'b','c'):
    obj2 = raw_input(Fore.CYAN + Style.BRIGHT + "Invallid. Please Enter again: ").lower()
if obj2 == 'a':
    text.print_slow_pink('Piggy: Because I have asthma.\n')
elif obj2 == 'b':
    text.print_slow_pink('Piggy: I am afriad I have not seen any other people.\n')
elif obj2 == 'c':
    text.print_slow_pink('Piggy: Because of my asthma, and my auntie does not allow me to.\n')
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Three Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# NEXT OBJECTIVE #
text.print_slow('You walk over to a pond that is being emptied by a large waterfall.\nYou see a shell. What do you do with it?\n')
time.sleep(1)
obj3 =raw_input(Fore.CYAN + Style.BRIGHT + 'a.) Pick it up\nb.) Continue to swim\n').lower()
while obj3 not in ('a', 'b'):
    obj3 =raw_input(Fore.CYAN + Style.BRIGHT + "Invallid. Please Enter Again: ").lower()
if obj3 == 'a':
    text.print_slow('You pick up the shell.\n')
elif obj3 == 'b':
    text.print_slow('You swim for awhile and then your attention is grabbed by Piggys admiration for the shell.\n')
    time.sleep(1)
    text.print_slow('You pick up the shell.\n')
# PRINT SHELL #
conch.conch()
# PRINT SHELL #
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Four Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# NEXT OBJECTIVE #
text.print_slow_pink("Piggy: Ooh! It's a conch, I remember when I had one.\nI think if you blow through the bottom sound comes out of it.\n")
obj4= raw_input(Fore.CYAN + Style.BRIGHT + 'Do you\na.) Blow through the bottom of the shell\nb.) Ask piggy to blow the shell\n').lower()
while obj4 not in ('a','b'):
    obj4 =raw_input(Fore.CYAN + Style.BRIGHT + "Invalid. Please Enter Again: ").lower()
if obj4 == 'a':
    text.print_slow('You blow through the bottom of the shell, and a loud noise comes out of it.\n')
elif obj4 == 'b':
    text.print_slow('You ask piggy to blow the conch.\n')
    time.sleep(1)
    text.print_slow_pink("Piggy: I can't remember?, You're going to have to blow it.\n")
    time.sleep(1)
    text.print_slow("You blow through the bottom of the shell, and a loud noise comes out of it.\n")
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Five Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# NEXT OBJECTIVE # 
text.print_slow('Within the next few moments, boys begin to emerge all around you.\nThe nearest to you appear to be twins, what do you do?\n')
time.sleep(1)
obj5 =raw_input(Fore.CYAN + Style.BRIGHT + 'Do you\na.) Ask for their names\nb.) Begin to gather all of the boys\nc.) Cower into the forest.\n').lower()
while obj5 not in ('a','b','c'):
    obj5 =raw_input(Fore.CYAN + Style.BRIGHT + "Invalid. Please Enter Again: ").lower()
if obj5 == 'a':
    text.print_slow('You ask for their names\n')
    time.sleep(1)
    text.print_slow_red('Twins: My name is Sam, and my name is Eric\n')
elif obj5 == 'b':
    text.print_slow('You attempt to gather all of the boys, however, there are too many\n')
    time.sleep(1)
    text.print_slow('The two twins approach you and ask for your name.\nYou tell them your name is {}.\nThey respond by telling you their names are Sam and Eric.\n'.format(name))
    time.sleep(1)
    text.print_slow('You three hear the fait noise of that seems like marching.\n')
elif obj5 == 'c':
    text.print_slow('You cower into the forest...\n')
    time.sleep(1)
    text.print_slow('You get deeper into the forest, however you decide to return outside.\nYou hear a faint noise.\nIt seems to be a large group of marching people\n')
    time.sleep(1)
    text.print_slow('The two twins approach you and ask for your name.\nYou tell them your name is {}.\nThey respond by telling you their names are Sam and Eric.\n'.format(name))
    time.sleep(1)
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Six Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# NEXT OBJECTIVE # 
text.print_slow('All of a sudden, you see a large group of boys marching in your direction.\nWhen they arrive, a person in the group faints.\n')
time.sleep(2)
text.print_slow('The leader of the group (distinusged by an ornament on his cloak) asks\n"Who is the man with the trumpet"\n')
time.sleep(2)
text.print_slow('You hesitate, but you respond with "I"\nYou follow by asking him a question.\n')
time.sleep(2)
obj6 =raw_input(Fore.CYAN + Style.BRIGHT + 'Do you\na.) Ask for his name\nb.) Ask who fainted, and if they are alright\n').lower()
while obj6 not in ('a','b'):
    obj6 =raw_input(Fore.CYAN + Style.BRIGHT + "Invalid. Please Enter Again: ").lower()
if obj6 == 'a':
    text.print_slow_red('My name is Jack, Jack Marridew to be exact.\n')
elif obj6 == 'b':
    text.print_slow_red('Oh yes, Simon is alright. That happens to him quite often\nMy name is Jack Marridew, and I am lead boy of the chior.\n')
time.sleep(1)
text.print_slow_red('Jack: I suppose if we have all of these kids on this island, we need a leader.\n')
time.sleep(1)
text.print_slow('You volunteer to be chief\n')
time.sleep(1)
text.print_slow_red('Jack: Who thinks I should be chief?\n')
time.sleep(3)
text.print_slow('Only three boys raise their hands.\n')
time.sleep(1)
text.print_slow_red('Jack: Who thinks {} should be chief?\n'.format(name))
time.sleep(3)
text.print_slow('The rest of the boys raise their hands.\n')
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Seven Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# NEXT OBJECTIVE #
text.print_slow('You have been elected chief.\n')
time.sleep(1)
obj7 =raw_input(Fore.CYAN + Style.BRIGHT + 'What is your first order as chief?\na.) Call a meeting\nb.) Assign Positions\nc.) Eliminate your rival Jack\nd.) Explore the island\n').lower()
while obj7 not in ('a','b','c','d'):
    obj7 =raw_input(Fore.CYAN + Style.BRIGHT +  'Invalid. Please Enter Again:').lower()
if obj7 =='a':
    text.print_slow('You call a meeting by blowing into the conch one more time.\n')
    text.print_slow('You begin by saying how important rescue is.\nYou mention that a fire should be kept on at all times.\n')
    time.sleep(1)
    text.print_slow('You give rules, the most important being whoever has the conch can talk.\nWhoever does not may not speak.\n')
    time.sleep(1)
    text.print_slow('You also mention that shelter must be built, and that food must be acquired.\n')
    time.sleep(1)
    text.print_slow('You begin to assign roles,\n')
elif obj7 == 'b':
    text.print_slow('You begin to assign roles,\n')
elif obj7 == 'c':
    #LOL#
    text.print_slow('You charge towards Jack and begin to punch him.\nYou take the knife from its holder and attempt to stab him.\n')
    time.sleep(2)
    text.print_slow_red('Unfortunatley, his chior steps in, and they MURDER you.')
    time.sleep(1)
    text.print_slow_red("""
GAME OVER\n
""")
    raw_input(Fore.CYAN + Style.BRIGHT + 'Press enter to continue...')
    print(Fore.CYAN + Style.BRIGHT + "==========================")
    time.sleep(1)
    sys.exit()
    #LOL#
elif obj7 == 'd':
    text.print_slow('You start talking about further exploration of the island, but piggy stops you.\n')
    time.sleep(1)
    text.print_slow_pink('Piggy: If we are going to explore, we must atlest give people jobs.\n')
    time.sleep(1)
    text.print_slow_pink('Piggy: We need ways to get food, water, shelter, and fire!\n')
    time.sleep(1)
    text.print_slow('You begin to assign roles,\n')
time.sleep(2)
text.print_slow_red('{}: Jack, you and your chior will be the hunters.\n'.format(name))
time.sleep(2)
text.print_slow_red('{}: Piggy, you can collect names.\n'.format(name))
time.sleep(2)
text.print_slow_red('{}: SamnEric, you can keep a fire going once we obtain one.\n'.format(name))
time.sleep(2)
text.print_slow_red('{}: Now, we can explore the island.\n{}: How about Jack, and Simon come with me to explore?\n'.format(name,name))
text.print_slow('You go out with Jack and Simon to explore the island.\n')

time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Eight Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# NEXT OBJECTIVE #

text.print_slow('You proceed to explore the island.\n')
text.print_slow('\n')
time.sleep(1)
text.print_slow('THE ISLAND\n')
text.print_slow('\n')
island.island()
time.sleep(2)
text.print_slow('THE JUNGLE\n')
text.print_slow('\n')
island.jungle()
time.sleep(2)
text.print_slow('THE CASTLE ROCK\n')
text.print_slow('\n')
island.castlerock()
time.sleep(2)
text.print_slow('THE MOUNTAIN\n')
text.print_slow('\n')
island.mountain()
time.sleep(2)
text.print_slow('\n')
text.print_slow('You have determined the three main parts of the island.\nThe Jungle, The Castle Rock, and the Mountain.\n')
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Nine Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# NEXT OBJECTIVE #

text.print_slow('You return back to Piggy at the camp.\nHe is startled by your arrival, what do you do?\n')
time.sleep(1)
obj8 =raw_input(Fore.CYAN + Style.BRIGHT + 'a.) Ask Piggy what happened.\nb.) Order others to gather firewood, and start a fire.\nc.) Attempt to eliminate Jack, your competition.\n').lower()
while obj8 not in ('a','b','c'):
    obj8 =raw_input(Fore.CYAN + Style.BRIGHT + 'Invalid. Please Enter Again:').lower()
if obj8 =='a':
    text.print_slow('You proceed to ask piggy something.\n')
elif obj8 == 'b':
    text.print_slow('You order others to get wood, however they are not as many people here as there were before.\n')
    time.sleep(1)
    text.print_slow('You proceed to ask piggy something.\n')
elif obj8 == 'c':
    #LOL#
    text.print_slow('You charge towards Jack and begin to punch him.\nYou take the knife from its holder and attempt to stab him.\n')
    time.sleep(2)
    text.print_slow_red('Unfortunatley, his chior steps in, and they MURDER you.')
    time.sleep(1)
    text.print_slow_red("""
GAME OVER\n
""")
    raw_input(Fore.CYAN + Style.BRIGHT + 'Press enter to continue...')
    print(Fore.CYAN + Style.BRIGHT + "==========================")
    time.sleep(1)
    sys.exit()
    #LOL#
time.sleep(2)
obj9 =raw_input(Fore.CYAN + Style.BRIGHT + 'Do you ask\na.) Where did the kids go?\nb.) How many kids where here?\n')
while obj9 not in ('a', 'b'):
    obj9 =raw_input(Fore.CYAB + Style.BRIGHT + 'Invalid. Please Enter Again:').lower()
if obj9 == 'a':
    text.print_slow_pink('Piggy: As soon as you left, the kids ran off, so I could not count how many there were.\n')
if obj9 == 'b':
    text.print_slow_pink('Piggy: The kids ran off, so I could not count how many there were.\n')
time.sleep(1)
text.print_slow_pink('Piggy: However, I did get a few. There was Robert, and Maurice, and Henry, and Simon.\n')

time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Ten Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)
# Next OBJECTIVE#
text.print_slow('Some boys emerge from the jungle.\n')
obj10 =raw_input(Fore.CYAN + Style.BRIGHT + 'Do you say\na.) We need a sign for ships and planes to come rescue us.\nb.) What should we do?\n')
while obj10 not in ('a', 'b'):
    obj10 =raw_input(Fore.CYAN + Style.BRIGHT + 'Invalid. Please Enter Again:').lower()
if obj10 == 'a':
    text.print_slow_pink('Piggy: We need to make shelters!\n')
    text.print_slow_red('Jack: No!\nJack: We need a large signal, like a fire up on the mountain!\n')
if obj10 == 'b':
    text.print_slow_pink('Piggy: We need to make shelters!\n')
    text.print_slow_red('Jack: No, Shut up!\n')
text.print_slow('The group re-forms and begins to climb the mountain.\nYou tell the others to gather firewood for a signal.\nYou follow by looking for something to light the fire\n')
obj11 =raw_input(Fore.CYAN + Style.BRIGHT + "What do you try first?\na.) Use piggy's specs.\nb.) Rub two sticks\n")
while obj11 not in ('a', 'b'):
    obj11 =raw_input(Fore.CYAN + Style.BRIGHT + 'Invalid. Please Enter Again:').lower()
if obj11 == 'a':
    text.print_slow('You ask Piggy for his specs...\n')
    text.print_slow_pink('Piggy: Why do you need my specs???\n')
if obj11 == 'b':
    text.print_slow('You search around for a while...\nYou finally select two sticks that you think are good for fire.\nYou proceed to rub them together.\nYou keep trying until you hear a scream from piggy.\nYou throw the sicks down to see what is going on.\n')
text.print_slow_red('Jack: Shut up Piggy, give them to me!\n')
text.print_slow('Jack takes Piggys specs, and starts a huge fire from gathered materials.\n')
text.print_slow('The fire becomes quite large, and then over takes a pile of wood set aside for future fires.\nAfter a while the fire engulfs 1/4th of the forest.\n')
text.print_slow_cyan('You have burnt 1/4th of the island.\n')
text.print_slow_pink('Piggy: Well that was SO useless.\n')
text.print_slow('Jack gives Piggy back his specs.\n')
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** Objective Eleven Completed **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to continue...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
time.sleep(1)
print(Fore.CYAN + Style.BRIGHT +'==========================')
print(Fore.BLUE + Style.BRIGHT +'** GAME STOPS HERE **')
raw_input(Fore.BLUE + Style.BRIGHT +'Press enter to close...')
print(Fore.CYAN + Style.BRIGHT +'==========================')
