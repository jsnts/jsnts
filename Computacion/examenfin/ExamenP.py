#Jair SAntos A01026654
#Este programa calcula tu imc las calorias necesarias para una persona y la cantidad de agua diaria necesaria para una persona

#definimos el calculo de las calorias

def calcCaloriasH(edad, peso, altura):
    return (66.5 + 13.75 * float(peso) + 5 * float(altura) - 6,775 * float(edad))

def calcCaloriasF(edad, peso, altura):
    return (655.1 + 9.56 * float(peso) + 1.85 * float(altura) - 4,766 * float(edad))

#definimos el calculo del IMC
def IMC(peso, altura):
    return (int(peso)/((int(altura)/100)*(int(altura)/100)))

#definir cantidad de agua
def cantAgua(peso):
    return (0.03 * float(peso))

#saludo
print("\n****************************************")
print("\nBienvenido a tu calculadora nutricional")
print("\n****************************************")
print("\nSelecciona una opcion")
print("""

    1) Calcular las calorias diarias necesarias para una persona

    2) Calcular el IMC de una persona

    3) Calcular la cantidad de agua diaria necesaria para una persona

    4) Salir""")
opcion = input("\n")
#seleccion de opcion

#Calorias
if opcion == "1":
    print("\nCual es su sexo? H/F")
    sexo = input("\n")
    if sexo == "H":
        print("\nCual es su edad?")
        a = input("\n")
        print("\nCual es su peso en Kgs?")
        b = input("\n")
        print("\nCual es su altura en cm?")
        c = input("\n")
        caloriasH = calcCaloriasH(a, b, c)
        print("\nSus calorias necesarias son: " + str(caloriasH))
        print("\nGracias por utilizar la calculadora nutricional!!")
    elif sexo == "F":
        print("\nCual es su edad?")
        a = input("\n")
        print("\nCual es su peso en Kgs?")
        b = input("\n")
        print("\nCual es su altura en cm?")
        c = input("\n")
        caloriasF = calcCaloriasF(a, b, c)
        print("\nSus calorias necesarias son: " + str(caloriasF))
        print("\nGracias por utilizar la calculadora nutricional!!")

#IMC
if opcion == "2":
        print("\nCual es su peso en Kgs?")
        a = int(input("\n"))
        print("\nCual es su altura en cm?")
        b = int(input("\n"))
        imc = IMC(a,b)
        print("\nSu imc es: " + str(imc))
        print("\nGracias por utilizar la calculadora nutricional!!")
    
#Agua
if opcion == "3":
    print("\nCual es su peso en Kgs?")
    a = input("\n")
    agua = cantAgua(a)
    print("\nSus calorias necesarias son: " + str(agua))
    print("\nGracias por utilizar la calculadora nutricional!!")

#salir
if opcion == "4":
    print("\nGracias por utilizar la calculadora nutricional!!")

