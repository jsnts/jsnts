archTexto = open("ArchuviodeTextoej.txt","w")

archTexto.write("Hola Bienvenido a la calculadora de IMC \n\n")

print("\n\nHola Bienvenido a la calculadora de IMC \n\n")

for i in range(3):

    print("Ingresa tus datos\n")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    peso = float(input("Peso en kilos: "))
    estatura = float(input("Estatura en mts: "))

    IMC = peso/(estatura ** 2)

    print("Su IMC es " + str(IMC) + "\n")

    archTexto.write("**************************************** \n\n")
    archTexto.write("Nombre: " + nombre + "\n")
    archTexto.write("Edad: " + edad + "\n")
    archTexto.write("Peso: " + str(peso) + "\n")
    archTexto.write("Estatura: " + str(estatura) + "\n")
    archTexto.write("IMC: " + str(IMC) + "\n\n")


archTexto.close()
