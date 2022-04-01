Palabra=input("Ingrese la palabra que quiere saber el numero de vocales:")

def contarvocales(Palabra):
    vocales=0
    for ind in range(0,len(Palabra)):
        if Palabra[ind]=="a" or Palabra[ind]=="e" or Palabra[ind]=="i" or Palabra[ind]=="o" or Palabra[ind]=="u":
            vocales+=1
    print("El numero de vocales es: ",vocales)

print(contarvocales(Palabra))