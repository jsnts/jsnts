print("\nDe que numeo quiere mostrar su serie: ")
numero = int(input(""))
print("\nCunatos numeos quiere mostrar en su serie: ")
cantidad = int(input(""))

serie = numero
while cantidad != 0:
    print(serie)
    serie = serie + numero
    cantidad = cantidad - 1