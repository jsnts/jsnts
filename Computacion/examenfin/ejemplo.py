from os import strerror


archTexto = open("BasedeDatos.txt","a")
dicc = {}
yn = "y"
i = 1
while yn != "n":
    print("\n\nBienvenido a la base de datos de productos STAR\n\n")
    print(""" 
    Que accion quiere realizar?
    1) Agregar    2) Borrar
    3) Cambiar    4) Consultar
    """)
    eleccion = int(input("Seleccion: "))
    if eleccion == 1:
        print("Usted eligio agregar un producto.")
        nbre = input("Cual es el nombre de su producto: ")
        mar = input("Cual es la marca de su producto: ")
        prc = input("Cual es el precio de su producto: ")
        if i <= 9:
            dicc["A0000" + str(i)]=[nbre, mar, prc]
        elif i >= 10 and i <= 99:
            dicc["A000" + str(i)]=[nbre, mar, prc]
        elif i >= 100 and i <= 999:
            dicc["A00" + str(i)]=[nbre, mar, prc]
        elif i >= 1000 and i <= 9999:
            dicc["A0" + str(i)]=[nbre, mar, prc]
        elif i >= 10000 and i <= 99999:
            dicc["A0" + str(i)]=[nbre, mar, prc]
        i = i+1
           


    elif eleccion == 2:
        print("Usted decidio borrar un articulo.")
        ida = input("Cual es el id de el articulo que quieres borrar: ")
        dicc.get(ida)
        dicc.pop(ida)

    elif eleccion == 3:
        print("Usted decidio cambiar un articulo.")
        print(dicc)
        idb = input("Cual es el id de su articulo: ")
        dicc.get(idb)
        nbre2 = input("Cual es el nuevo nombre: ")
        mar2 = input("Cual es la nueva marca del producto: ")
        prc2 = input("Cual es el nuevo precio del producto: ")
        dicc[idb]=[nbre2, mar2, prc2]
        print(dicc)
    
    elif eleccion == 4:
        print("Usted eligio consultar un producto.")
        print(dicc.keys())
        idc = input("Cual es la clave del prodcuto que quiere consultar: ")
        print(dicc.get(idc))



    yn = input("Quiere hacer algo mas (y/n): ")
archTexto.write(str(dicc))
archTexto.close()

print(dicc)
    
