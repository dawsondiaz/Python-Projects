# Take care of the wonderful imports #       #
import time                                  #
import sys                                   #
from random import randrange                 #

from colorama import init                    #
from colorama import Fore, Back, Style       #
init()                                       #
##############################################
def title():
	print(Fore.YELLOW + Style.BRIGHT + """:""" + Style.BRIGHT + Fore.RED + """:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""" + Fore.YELLOW + Style.BRIGHT + """:""" + Fore.YELLOW + Style.BRIGHT + """
:""" + Fore.GREEN + Style.BRIGHT + """                        _______ _                                            """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """                       |__   __| |                                           """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """                          | |  | |__   ___                                   """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """                          | |  | '_ \ / _ \                                  """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """                          | |  | | | |  __/                                  """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """                          |_|  |_|_|_|\___|                                  """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """  _                   _           _   _   _            ______   _            """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """ | |                 | |        / _| | | | |          |  ____| (_)           """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """ | |     ___  _ __ __| |   ___ | |_  | |_| |__   ___  | |__  | |_  ___  ___  """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """ | |    / _ \| '__/ _` |  / _ \|  _| | __| '_ \ / _ \ |  __| | | |/ _ \/ __| """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """ | |___| (_) | | | (_| | | (_) | |   | |_| | | |  __/ | |    | | |  __/\__ \ """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """ |______\___/|_|_ \__,_|  \___/|_|    \__|_| |_|\___| |_|    |_|_|\___||___/ """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """  _______        _                 _                 _                       """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """ |__   __|      | |       /\      | |               | |                      """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """    | | _____  _| |_     /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___      """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """    | |/ _ \ \/ / __|   / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \     """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """    | |  __/>  <| |_   / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/     """ + Fore.YELLOW + Style.BRIGHT + """:
:""" + Fore.GREEN + Style.BRIGHT + """    |_|\___/_/\_\\__|  /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|     """ + Fore.YELLOW + Style.BRIGHT + """:\n:                                                                             :"""
+ Fore.YELLOW + Style.BRIGHT + """
:""" + Fore.RED + Style.BRIGHT + """:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""" + Fore.YELLOW + Style.BRIGHT + """:""")

def title_old():
    print(Fore.GREEN + Style.BRIGHT + """:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:    _                   _          __   _   _           ______ _ _             :
:   | |                 | |        / _| | | | |          |  ___| (_)            :
:   | |     ___  _ __ __| |   ___ | |_  | |_| |__   ___  | |_  | |_  ___  ___   :
:   | |    / _ \| '__/ _` |  / _ \|  _| | __| '_ \ / _ \ |  _| | | |/ _ \/ __|  :
:   | |___| (_) | | | (_| | | (_) | |   | |_| | | |  __/ | |   | | |  __/\__ \  :
:   \_____/\___/|_|  \__,_|  \___/|_|    \__|_| |_|\___| \_|   |_|_|\___||___/  :
:   _____ _            _____         _                                        :
:  |_   _| |          |_   _|       | |                                       :
:    | | | |__   ___    | | _____  _| |_                                      :
:    | | | '_ \ / _ \   | |/ _ \ \/ / __|                                     :
:    | | | | | |  __/   | |  __/>  <| |_                                      :
:    \_/ |_| |_|\___|   \_/\___/_/\_\\__|                                      :
:    ___      _                 _                                             :
:   / _ \    | |               | |                                            :
:  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___                            :
:  |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \                           :
:  | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/                           :
:  \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|                           :
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""")