#Name: Esteak Shapin
#Email: esteak.shapin50@myhunter.cuny.edu
#Date: September 7, 2022
#This program draws a dodecagon

import turtle

t = turtle.Turtle()

#number of sides
n = 12

#size of sides
size = 50

#angle
angle = 180 - 150

for i in range(n+1):
    t.forward(size)
    t.left(angle)

#keeping the window open
turtle.done()