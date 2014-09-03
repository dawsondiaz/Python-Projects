# Take care of the wonderful imports #       #
import time                                  #
import sys                                   #
from random import randrange                 #
import text
from colorama import init                    #
from colorama import Fore, Back, Style       #
init()                                       #
##############################################
def tips():
	text.print_fast_red('''== TIPS FOR BETTER GAMEPLAY ==
- Avoid pressing enter more than once
- Do not press any keys while text is printing
- Change background of terminal to black
- SUGGEST NEW FEATURES!!
''')
	text.print_fast_yellow('''== FRQUENTLY ASKED QUESTIONS ==
Q.) Why did you make this?
A.) It was for a school project
''')
	text.print_slow_cyan('''If you have any questions, please
contact Dawson at contact@dawsondiaz.com\n
''')
