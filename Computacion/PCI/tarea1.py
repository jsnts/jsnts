#Jair Santos A01026654
#Ricardo Gaytán A00829872
#Emilio Flores A01571179

#Saludo
print("Hola, espero que hoy estes bien!!")

#Ingresar datos
print("Me podrias decir tu peso?")
peso = float(input())
print("Muchas gracias, ahora me puedes decir tu estatura en metros?")
estatura = float(input())
imc = peso/(estatura * estatura)

#Resultados
if (imc < 18.5):
    print("Tu tienes una insuficiencia nutrimental deberias comer mejor y poner.")
elif (imc < 24.9):
    print("Usted esta en buena condicion siga asi y procure no subir de peso.")
elif (imc < 29.9):
    print("Usted esta en sobrepeso le recomiendo ponerse a dieta y empezar a ejercitarse un poco.")
elif (imc > 30.0):
    print("Usted tiene obesidad lo recomendable es ponerse en una dieta para enflacar rapidamente y hacer ejercicio regularmente.")