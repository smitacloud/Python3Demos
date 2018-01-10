import turtle # check documentation

def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()# we created an instance of a class and named it as brad to draw a square
    #Turtle() inplicitly calls the init() method of Turtle class

    #lets change its shape ,color and speed
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    brad.forward(100)#100 steps forward
    brad.right(90)#90 degree angle towards right

    brad.forward(100)  # 100 steps forward
    brad.right(90)  # 90 degree angle towards right

    brad.forward(100)  # 100 steps forward
    brad.right(90)  # 90 degree angle towards right

    brad.forward(100)  # 100 steps forward
    brad.right(90)  # 90 degree angle towards right

    #lets create another instance of a class Turtle and name it angie
    angie= turtle.Turtle()

    #now i will ask angie to draw a circle
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100) #radius 100
    window.exitonclick()

#calling draw_square() function
draw_square()


#Question : why the above code quality will upset the Computer Science Professor
''' move forward ...turn right....many times instead using any loops

secondly my function name is draw_sqaure and we are drawing circle too'''
