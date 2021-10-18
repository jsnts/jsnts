lista = ["paco","hugo","luis","sonia","Flora"]
promfin = 0
for elementos in lista:
    promedio = int(input("Cual es el promedio de " + elementos + ": "))
    promfin = promfin + promedio

promfin = promfin/5
print("El promedio de todos es: " + str(promfin))