from operator import index

def EncontrarNum(numero, lista):
    return(lista.index(numero))

numero=int(input())
lista=[1,2,3,4,5,6,7,8,9,10]
print (EncontrarNum(numero, lista))
