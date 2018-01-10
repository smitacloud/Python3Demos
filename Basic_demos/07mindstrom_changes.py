import turtle # check documentation

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)  # 100 steps forward
        some_turtle.right(90)  # 90 degree angle towards right
def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()# we created an instance of a class and named it as brad to draw a square
    #Turtle() inplicitly calls the init() method of Turtle class
    #lets change its shape ,color and speed
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    #lets create another instance of a class Turtle and name it angie
    angie= turtle.Turtle()

    #now i will ask angie to draw a circle
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100) #radius 100
    window.exitonclick()

#calling draw_square() function
draw_art()

'''
So here we used 2 new concepts
    class     -Turtle
    instance  -brad and angie
'''