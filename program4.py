#Name: Esteak Shapin #Email: esteak.shapin50@myhunter.cuny.edu
#Date: September 7, 2022
#This program draws the purina logo

import turtle

#setting up turtle
t = turtle.Turtle()

#offsetting turtle to center logo
t.penup()
t.setpos(-150, -50)
t.pendown()
t.pensize(5)
t.shape("circle")


for i in ['green', 'blue', 'lightBlue', 'red']:
    t.pencolor(i)
    for i in [300, 100, 100]:
        t.forward(i)
        t.right(90)

# keeping window open
turtle.done()