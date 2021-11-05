cuadroMagico = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

n = input("De cuantos numeros quiere su cuadro magico: ")

renglon = 0
columna = 2

numero = 1

cuadroMagico[renglon][columna] = numero

if n % 2 == 0:
    print("El cuadro magico no se puede hacer para numeros pares.")

else:
    for numero in range(2, n*n+1):

        renglon = renglon - 1
        columna = columna + 1

        if (renglon < 0) and (columna > n-1):
            renglon = 1
            columna = n-1
        
        elif columna > n-1:
            columna = 0
    
        elif renglon < 0:
            renglon = n-1
    
        elif cuadroMagico[renglon][columna] != 0:
            renglon = renglon + 2
            columna = columna - 1
    
    cuadroMagico[renglon][columna] = numero


for i in range(n):
    print(cuadroMagico[i])