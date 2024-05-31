from turtle import *
#we want to build a house

#step 1 draw a square

color("dark red")
width(5)
forward(200)

left(90)
forward (200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(60)
#end of square

#making a door

color("blue")
left(90)
forward(90)

right(90)
forward(50)

right(90)
forward(90)
#end of making a door

penup()
goto(200, 200)
pendown()

#making a roof 

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

exitonclick()