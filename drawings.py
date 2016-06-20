import turtle

#def draw_screen():
#draw_screen()

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.color("blue")
    brad.shape("turtle")
 #   brad.speed("slowest")

    N = 1    
    for N in range(0,4):
        brad.forward(100)
        brad.right(90)
        N += 1

draw_square()
    
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.circle(100)
#    window.exitonclick()

draw_circle()

def draw_triangle():
    fred = turtle.Turtle()
    fred.shape("triangle")
    fred.right(45)
    fred.forward(100)
    fred.right(135)
    fred.forward(100)
    fred.right(110)
    fred.forward(100)
    
#    window.exitonclick()

draw_triangle()

