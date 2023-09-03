import random

n = 20
random_value = int(n * random.random()) + 1
attempts = 0

while True:
    user_input = int(input('Input your Number = '))

    if user_input == 0:
        print('Input cannot be zero')
    elif user_input > 20:
        print('Try a number lower than 20')
    elif user_input < random_value:
        print('Try a higher number')
        attempts += 1
    elif user_input > random_value:
        print('Try a lower number')
        attempts += 1
    else:
        attempts += 1
        print(f'CONGRATS! You guessed the number {random_value} in {attempts} attempts.')
        break