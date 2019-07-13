# Write program that accepts two inputs - minimum and maximum number that can be rolled.
# The program will need to print the decided number, which should be between (and also include) the min and max numbers above.
# The program should continue until the user tells it to stop.
from random import randint


def roll_a_die(name, min, max):
    print(str(name) + ' rolled a die ' + str(max) + '-sided die.')
    value = randint(int(min), int(max))
    print(value)
    go_again = input('Would you like to roll the die again? ')
    if go_again.lower() == 'yes':
        roll_a_die(name, min, max)
    else:
        print("Thanks for using Kyle's Die Rolling Simulator.")



users_name = input('What is your name? ')

min_number = input('What is the lowest number on your die? ')

max_number = input('What is the highest number on your die? ')

roll_a_die(users_name, min_number, max_number)
