#Este codigo da los numeros primos de una serie de numeros
print("Cuantos numeros primos quiere enseñar: ")
veces = int(input(""))

a = 0
num=0
while a == veces:
    a = a + 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
    num = num + 1


print("se acabo")