import turtle, random

turtle.delay(0)

tortue = turtle.Turtle()
"""
1

tortue.forward(50)
tortue.left(90)
tortue.forward(50)
tortue.left(90)
tortue.forward(50)
tortue.left(90)
tortue.forward(50)
tortue.circle(50)

2

 
for i in range (500):

    i=i+5
    tortue.forward(i)
    tortue.left(90)



i=0
tortue.speed(115)
while True:
    i+=2
    tortue.circle(i,i,i)




3

tortue.speed(115)
while True:
    i= random.randint(1,3)
    if i==1:
        i= tortue.left(90)
    elif i==2:
        i=tortue.forward(1)
    else:
        i=tortue.right(90)       



"""
4
""
n=8
listetortue=[]


for i in range(n):
    newTortue = turtle.Turtle()
    listetortue.append(newTortue)
    newTortue.penup()
    newTortue.pensize(2)
    newTortue.shape('turtle')
    shape= random.randint(1,5)
    newTortue.shapesize(shape,shape)
    newTortue.color(1,0,0)
    newTortue.speed(10)
    newTortue.setposition(random.randint(-400,400),random.randint(-400,400))
    newTortue.color(random.random(),random.random(),random.random())
    directions = [0,90,180,270]

    i=0
 
while True:
    for i in listetortue:
        i.setheading(random.choice(directions))
        i.forward(20)

        for i in listetortue:
            for j in listetortue:
                if i.distance(j) <= (i.shapesize()[0] +  j.shapesize()[0])*5:
                    if i != j:
                        if i.shapesize()[0] >= j.shapesize()[0]:
                            print("ok")
                            i.shapesize(   i.shapesize()[0] + j.shapesize()[0] ,   i.shapesize()[0] + j.shapesize()[0]  )
                            j.ht()
                            listetortue.remove(j)
