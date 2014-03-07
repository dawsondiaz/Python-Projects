# Take care of the wonderful imports #       #
import time                                  #
import sys                                   #
from random import randrange                 #

from .initialise import init, deinit, reinit
from .ansi import Fore, Back, Style
from .ansitowin32 import AnsiToWin32         #                                       #
##############################################


def conch():
    print (Fore.YELLOW + Style.BRIGHT + '''  _______ _             _____                 _     
 |__   __| |           / ____|               | |    
    | |  | |__   ___  | |     ___  _ __   ___| |__  
    | |  | '_ \ / _ \ | |    / _ \| '_ \ / __| '_ \ 
    | |  | | | |  __/ | |___| (_) | | | | (__| | | |
    |_|  |_| |_|\___|  \_____\___/|_| |_|\___|_| |_|
                                                    
               /\'
              {.-}
             ;_.-"\'
            {    _.}_
             \.-" /  `,
              \  |    /
               \ |  ,/
                \|_/
''')
def mini():
	print (Fore.YELLOW + Style.BRIGHT + '''
               /\'
              {.-}
             ;_.-"\'
            {    _.}_
             \.-" /  `,
              \  |    /
               \ |  ,/
                \|_/	
	''')
