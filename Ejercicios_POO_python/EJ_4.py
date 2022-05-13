class operaciones:
    def __init__(self):
        self.numero1 = int(input("Ingrese el primer numero: "))
        self.numero2 = int(input("Ingrese el segundo numero: "))
        self.sumar()
        self.dividir()
        self.multiplicar()
        self.restar()

    def sumar(self):
        print("la suma de los dos numeros es ", self.numero1+self.numero2)

    def restar(self):
        print("la resta de los dos numeros es ", self.numero1-self.numero2)

    def multiplicar(self):
        print("la multiplicacion de los dos numeros es ", self.numero1*self.numero2)

    def dividir(self):
        print("la division de los dos numeros es ", self.numero1/self.numero2)

op1=operaciones()
op1.__init__()
