def pintar():
    ancho=int(input("Ingrese un numero: "))
    largo=int(input("Ingrese un numero: "))
    caracter=str(input("Ingrese un caracter: "))

    for i in range(largo):
        print(ancho*caracter)

pintar()
    