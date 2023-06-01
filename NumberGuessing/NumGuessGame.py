import random

x=random.randint(1,100)

print('---NUMBER GUESSING GAME---\n')
print('You can guess a nummber between 1 and 100\nYou can guess untill you find the number!!')

guess = int(input("Guess a number: "))

if x == guess:
    print('Wow!! You guessed the number right in the first try.')
else:
    while x != guess:
        if x > guess:
            print('You guessed a smaller number\n')
        else:
            print('You guessed a larger number\n')
        guess = int(input("Guess a number: "))
    print('You guessed the number right!!')
print('The number was: ', x)
print('\n---END---')
