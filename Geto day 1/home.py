from turtle import *


#we want to paint a house

#step 1: draw a square
speed(20)
width(7)
color("pink")
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("purple")

left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
    #height of the door

penup()
goto(200, 200)
pendown

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


left(90)
forward(90)


color("red")
pendown()


left(120)
forward(30)

left(90)
forward(50)


left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(20)

penup()

right(90)
forward(100)

pendown()
left(90)
forward(30)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(20)




exitonclick()