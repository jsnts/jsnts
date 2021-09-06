import math
#Este programa utiliza la magnitud y direccion (angulo) de un vector para conseguir sus componentes en X y Y

#convertir de grados a radianes
def convertgrados(angulo):
    return math.radians(angulo)

#calcular el componente x
def calcvectorx(magnitud, angulo):
    return (magnitud*math.cos(angulo))

#calcular el componente y
def calcvectory(magnitud, angulo):
    return (magnitud*math.sin(angulo))


#saludo
print("\n\nBienvenido a la calculadora de vecotres!!")
print("\nMe podrias decir la magnitud de tu vector y su angulo?")
a = float(input("\nMagnitud: "))
b = int(input("\nAngulo: "))

angulorad = convertgrados(b)
componentex = calcvectorx(a,angulorad)
componentey = calcvectory(a,angulorad)

#output
print("\nLa componente X de su vector es %5.2f " %(componentex))
print("\nLa componente Y de su vector es %5.2f " %(componentey))

#despedida
print("\nGracias por usar la calculadora de vectores!!\n")

