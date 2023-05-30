import random
while True:
    print('--- WELCOME TO DICE ROLLER ---\n')
    print('1.Roll the dice\n2.Exit')
    user = int(input("what you want to do(1/2)\n"))
    
    if user == 1:
        number = random.randint(1,6)
        if number == 1:
            print('\nYour dice number is 1')
            print(' -----')
            print('|     |')
            print('|  •  |')
            print('|     |')
            print(' -----')
        elif number == 2:
            print('\nYour dice number is 2')
            print(' -----')
            print('|  •  |')
            print('|     |')
            print('|  •  |')
            print(' -----')
        elif number == 3:
            print('\nYour dice number is 3')
            print(' -----')
            print('|  •  |')
            print('|  •  |')
            print('|  •  |')
            print(' -----')
        elif number == 4:
            print('\nYour dice number is 4')
            print(' -----')
            print('| • • |')
            print('|     |')
            print('| • • |')
            print(' -----')
        elif number == 5:
            print('\nYour dice number is 5')
            print(' -----')
            print('| • • |')
            print('|  •  |')
            print('| • • |')
            print(' -----')
        else:
            print('\nYour dice number is 6')
            print(' -----')
            print('| • • |')
            print('| • • |')
            print('| • • |')
            print(' -----')
    else:
        break
