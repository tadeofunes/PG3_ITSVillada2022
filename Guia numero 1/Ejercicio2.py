año=int(input("Ingrese un año: "))
def añobisiesto(año):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        return ("El año es bisiesto")
    else:
        return ("El año no es bisiesto")

print(añobisiesto(año))
