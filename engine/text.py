# Take care of the wonderful imports #       #
import time                                  #
import sys                                   #
from random import randrange                 #

from colorama import init                    #
from colorama import Fore, Back, Style       #
init()                                       #
##############################################
def print_slow(str):
    for letter in str:
        sys.stdout.write(Fore.GREEN + Style.BRIGHT + letter)
        sys.stdout.flush()
        time.sleep(0.07)
