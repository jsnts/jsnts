#Muestra el funcionamiento de la tortuga en python

from turtle import * 

#dibuja un cuadrado
for i in range(4):
    fd(50)
    lt(90)


#mueve la coordenada 100,100
pu()#levanta la pluma
goto(100,100)
pd()



#dibuja un triangulo equilatero
for i in range(3):
    fd(100)
    rt(120)



#mueve a la coordenada (-150,150)
pu()
goto(-150,150)
pd()

#dibuja un circulo
begin_fill()
fillcolor("cyan")
circle(100)
end_fill()


#dibuja un hexagono
for i in range(6):
    fd(100)
    lt(360/6)

#mueve a coordenada (150,150)
pu()
goto(150,150)
pd()

#dibuja una estrella
for i in range(5):
    fd(100)
    lt(720/5)
input()