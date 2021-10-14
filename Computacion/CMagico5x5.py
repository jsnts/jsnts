cuadroMagico = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

renglon = 0
columna = 2

numero = 1

cuadroMagico[renglon][columna] = numero

for numero in range(2,26):
    
    renglon = renglon - 1
    columna = columna + 1
    
    if (renglon < 0) and (columna > 4):  
        renglon = 1
        columna = 4
        
    elif columna > 0:  #Sali por la derecha
       columna = 0

    elif renglon < 0:    #Salida por arriba
        renglon = 6

    elif cuadroMagico[renglon][columna] != 0:  #Casilla o celda ocupada
        renglon = renglon + 2  #Ajuste de 2 porque ya habia avanzado
        columna = columna - 1 #Ajuste de 1 a la izquierda porque ya habia avanzado
    
    #Asignar el numero a la celda o casilla correspondiente al renglo columna
    cuadroMagico[renglon][columna] = numero

#Mostramos en pantalla el cuadro magico
for i in range(7):
    print(cuadroMagico[i])

