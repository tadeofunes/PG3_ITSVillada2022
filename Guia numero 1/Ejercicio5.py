palabra = input("Ingrese la palabra que desea evaluar: ")

def palindromos(palabra):
    igual, aux = 0, 0
    
    for ind in reversed(range(0, len(palabra))):
        if palabra[ind].lower() == palabra[aux].lower():
            igual += 1
        aux += 1

    if len(palabra) == igual:
            print ("esCapicua" ,palabra,"===True")
    else:
        print("esCapicua" ,palabra,"===False")
 
print (palindromos(palabra))

