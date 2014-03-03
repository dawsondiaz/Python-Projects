# Take care of the wonderful imports #       #
import time                                  #
import sys                                   #
from random import randrange                 #
import text
from colorama import init                    #
from colorama import Fore, Back, Style       #
init()                                       #
##############################################
def license():
	text.print_fast_red('''== Disclaimer ==
NOT ALL ASPECTS OF THE GAME ARE TRUE TO WHAT HAPPENS IN THE BOOK.
PORTIONS WERE MODIFIED TO FIT WITH THE "TEXT GAME ENVIRONMENT."
WE ARE SORRY FOR ANY CONFUSION CAUSED BY PLAYING THE GAME.\n
''')
	text.print_fast_yellow('''== License ==
THIS GAME IS PROVIDED AS FREE SOFTWARE FOR EDUCATIONAL
PURPOSES ONLY. IT MAY NOT BE COMMERICALLY DISTRIBUTED.
INTELLECTUAL PROPERTY OF ANY CHARACTERS OR EVENTS IN
THIS GAME BELONG TO WILLIAM GOULDING.\n
''')
	text.print_slow_cyan('''If you have any questions, please
contact Dawson at contact@dawsondiaz.com\n
''')
