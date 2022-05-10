import random 
#Establece la clase jugador junto con nombre, el tiro del dado y la posición
#También hacemos un metodo que sume la posición con cuanto sale del dado para tener posición al final del turno
class Jugador():
    def __init__(self,name):
        self.name=name
        self.pos = 1
    def roll(self):
        return random.randint(1,6)
  
    def turno(self):
        return self.pos+self.roll()

#Se pone el número de casillas que va a haber y se mezclan
class Tablero(Jugador):
    def __init__(self):

        self.Casillas = ["C"] * 30
        self.Serpientes = ["S"] * 3
        self.Escaleras = ["L"] * 3
    def crear(self):
        self.crear=self.Casillas+self.Serpientes+self.Escaleras
        x = random.shuffle(self.crear)
        return x




class snakesnladder(Tablero):
    def __init__(self,x,y):
        self.j1 = Jugador(x)
        self.j2 = Jugador(y)
    def jugar(self):
        while True:
            decision=input("Presiona C para continuar con el siguiente turno o T para terminar el juego: \n")
            if (decision==("T") or decision==("t")):
                print("-- GAME OVER -- \n ¡Gracias por jugar!!! \n")
                break
            elif (decision==("C") or decision==("c")):
                i=1
                if i%2!=0:
                    #p es posición inicial
                    p=self.j1.pos
                    #p es la posición con el tiro del dado
                    np=self.j1.turno()
                    #d es cuanto salió del dado
                    d=np-p
                    #t es el tipo de casilla en el que cayó
                    tp=p-1
                    t=self.crear
                    #Condiciones de casillas
                    if t=="L":
                        np+=3
                        return np
                    elif t=="S":
                        np-=3
                        return np
                    if np <1:
                        np=1
                        return np
                    #fp es la posición final del jugadores
                    fp=np
                    print(i,p,d,t,fp)
                    if fp>=30:
                        print("¡Jugador 1 es el ganador!!!\n")
                        break

                elif i%2==0:
                    #p es posición inicial
                    p=self.j2.pos
                    #p es la posición con el tiro del dado
                    np=self.j2.turno()
                    #d es cuanto salió del dado
                    d=np-p
                    #t es el tipo de casilla en el que cayó
                    tp=p-1
                    t=self.crear
                    #Condiciones de casillas
                    if t=="L":
                        np+=3
                        return np
                    elif t=="S":
                        np-=3
                        return np
                    if np <1:
                        np=1
                        return np
                    #fp es la posición final del jugadores
                    fp=np
                    print(i,p,d,t,fp)
                    if fp>=30:
                        print("¡Jugador 2 es el ganador!!!\n")
                        break
            else:
                print("Opción invalida, por favor presiona C para continuar con el siguiente turno o T para terminar el juego:\n")

    

def main():

    j1 = input("Nombre jugador 1:")
    j2 = input("Nombre jugador 2:")

    Juego = snakesnladder(j1,j2)
    Juego.jugar()


main()