from random import randint
from turtle import *
# Error because of misspelling
#prnt('hello world')

# Expressions
print((3 + 4) * (15 - 9))

print('my name is ' + 'eric')

print('meow ' * 4)

print(f'Three apples cost ${3 * 1.25}')

# Variables
name = 'Eric'

print(f'Hello, {name}')

name = 'Tom'

print(f'Hello, {name}')

score = 0

print(score + 1)

score = score + 1
score += 1

player_name = 'Eric'

print("Congratulations, " + player_name + "! Your score is " + str(score))

# Strings

score = 20
lives = 3

print(f'Score: {score} / Lives: {lives}')

#name = input('Please enter you name: ')

#print('Hello, ' + name + '!')

#age = int(input('Enter your age: '))

#old_age = age + 50

#print('In 50 years, you\'ll be ' + str(old_age))

print(len('The Mississippi River'))

print(name.upper())

print(name.lower())

print(name.capitalize())

# functions
def calculated_damage(enemy_level):
    if enemy_level < 3:
        damage = 2
    else:
        damage = 6
    return damage

boss_level = 2
damage = calculated_damage(boss_level)

print(damage)

def draw_house():
    pendown()

    # Draw a 50 x 50 square
    for i in range(0, 4):
        forward(50)
        right(90)

    # Draw the triangle
    left(180)
    forward(10)
    right(135)
    forward(50)
    right(90)
    forward(50)
    right(135)
    forward(70)

    # Go to the starting point
    right(180)
    forward(10)
    
    penup()

draw_house()
goto(100, 100)
draw_house()
goto(200, 0)
draw_house()
goto(100, -100)
draw_house()
