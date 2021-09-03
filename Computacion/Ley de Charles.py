#Autores: Regina Grimaldo (A00834044)
#Este programa calcula el volumen 1 de un gas utilizando la ley de charles

#Bienvenida
print("\nBienvenid@ a la calculadora de Ley de Charles")

#Definir calculo de temperatura de celcius a kelvin
def calculakelvin1 (temcelcius1):
    return temcelcius1 + 273

#Definir el calculo de la segunda temperatura a kelvin
def calculakelvin2 (temcelcius2):
    return temcelcius2 + 273

#Definir el calculo de la ley de charles para encontrar el volumen 1
def leydecharles (volumen2,kelvin1,kelvin2):
    return (volumen2 * kelvin1)/kelvin2

#input
print("\nPorfavor ingrese sus datos")
#Le pone variables a los inputs
temcelcius1= float(input('\nTemperatura inicial (en c°) ==>'))
temcelcius2= float(input('\nTemperatura final (en c°) ==>'))
volumen2= float(input('\nVolumen inicial ==>'))

#Imprime la temperatura 1
kelvin1= calculakelvin1(temcelcius1)
print ('\nEl valor en kelvin de la temperatura inicial es de %5.2f' %(kelvin1))

#Imprime la temperatura 2
kelvin2= calculakelvin2(temcelcius2)
print ('\nEl valor en kelvin de la temperatura final es de %5.2f' %(kelvin2))

#Imprime el volumen buscado
volumen1 = float(leydecharles(volumen2,kelvin1,kelvin2))
print('\nEl volumen final de el gas es %7.4f' %(volumen1))

#despedida
print("Gracias por utilizar la calculadora de Ley de Charles")