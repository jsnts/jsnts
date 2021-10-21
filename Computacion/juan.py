import numpy as np
def matriz(pE, neu):
    peso = np.zeros((neu,neu))
    for i in range(neu):
        for j in range(neu):
            suma = 0
            for k in range(len(pE)):
                suma += pE[k][i]*pE[k][j]
            peso[i][j] = 1/neu*suma
    return peso

matriz([[-1,1,-1],[1,1,1],[-1,-1,-1],[1,-1,1],[1,1,-1]],3)

