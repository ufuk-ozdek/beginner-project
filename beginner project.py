import random

'''
x = random.randrange(0,101)
guess = int(input('> '))
while True:
    if x > guess and guess in range(101):
        print('HIGHER')
        guess = int(input('> '))
    elif guess > x and guess in range(101):
        print('LOWER')
        guess = int(input('> '))
    elif guess == x:
        print('Congratulations! Answer is ' + str(x))
        break
    else:
        print('Invalid Value')
        guess = int(input('> '))
'''


maxi = int(input('max: '))
mini = int(input('min: '))

x = random.randrange(mini,maxi+1)

# you have 7 chance to find the number
guess = int(input('> '))
i = 0
while i < 7:
    i += 1
    if i == 7 :
        print('YOU FAILED :( ANSWER WAS ' + str(x))
        break
    if guess == x:
        print('Congratulations! Answer is ' + str(x))
        break
    elif guess < x and guess > mini :
        print('HIGHER')
        guess = int(input('> '))
    elif guess > x and guess < maxi :
        print('LOWER')
        guess = int(input('> '))
    else:
        print('Invalid Value')
        guess = int(input('> '))


else:
    print('YOU FAILED :( ANSWER WAS ' + str(x))

