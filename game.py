import turtle
import * from random

def game():
#code to beautify the screen of the turtle window
    window = turtle.Screen() #create a screen pointer named window
    window.bgcolor("Ivory")#setting the background color of window as navajo white


    #code for building the race track
    racetrack = turtle.Turtle()
    racetrack.speed(100)
    racetrack.pencolor('Black')
    racetrack.penup()
    racetrack.goto(-200,200)

    for track in range(21):
        racetrack.write(track,align = 'center')
        racetrack.right(90)
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.pendown()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.forward(10)
        racetrack.penup()
        racetrack.backward(210)
        racetrack.left(90)
        racetrack.forward(20)


    #add the animals in the racing track
    turtle_1 = turtle.Turtle()
    turtle_1.color('red')
    turtle_1.shape('turtle')
    turtle_1.penup()
    turtle_1.goto(-200,180)
    turtle_1.pendown()
    turtle_1.right(360)


    turtle_2 = turtle.Turtle()
    turtle_2.color('blue')
    turtle_2.shape('turtle')
    turtle_2.penup()
    turtle_2.goto(-200,150)
    turtle_2.pendown()
    turtle_2.right(360)



    turtle_3 = turtle.Turtle()
    turtle_3.color('green')
    turtle_3.shape('turtle')
    turtle_3.penup()
    turtle_3.goto(-200,120)
    turtle_3.pendown()
    turtle_3.right(360)


    turtle_4 = turtle.Turtle()
    turtle_4.color('yellow')
    turtle_4.shape('turtle')
    turtle_4.penup()
    turtle_4.goto(-200,90)
    turtle_4.pendown()
    turtle_4.right(360)


    turtle_5 = turtle.Turtle()
    turtle_5.color('indigo')
    turtle_5.shape('turtle')
    turtle_5.penup()
    turtle_5.goto(-200,60)
    turtle_5.pendown()
    turtle_5.right(360)



    for turn in range(150):
        turtle_1.forward(randint(1, 5))
        turtle_2.forward(randint(1, 5))
        turtle_3.forward(randint(1, 5))
        turtle_4.forward(randint(1, 5))
        turtle_5.forward(randint(1, 5))
#conditional statements to find out the winnerof the turtle race
        if turtle_1.xcor() >= 200:
            break
        elif turtle_2.xcor() >= 200:
            break
        elif turtle_3.xcor() >= 200:
            break
        elif turtle_4.xcor() >= 200:
            break
        elif turtle_5.xcor() >= 200:
            break


    window.exitonclick()


if __name__ == '__main__':
    game()
