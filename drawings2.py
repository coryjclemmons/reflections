import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.color("blue")
    brad.shape("turtle")
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)

#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.circle(100)

    window.exitonclick()

draw_art()
