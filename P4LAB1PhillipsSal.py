
# Saleese Phillips
# 03/19/2025
# P4Lab1
# Graphic Program - Drawing a House Shape with Loops

import turtle

win = turtle.Screen()
win.bgcolor('blue')

timmy = turtle.Turtle()
timmy.pensize(6)
timmy.pencolor('red')
timmy.shape('arrow')

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.left(90)
timmy.forward(100)
timmy.right(60)

sides = 0
while sides < 3:
    timmy.forward(100)
    timmy.right(120)
    sides += 1 