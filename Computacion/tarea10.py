import math
#Este programa utiliza la magnitud y direccion (angulo) de un vector para conseguir sus componentes en x y y

#calculo del vector
def convertgrados(angulo):
    return math.radians(angulo)

def calcvectorx(magnitud, angulo):
    return (magnitud*math.cos(angulo))

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
print("\nLa componente x de su vector es %5.2f " %(componentex))
print("\nLa componente x de su vector es %5.2f " %(componentey))

#despedida
print("\nGracias por usar la calculadora de vectores!!\n")

