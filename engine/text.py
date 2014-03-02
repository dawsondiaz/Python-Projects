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
def print_fast(str):
    for letter in str:
        sys.stdout.write(Fore.GREEN + Style.BRIGHT + letter)
        sys.stdout.flush()
        time.sleep(0.04)
def print_slow_red(str):
    for letter in str:
        sys.stdout.write(Fore.RED + Style.BRIGHT + letter)
        sys.stdout.flush()
        time.sleep(0.07)
def print_slow_darkblue(str):
    for letter in str:
        sys.stdout.write(Fore.BLUE + letter)
        sys.stdout.flush()
        time.sleep(0.07)
def print_slow_pink(str):
    for letter in str:
        sys.stdout.write(Fore.MAGENTA + Style.BRIGHT + letter)
        sys.stdout.flush()
        time.sleep(0.07)
def print_slow_blank(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)


