print('''
You will be asked my age, if you fail to guess correctly, that's to bad for you.
''')
inputs = input
numGuesses = 0

while inputs != 15:
    numGuesses += 1
    inputs = int(input('Can you guess how old I am? '))

    if inputs == 15:
        print('You did it!')
    elif inputs > 15:
        print('Keep Trying!')
    else:
        print('Too Low!')

if numGuesses == 1:
    print('Fantastic Job!')

elif numGuesses < 5:
    print('Good Job! You have guessed my age in' , numGuesses, 'trys!')

else:
    print('You have guessed my age in', numGuesses, 'trys you could have done better!')
