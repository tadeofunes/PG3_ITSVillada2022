while True:
    try:
        num1=int(input("Ingrese el primer numero: "))
        num2=int(input("Ingrese el segundo numero: "))
        division=num1/num2
        print ("Su numero es ", division)
    except ZeroDivisionError:
        print ("Error, no puedes dividir un numero por 0")

    except ValueError:
        print ("Error, ingrese un numero")