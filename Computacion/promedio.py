lista = ["paco","hugo","luis","sonia","Flora"]
promfin = 0
for elementos in lista:
    promedio = input("Cual es el promedio de " + elementos + ": ")
    promfin = promfin + int(promedio)

promfin = promfin/5
print("El promedio de todos es: " + str(promfin))