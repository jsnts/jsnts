print("Buenas tardes, los paquetes de cables son estos: Basico $150, Familia $350, Premium $600")
cap_ventas=0
men="yes"
yn= "y"
art1 = 0
art2 = 0
art3 = 0
while men != "end":
    print("""
Bienvenido al menu de opciones
1)Capturar ventas
2)Revision de quejas
3)Mostrar total de ventas
4)Salir
""")
    men1=int(input(""))
    if men1 == 1:
        print("Ha seleccionado captura de ventas")
        while yn != "n":
            print("Cual paquete quiere registrar: ")
            print("""
            a)Basico   b)Familiar   c)Premium   d)Terminar"""
            )
            paq_basic = 150
            paq_fam = 350
            paq_prem = 600
            seleccion = input("Seleccion: ")
            if seleccion == "a":
                cap_ventas = cap_ventas + paq_basic
                art1= art1+1
            elif seleccion == "b":
                cap_ventas = cap_ventas + paq_fam
                art2= art2+1
            elif seleccion == "c":
                cap_ventas = cap_ventas + paq_prem
                art3= art3+1
            elif seleccion == "d":
                print("Decidio terminar su registro de ventas y se guardaron las ventas anteriores.")
                yn = "n"
            else:
                print("No selecciono ningun paquete.")
    elif men1 == 2:
        print("Ha seleccionado revision de quejas")
    elif men1 == 3:
        print("Ha seleccionado mostrar total de ventas")
        print("Este es el total de ventas: " + cap_ventas)
        print("El numero de paquetes basicos es: " + art1)
        print("El numero de paquetes familiares es: " + art2)
        print("El numero de paquetes premium es: " + art3)
        print("La venta total de paquetes basicos fue de: " + (art1*150))
        print("La venta total de paquetes familiares fue de: " + (art2*350))
        print("La venta total de paquetes premium fue de: " + (art3*600))
        print("La numero total de paquetes fue de: " + (art1+art2+art3))
        if cap_ventas > 2000:
            print("Vamos bien")
        elif cap_ventas > 5000:
            print("Felicidades, lo estas logrando.")
    elif men1 <= 0 or men1 < 4:
        print("No ha seleccionado el numero correcto")

    elif men1 == 4:
        print("Ha seleccionado Salir")
        men="end"