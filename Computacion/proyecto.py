#Este es el proyecto final de Jair Santos y Bruno Marquez
archTexto = open("proyecto.txt","r")
#Aqui esta leyendo el archivo de texto para ver los ejercicios
ejercicioesp1 = archTexto.read(832)
diccesp = {}
sn = "s"


#Este es el menu de eleccion
print("\n\nBienvenido al programa de ENTRENAMIENTO PARA EL EXAMEN PISA!!\n\n")
while sn != "n":
    print("Puedes elegir de los siguientes temas cual quieres estudiar: \n")
    print("""

1)Matematicas       2)Ciencias      
3)Español           4)Salir

""")



#Esta seccion es la de mate
    menu = input("Seleccion: ")
    if int(menu) == 1:
        print("Usted eligio la modalidad de Matematicas")
        sn = input("Quieres seguir estudiando (s/n): ")




#Esta seccion es la de ciencias
    elif int(menu) == 2:
        print("Usted eligio la modalidad de Ciencias")
        sn = input("Quieres seguir estudiando (s/n): ")





#Esta seccion es la de español        
    elif int(menu) == 3:
        print("Usted eligio la modalidad de Español\n")
        print("A continuacion le van a aparecer diferentes ejercicios de lectura y español vas a tener que responder.\n")
        print(ejercicioesp1)
        espa1 = input("\nRespuesta a la pregunta 1: ")
        if espa1 == "b" or espa1 == "B":
            print("\nLa primer pregunta te la sacaste bien!!")
        else:
            print("\nUy, te la sacaste mal.")
        espa2 = input("\nRespuesta a la pregunta 2: ")
        if espa2 == "a" or espa2 == "A":
            print("\nLa segunda pregunta te la sacaste bien!!")
        else:
            print("\nUy, te la sacaste mal.")
        espa3 = input("\nRespuesta a la pregunta 3: ")
        if espa3 == "c" or espa3 == "C":
            print("\nLa tercer pregunta te la sacaste bien!!")
        else:
            print("\nUy, te la sacaste mal.")
        espa4 = input("\nRespuesta a la pregunta 4: ")
        if espa4 == "a" or espa4 == "A":
            print("\nLa cuarta pregunta te la sacaste bien!!")
        else:
            print("\nUy, te la sacaste mal.")
        espa5 = input("\nRespuesta a la pregunta 5: ")
        if espa5 == "b" or espa5 == "B":
            print("\nLa quinta pregunta te la sacaste bien!!")
        else:
            print("\nUy, te la sacaste mal.\n")
        print("*"*60)
        print("\nA continuacion te va a aparecer un ejercicio de español ")
        
        archTexto.seek(854)
        ejercicioesp2 = archTexto.read(566)
        print(ejercicioesp2)
        archTexto.seek(1438)
        ejercicioesp2p = archTexto.readlines()
        for elementos in ejercicioesp2p:
            print(elementos)
            for letras in elementos[0]:
                respuesta = input("Esta es c o p: \n")
                if respuesta == "c":
                    if letras.islower():
                        print("\nTe la sacaste bien!!\n")
                    elif letras.isupper():
                        print("\nUy, te la sacaste mal.\n")
                elif respuesta == "p":
                    if letras.isupper():
                        print("Te la sacaste bien!!\n")
                    elif letras.islower():
                        print("\nUy, te la sacaste mal.\n")

        sn = input("Quieres seguir estudiando (s/n): ")

    #Esta seccion aplica la accion de salir
    elif int(menu) == 4:
        print("Espero que tengas un buen dia, gracias por usar el programa!!")
        sn = "n"
    else:
        print("\n\nNo elegiste ninguna modailidad, porfavor eliga otra vez.\n\n")

archTexto.close()