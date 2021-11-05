from turtle import * 

speed(5)

shape("turtle")


def muevete(x, y):
    pu()
    goto(x, y)
    pd()

def dibuja_estrella(tamaño):
    for i in range(5):
        fd(tamaño)
        lt(720/5)


def dibuja_poligono(lados,tamaño,pluma):
    pencolor(pluma)
    for i in range(lados):
        fd(tamaño)
        lt(360/lados)



muevete(-200,100)

dibuja_poligono(4,100,"blue")

muevete(100,200)

dibuja_estrella(300)

muevete(-200,-300)

dibuja_poligono(3,40,"pink")

muevete(200,-100)

dibuja_poligono(7, 20, "green")


input()