#dibujar casita

from turtle import *

speed(50)

#dibujar el cuadrado de la casa
begin_fill()
fillcolor("peachpuff")
for i in range(4):
    fd(100)
    left(90)
end_fill()

#dibujar el triangulo de la casa

pu()
goto(125,100)
pd()
begin_fill()
fillcolor("red")
lt(158.2)
fd(80)
lt(43.6)
fd(80)
lt(158.2)
fd(150)
end_fill()

pu()
goto(20,80)
pd()

#dibujo de ventanas
begin_fill()
fillcolor("paleturquoise")
for i in range(4):
    fd(20)
    rt(90)
end_fill()

pu()
goto(60,80)
pd()

begin_fill()
fillcolor("paleturquoise")
for i in range(4):
    fd(20)
    rt(90)
end_fill()

pu()
goto(45,0)
pd()

#dibujo de la puerta
begin_fill()
fillcolor("darkorange")
fd(10)
lt(90)
fd(20)
lt(90)
fd(10)
lt(90)
fd(20)
end_fill()

pu()
goto(200,200)
pd()

#dibujo del sol
begin_fill()
fillcolor("yellow")
circle(50)
end_fill()

pu()
goto(200,0)
pd()

#dibujo del tronco del arbol
begin_fill()
fillcolor("saddlebrown")
lt(90)
fd(15)
lt(90)
fd(30)
lt(90)
fd(15)
lt(90)
fd(30)
end_fill()

pu()
goto(177,60)
pd()

#dibujo de las hojas del arbol
begin_fill()
fillcolor("green")
circle(30)
end_fill()


input()