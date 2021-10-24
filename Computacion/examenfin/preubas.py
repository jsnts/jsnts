menu = input("Seleccion: ")
if int(menu) == 1:
    print("Usted eligio la modalidad de Matematicas")
    print('Éstos son los temas a repasar:')
    tmat={'Numero':'Lee, escribe y ordena números naturales hasta 1 000',
    'Adición y sustracción':'Resuelve problemas de suma y resta con números naturales hasta 1 000.',
    'Multiplicación y división':'Resuelve problemas de multiplicación con números naturales menores que 10.'}
    print(tmat)
    elmat=str(input('¿Qué desea hacer?'))
    acmat=['Seleccionar un tema','Buscar un tema','Retroceder']
    print(acmat)
    if elmat in ['Seleccionar un tema','seleccionar un tema','seleccionar','selecc']:
        print('Ha elegido "Seleccionar un tema"')
        tael=str(input('¿Qué tema desea ver?'))
        while True:
            tael=str(input('¿Qué tema desea ver?'))
            if tael in ['suma y resta','Suma y Resta','Adición y Sustracción','adición y sustracción','adicion y sustraccion']:
                print('Adición y Sustracción')
                print('Conceptos:')
                concm=['Adición: operación matemática de composición que consiste en combinar o añadir dos números o más para obtener una cantidad final',
                'Sustracción: Consiste en restar una cantidad (el sustraendo) de otra (el minuendo) para averiguar la diferencia entre las dos']
                print(concm)
                print('A continuación se veremos ejemplos de Suma y resta de cantidades menores a 1000')
                print('Ejemplo 1:')
                print('3+7=10')
                print('7-3=4')
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
                        print('3)')
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
                        print('Has concluido todos los ejercicios con éxito!')         
                print('De acuerdo, volvamos al inicio')
                break
            elif tael in ['Numero','Número','numero','número','NÚMERO','NUMERO']:
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
                print('Ordenar los números de mayor a menor:')
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
                        print('3)')
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
                        print('Has concluido todos los ejercicios con éxito!')         
                print('De acuerdo, volvamos al inicio')
                break
            elif tael in ['multiplicacion y division','Multiplicacion y Division','multiplicación y división','Multiplicación y división']:
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
                paus2=str(input('¿continuamos?'))
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
                        print('Divide 10/3, No anotes el residuo')
                        ans3=str(input())
                        while ans3 >=4 and ans3 <3:
                            print('Respuesta inválida, Intenta de nuevo')
                            ans3=str(input())                       
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
                        print('Has concluido todos los ejercicios con éxito!')         
                print('De acuerdo, volvamos al inicio')
                break
    elif elmat in ['Buscar un tema','buscar','Buscar','buscar un tema']:
        print('¿Qué tema desea buscar?')
        btem=str(input())
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
    elif elmat in ['Retroceder','retroceder','volver']:
        print('Deseas seguir estudiando?')


