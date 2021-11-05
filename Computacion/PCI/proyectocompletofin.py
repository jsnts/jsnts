#Este es el proyecto final de Jair Santos A01026654 y Bruno Marquez A01361417
from os import close


archTexto = open("proyecto.txt","r")
#Aqui esta leyendo el archivo de texto para ver los ejercicios
ejercicioesp1 = archTexto.read(832)
sentidos = {}
sn = "s"
solido = {}
liquido = {}
gas = {}

#Este es el menu de eleccion
print("\n\nBienvenido al programa de ENTRENAMIENTO PARA EL EXAMEN PISA!!\n\n")
while sn != "n": #Aqui hacemos un while si o no
    print("Puedes elegir de los siguientes temas cual quieres estudiar: \n")
    print("""

1)Matematicas       2)Ciencias      
3)Español           4)Salir

""")



    #Esta seccion es la de mate
    menu = input("Seleccion: ")
    if int(menu) == 1:
        print("Elegiste la modalidad de Matematicas")
        print("Usted eligio la modalidad de Matematicas")
        acmat=['Seleccionar un tema','Buscar un tema','Retroceder']
        print(acmat)
        elmat=str(input('¿Qué desea hacer?')) #Aqui puedes seleccionar entre tres opciones
        if elmat in ['Seleccionar un tema','seleccionar un tema','seleccionar','selecc']:
            print('Ha elegido "Seleccionar un tema"') 
            print('Éstos son los temas a repasar:')
            tmat={'Numero':'Lee, escribe y ordena números naturales hasta 1 000',
            'Adición y sustracción':'Resuelve problemas de suma y resta con números naturales hasta 1 000.',
            'Multiplicación y división':'Resuelve problemas de multiplicación con números naturales menores que 10.'}
            print(tmat)
            tael=str(input('¿Qué tema desea ver?')) #Aqui puedes elegir entre los tres temas que hay
            while True:
                tael=str(input('¿Qué tema desea ver?')) #Suma y resta
                if tael in ['suma y resta','Suma y Resta','Adición y Sustracción','adición y sustracción','adicion y sustraccion']:
                    print('Adición y Sustracción')
                    print('Conceptos:')
                    concm=['Adición: operación matemática de composición que consiste en combinar o añadir dos números o más para obtener una cantidad final',
                    'Sustracción: Consiste en restar una cantidad (el sustraendo) de otra (el minuendo) para averiguar la diferencia entre las dos']
                    print(concm)
                    print('A continuación se veremos ejemplos de Suma y resta de cantidades menores a 1000')
                    print('Ejemplo 1:')
                    print('3+7=10')
                    print('7-3=4')              #Aqui esta la explicacion de suma y resta
                    print('3+30=33')
                    print('67-14=53')
                    ot=str(input('¿Hacemos ejercicios?'))
                    while ot in ['Si','si','Sí','sí']:
                        if ot in ['si','Si','Sí','sí']:
                            print('1)')
                            print('A 51 Réstale 17')
                            ans=float(input())
                            while ans != 34:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans=float(input())
                            if ans ==34:
                                print('Respuesta correcta')
                            print('2)')
                            print('A 43 réstale 27:')
                            ans2=float(input())
                            while ans2 != 16:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans2=float(input())                       
                            if ans2 ==16:
                                print('Respuesta correcta')
                            print('3)')                                         #Aqui estan los ejercicios de suma y resta
                            print('A 15 súmale 2')
                            ans3=float(input())
                            while ans3 != 17:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans3=float(input())                       
                            if ans3 ==17:
                                print('Respuesta correcta')
                            print('4)')
                            print('A 65 súmale 17')
                            ans4=float(input())
                            while ans4 != 82:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans4=float(input())                       
                            if ans4 ==82:
                                print('Respuesta correcta')
                            ot=str(input('¿Hacemos ejercicios?'))
                            print('Has concluido todos los ejercicios con éxito!') 
                                    
                    print('De acuerdo, volvamos al inicio')
                    break
                elif tael in ['Numero','Número','numero','número','NÚMERO','NUMERO']: #Como se escriben los numeros y su orden
                    print('Número')
                    print('Conceptos:')
                    concm=['Número: Es una cantidad que tiene un valor',
                    'Orden: Ajustar números de acuerdo a ciertas indicaciones']
                    print(concm)
                    print('A continuación se veremos ejemplos de números, como ordenarlos y leerlos')
                    print('Ejemplos:')
                    print('120')
                    print('Se lee: Ciento veinte')
                    paus12=str(input('¿continuamos?'))
                    print('Ordenar los números de mayor a menor:')          #Esta es la explicacion de los numeros en orden y como se escriben
                    print('9-6-10-2-5')
                    print('Respuesta: 10-9-6-5-2')
                    paus13=str(input('¿continuamos?'))
                    print('Ordenar los números de menor a mayor:')
                    print('9-6-10-2-5')
                    print('Respuesta: 2-5-6-9-10')
                    ot=str(input('¿Hacemos ejercicios?'))
                    while ot in ['Si','si','Sí','sí']:
                        if ot in ['si','Si','Sí','sí']:
                            print('1)')
                            print('Escribe el número 19')
                            ans=str(input())
                            while ans not in ['diecinueve','Diecinueve']:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans=str(input())
                            if ans in ['diecinueve','Diecinueve']:
                                print('Respuesta correcta')
                            print('2)')
                            print('Ordena los números de mayor a menor, anótalos seguidos,Ejemplo: 1234')
                            print('4,5,6,8,9')
                            ans2=float(input())
                            while ans2 != 98654:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans2=float(input())                       
                            if ans2 ==98654:
                                print('Respuesta correcta')
                            print('3)')                                     #Aqui estan los ejercicios de orden de numeros y como se escriben
                            print('Escribe el número 20')
                            ans3=str(input())
                            while ans3 not in  ['Veinte','veinte']:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans3=str(input())                       
                            if ans3 in ['Veinte','veinte']:
                                print('Respuesta correcta')
                            print('4)')
                            print('Ordena los números de menor a mayor,anótalos seguidos,Ejemplo: 1234')
                            print('9,8,3,4,1')
                            ans4=float(input())
                            while ans4 !=13489:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans4=float(input())                       
                            if ans4 ==13489:
                                print('Respuesta correcta')
                            ot=str(input('¿Hacemos ejercicios?'))
                            print('Has concluido todos los ejercicios con éxito!')
                                     
                    print('De acuerdo, volvamos al inicio')
                    break
                elif tael in ['multiplicacion y division','Multiplicacion y Division','multiplicación y división','Multiplicación y división']: #Aqui es multiplicar y dividir
                    print('Multiplicación y División')
                    print('Conceptos:')
                    concm=['Multiplicación: Multiplicar es lo mismo que sumar varias veces el mismo número',
                    'División: Óperación que nos enseña a repartir en partes iguales cierta cantidad. La división es una operación matemática y es lo contrario a la multiplicación.',
                    'División impropia: división en la cual el numero que dividimos es mayor que o igual al número por el que lo dividimos.']
                    print(concm)
                    print('A continuación se veremos ejemplos de como multiplicar y sumar')
                    print('Ejemplos:')
                    print('5x2')
                    print('Se lee: 5 por 2 y es igual a sumar 2 cinco veces(2+2+2+2+2')
                    print('El resultado sería: 10')
                    paus=str(input('¿continuamos?'))
                    print('9/3')
                    print('Se lee 9 entre 3, Esto quiere decir dividir 9 en 3 partes iguales')
                    print('El resultado sería: 3')
                    paus2=str(input('¿continuamos?'))           #Estas son explicaciones de como se divide y multiplica
                    print('9/2')
                    print('Se lee 9 entre 2, Esta seria una división impropia')
                    print('Esta se resuelve buscando el número que multiplicado por 2 nos acerque más a 9')
                    paus3=str(input('¿continuamos?'))
                    print('Como 2x4=8 o 2x3=6 o 2x2= 4')
                    print('El más cercano sería 2x4=8')
                    print('Anotamos nuestr número (4) y el resultado (8) lo restamos a 9')
                    print('Quedando 1')
                    print('El resultado de 9/2 sería 4 y nos sobra 1')
                    ot=str(input('¿Hacemos ejercicios?'))
                    while ot in ['Si','si','Sí','sí']:
                        if ot in ['si','Si','Sí','sí']:
                            print('1)')
                            print('Multiplica 5 y 4')
                            ans=float(input())
                            while ans != 20:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans=float(input())
                            if ans ==20 :
                                print('Respuesta correcta')
                            print('2)')
                            print('Divide 6/2')
                            ans2=float(input())
                            while ans2 != 3:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans2=float(input())                       
                            if ans2 ==3:
                                print('Respuesta correcta')
                            print('3)')
                            print('Divide 10/3, No anotes el residuo')          #Aqui estan los ejercicios de multiplicacion y division
                            ans3=float(input())
                            while ans3 >=4 and ans3 <3:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans3=float(input())                       
                            if ans3 >=3 and ans3 <4:
                                print('Respuesta correcta')
                            print('4)')
                            print('Multiplica 5x7')
                            ans4=float(input())
                            while ans4 !=35:
                                print('Respuesta inválida, Intenta de nuevo')
                                ans4=float(input())                       
                            if ans4 ==35:
                                print('Respuesta correcta')
                            ot=str(input('¿Hacemos ejercicios?')) 
                            print('Has concluido todos los ejercicios con éxito!')
                                    
                    print('De acuerdo, volvamos al inicio')
                    break
        elif elmat in ['Buscar un tema','buscar','Buscar','buscar un tema']: #Aqui buscamos temas si es que existen en el temario
            print('¿Qué tema desea buscar?')
            btem=str(input())
            tmat={'Numero':'Lee, escribe y ordena números naturales hasta 1 000',
            'Adición y sustracción':'Resuelve problemas de suma y resta con números naturales hasta 1 000.',
            'Multiplicación y división':'Resuelve problemas de multiplicación con números naturales menores que 10.'}
            if btem in tmat:
                print('Mostrando',btem)
                print(tmat.get(btem))
                otr=str(input('¿Buscamos otro tema?'))
                while otr in ['Si','si','Sí','sí']:
                    btem=str(input('Ingrese el tema a buscar:'))
                    if btem in tmat:
                        print('Mostrando',btem)
                        print(tmat.get(btem))
                        otr=str(input('¿Buscamos otro tema?'))
                print('De acuerdo, Adiós')            
            else: 
                print(tmat.get(btem,'No se encuentra en nuestro temario'))
                otr=str(input('¿Buscamos otro tema?'))
                if otr in ['Si','si','Sí','sí']:
                    btem=str(input('Ingrese el tema a buscar:'))
                    while btem not in tmat:
                        print(tmat.get(btem,'No se encuentra en nuestro temario'))
                        otr=str(input('¿Buscamos otro tema?'))
                        if otr in ['No','no']:
                            break
                        btem=str(input('Ingrese el tema a buscar:'))   
        elif elmat in ['Retroceder','retroceder','volver']: #Aqui regresamos al menu
            print("Has elegido retroceder.")

    
        sn = input("Quieres seguir estudiando (s/n): ")




#Esta seccion es la de ciencias
    elif int(menu) == 2:
        print("\nElegiste la modalidad de Ciencias\n")
        print("A continuacion te van a aparecer diferentes ejercicios de ciencias y salud que vas a tener que responder.") #Aqui poenne cuales son los organos de los sentidos y ponen sus funciones segun la lectura
        archTexto.seek(2116)
        ejerciciocienc1 = archTexto.read(932)
        print(ejerciciocienc1)
        print("\nMenciona los 5 organos de los sentidos: ")
        for i in range(5):
            sen = str(input("\nOrgano: "))
            sentidos[sen] = ""
        print("\nMuy bien, el siguiente ejercicio va a ser mencionar las funciones de los organos que acabas de mencionar\n")
        organos = sentidos.keys()
        for elementos in organos:
            sentidos[elementos] = input("\nCual es la funcion de " + elementos + ": ")
        
        print("\n\n" + "*"*50 + "\n\n")
        archTexto.seek(3062)
        ejerciciocienc2 = archTexto.read(550)
        print(ejerciciocienc2)
        print("\nAhora explica en tus propias palabras lo que entendiste del texto: ") #Aqui explican en sus propias apalabras el ciclo del agua
        archEscribir = open("proyectodescripcion.txt", "a")
        archEscribir.write("\n")
        archEscribir.write(input(""))
        archEscribir.write("\n")
        archEscribir.close()
        print("\n\n" + "*"*50 + "\n\n")
        print("Ejercicio 3: elige 9 objetos, tres solidos, tres liquidos y tres gases y menciona sus nombre.") #Aqui difertencian y clasifican objetos en tres estados de la materia
        for i in range(3):
            nmbresol = input("\nCual es el nombre del objeto solido: ")
            print("\n" + "*"*50 + "\n")
            solido[nmbresol] = "Solido"
        
        for i in range(3):
            nmbreliq = input("\nCual es el nombre del objeto liquido: ")
            print("\n" + "*"*50 + "\n")
            liquido[nmbreliq] = "Liquido"
        
        for i in range(3):
            nmbregas = input("\nCual es el nombre del objeto gaseoso: ")
            print("\n" + "*"*50 + "\n")
            gas[nmbregas] = "Gas"
            

        print("Muy bien, has acabado el modulo de ciencias!!")
        sn = input("Quieres seguir estudiando (s/n): ")





#Esta seccion es la de español        
    elif int(menu) == 3:
        print("\n\n" + "*"*50 + "\n\n")
        print("Elegiste la modalidad de Español\n")
        print("A continuacion te van a aparecer diferentes ejercicios de lectura y español que vas a tener que responder.\n") #Aqui va el primer tema que es lectura y responden varias preguntas acerca de la lectura
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
        print("\n\n" + "*"*50 + "\n\n")
        print("\nA continuacion te va a aparecer otro ejercicio de lectura \n") #Aqui tienen que describir a un personaje de la segunda lectura
        archTexto.seek(930)
        ejercicio2esplect = archTexto.read(490)
        print(ejercicio2esplect)
        print("\n\nDe la historia anterior describe al personaje principal:")
        archEscribir = open("proyectodescripcion.txt", "a")
        archEscribir.write("\n")
        archEscribir.write(input(""))
        archEscribir.write("\n")
        archEscribir.close()

        print("\n\n" + "*"*50 + "\n\n")
        print("\nA continuacion te va a aparecer un ejercicio de español ") #Y por ultimo clasificvan palabras en sustantivos propios o comunes

        ejercicioesp3 = archTexto.read(564)
        print(ejercicioesp3)
        archTexto.seek(2014)
        ejercicioesp2p = archTexto.readlines()
        for elementos in ejercicioesp2p:
            print(elementos)
            if elementos == ("\n"):
                break
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
            print("\n" + "*" * 50)

            
            
        print("\nMuy bien has acabado con la modalidad de español, espero que te haya hido muy bien!!\n")

        sn = input("Quieres seguir estudiando (s/n): ")

    #Esta seccion aplica la accion de salir
    elif int(menu) == 4:
        print("Espero que tengas un buen dia, gracias por usar el programa!!")
        sn = "n"
    else:
        print("\n\nNo elegiste ninguna modailidad, porfavor eliga otra vez.\n\n")

archTexto.close()