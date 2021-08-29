#saludo
print("Hola lindo dia!")

#preguntar nombre
print("Como te llamas?")
nombre = str(input())
print("Gusto en conocerte " + nombre)

#preguntar edad
print("Cuantos años tienes?")
edad = int(input())

#verificar edad
if (edad > 11) and (edad <= 60):
    print("Tu tienes que pagar boleto completo")
elif (edad <= 11):
    print("Tu pagas medio boleto") 
else:
    print("Tu entras gratis y recibe souvenir")