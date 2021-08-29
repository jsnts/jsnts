import math
#calcula la posicion y velocidad de un objeto en caida libre

#Bienvinida al usuario
print("Hola, buen dia!")

#Pedir la altura
print("Cual es la altura de su objeto?")
altura = float(input("\nAltura: "))

#gravedad
g = -9.81
#Calculamos el tiempo de caida
tiempoCaida = ((-2 * altura/g) ** 0.5)

#Mostrar el tiempo de caida
print("\nTiempo de caida del objeto: %5.4f" %(tiempoCaida))

#Mostrar segundo a segundo su posicion y velocidad
tmpoCaidaEnt = int(tiempoCaida)

print("*" * 46)
print("    Tiempo       Altura      Velocidad")
print("_" * 46)

for t in range(tmpoCaidaEnt + 1):
    vf = g * t
    pos = altura + (0.5 * g * (t**2))
    print("%7.0f        %7.4f       %7.4f" %(t,pos,vf))

#despedida

print("Que tengas un buen dia!!")