#Jair Santos A01026654
#Ricardo Gaytán A00829872
#Emilio Flores A01571179

#aqui estoy importando la biblioteca de mates
import math

#saludo y preguntar que figura es
print("Hola, que figura quiere verificar?")
print(""" 
1)Triangulo Equilatero   2)Cuadrado
3)Circulo     4)Rectangulo
""")
fig = input()

#los calculos de las figuras

#calculo del triangulo
if int(fig) == 1:
    print("Cuales son las medidas en metros?")
    base1 = float(input("Base: "))
    altura2 = float(input("Altura: "))
    area1 = base1 * altura2
    print("Perfecto, su area es: " + str(area1/2) + ". y su perimetro es: " + str(base1 + base1 + base1))

#calculo del cuadrado
elif int(fig) == 2:
    print("Cuales son las medidas en metros?")
    lado2 = float(input("Lado: "))
    area2 = lado2 * lado2
    print("Perfecto, su area es: " + str(area2) + ". y su perimetro es: " + str(lado2 * 4))

#calculo del circulo
elif int(fig) == 3:
    print("Cuales son las medidas en metros?")
    radio3 = float(input("Radio: "))
    area3 = math.pi * (radio3 * radio3)
    circum3 = math.pi * (2 * radio3)
    print("Perfecto, su area es: " + str(area3) + ". y su circunferencia es: " + str(circum3))

#calculo del rectangulo
elif int(fig) == 4:
    print("Cuales son las medidas en metros?")
    base4 = float(input("Base: "))
    altura4 = float(input("Altura: "))
    area4 = base4 * altura4
    perim4 = (base4 * 2)+ (altura4 * 2)
    print("Perfecto, su area es: " + str(area4) + ". y su perimetro es: " + str(perim4))