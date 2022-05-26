try:    
    valor = input("Escribe lo que quieras almacenar: ")
    file = open('readme.txt', 'w')
    file.write("Funciona: ")
    if valor.isnumeric() == True:
        file.write(int(valor))
    else: 
        file.write(valor)
    file.close()
    file = open('readme.txt', 'r')
    print(file.read())
    file.close()
except TypeError:
    file = open('readme.txt', 'w')
    file.write("Tu tipeado tiene un problema")
    file.close()
    file = open('readme.txt', 'r')
    print(file.read())
    file.close()