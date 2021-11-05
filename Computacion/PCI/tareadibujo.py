from turtle import *

speed(100)

def mover(x,y):
    pu()
    goto(x,y)
    pd()

def dib_pol(lados,tamaño,pluma,relleno):
    pencolor(pluma)
    begin_fill()
    fillcolor(relleno)
    for i in range(lados):
        fd(tamaño)
        lt(360/lados)
    end_fill()

def dib_circulo(tamaño,pluma,relleno):
    pencolor(pluma)
    begin_fill()
    fillcolor(relleno)
    circle(tamaño)
    end_fill()

def dib_rec(tamaño1,tamaño2,pluma,relleno):
    pencolor(pluma)
    begin_fill()
    fillcolor(relleno)
    for i in range(2):
        fd(tamaño1)
        lt(90)
        fd(tamaño2)
        lt(90)
    end_fill()

mover(-100,-100)

dib_pol(8,150,"saddlebrown","saddlebrown")

mover(-60,-50)

dib_rec(80,20,"black","black")

mover(-30,-50)

dib_rec(20,40,"red","red")


input()