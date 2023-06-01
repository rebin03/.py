import random

x=random.randint(1,100)

print('---NUMBER GUESSING GAME---\n')
print('You can guess a nummber between 1 and 100\nYou have only 10 chances to guess the number!!')

guess = int(input("Guess a number: "))
count = 1

if x == guess:
    print('Wow!! You guessed the number right in the first try.')
else:
    while x != guess and count<10:
        count += 1
        if x > guess:
            print('You guessed a smaller number\n')
        else:
            print('You guessed a larger number\n')
        guess = int(input("Guess a number: "))
    if x == guess:
        print('\nYou guessed the number right!!')
    else:
        print('\nYou lost the game!!')
        print('The number was: ', x)

print('\n---END---')
