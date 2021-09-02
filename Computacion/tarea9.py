#este programa calcula las raices de una ecuacion cuadratica
#mediante la formula generla siempre y cuando sus raices sean reales

# x1 = (-b + (raiz(b^2 - 4*a*c))/2a)   x2 = (-b + (raiz(b^2 - 4*a*c))/2a)
#Para que sus raices sean reales la discrimiante debe ser mayor igual a cero

def calcdicriminante(a,b,c):
    print("Hola")
    print("Estoy calculando la discriminante de su ecuacion cuadratica")
    return (b**2) - (4*a*c)

def calculax1(a,b):
    return (-b + (disc ** 0.5)/2*a)

def calculax2(a,b):
    return (-b - (disc ** 0.5)/2*a)

print("\nBienvenido a la calculadora de ecuacionews cuadraticas")

print("\nTomando en cuenta que la ecuacion cuadratico tiene la forma")
print(" Ax^2 + Bx + C = 0   siendo A!= 0")
print("Ingresa tus valores aqui")
a = float(input("A ==> "))
b = float(input("B ==> "))
c = float(input("C ==> "))


discriminante = calcdicriminante(a,b,c)
print("El valor de tu discriminante es de %5.2f" %(discriminante))