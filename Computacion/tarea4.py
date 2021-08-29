#Este programa muestra como funciona for
total = 0

#ejectua 10 veces el ciclo
for num in range(10):
    total = total + num
    #muestra los valores
    print("num: " + str(num) + "       total: " + str(total))

print("Sali del ciclo y los valores de num y total son: ")
print("num: " + str(num))
print("total: " + str(total))

print("\n\n2a modalidad")

for num in range(1,5):
    total = total + num
    #muestra los valores
    print("num: " + str(num) + "       total: " + str(total))

print("Sali del ciclo y los valores de num y total son: ")
print("num: " + str(num))
print("total: " + str(total))

print("\n\n3a modalidad")
for num in range(1,100,5):
    total = total + num
    #muestra los valores
    print("num: " + str(num) + "       total: " + str(total))

print("Sali del ciclo y los valores de num y total son: ")
print("num: " + str(num))
print("total: " + str(total))