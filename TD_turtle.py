import turtle
from turtle import circle, forward, right, left, bye, pendown, penup, pendown, goto, speed

circle(50)
right(90)
penup()
forward(25)

pendown()
forward(50)

for i in range(1,3):
    left(90)
    forward(300)
    left(90)
    forward(100)

#Exo1

def dessine(n):
    if n <= 0:
        return None
    else :
        turtle.forward(n)
        turtle.right(90)
    return dessine(n-10)

print(dessine(500))

#Exo2

def Von_Koch(n,l):
    if n == 0:
        return turtle.forward(l)
    else:
        Von_Koch(n - 1,l/3)
        turtle.left(60)
        Von_Koch(n - 1, l/3)
        turtle.right(120)
        Von_Koch(n - 1,l/3)
        turtle.left(60)
        Von_Koch(n - 1, l/3)
        
        
Von_Koch(3,100)

def Von_Koch(n,l):
    if n == 0:
        return turtle.forward(l)
    else:
        Von_Koch(n - 1,l/3)
        turtle.left(60)
        Von_Koch(n - 1, l/3)
        turtle.right(120)
        Von_Koch(n - 1,l/3)
        turtle.left(60)
        Von_Koch(n - 1, l/3)
        
def flocon (n, l):
    for i in range(3):
        Von_Koch(n,l)
        right(120)
print(flocon(4,200))

#Exo3 fractale
import math
from turtle import circle, forward, right, left, bye, pendown, penup, pendown, goto, speed

#carré simple
def carre(l):
    for i in range(4):
        forward(l)
        right(90)

def carre2(t,n):
    if n == 0:
        return None
    else:
        carre(t)
        forward(t/2)
        right(45)
        carre2(math.sqrt((t/2)**2+ (t/2)**2),n-1)
        
carre2(100,3)

