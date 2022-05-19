class dividirenteros:
    def dividirentero(self):
        while True:
            try:
                self.num1 = (int(input("Ingrese el primer numero: ")))
                self.num2 = (int(input("Ingrese el segundo numero: ")))
                self.suma = self.num1 / self.num2
                print ("Su numero es ", self.suma)
            except ZeroDivisionError:
                print ("Error, no puedes dividir un numero por 0")

    

s=dividirenteros()
s.dividirentero()