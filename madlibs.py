from random import choice,randint
from time import sleep

nouns = ('Chuck Norris' , 'Winnie the Pooh' , 'Rambo')
verbs = ('gracefully' , 'peacefully' , 'internally')
advs = ('logs in' , 'kills' , 'waves')
adjs =('spontaneous' , 'hairy' , 'stupid')

print('%s %s %s %s' % (choice(adjs), choice(nouns), choice(advs), choice(verbs)))

sleep(2)
