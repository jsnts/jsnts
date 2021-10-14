#Jair Santos A01026654

#Este programa calcula el promedio de 5 personas
print("\nBienvendio a la calculadora de promedios!!")
suma = 0
for persona in ("Dany", "Hugo", "Katy", "Luis", "Paco"):
    calificacion = int(input("Ingresa la calificacion de " + persona + ":"))
    suma = suma + calificacion 

promedio = suma/5
print("El promedio de calificaion es: " + str(promedio))