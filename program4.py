#Name: Esteak Shapin #Email: esteak.shapin50@myhunter.cuny.edu
#Date: September 7, 2022
#This program draws the purina logo

import turtle

#setting up turtle
t = turtle.Turtle()

t.pensize(5)
t.shape("circle")


for i in ['green', 'blue', 'lightBlue', 'red']:
    t.pencolor(i)
    for i in [300, 100, 100]:
        t.forward(i)
        t.right(90)
