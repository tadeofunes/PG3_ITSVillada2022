class triangulo:
    
    def __init__(self):
        self.lado1 = int(input("Ingrese el primer lado: "))
        self.lado2 = int(input("Ingrese el segundo lado: "))
        self.lado3 = int(input("Ingrese el tercer lado: "))
        self.lista = [self.lado1, self.lado2, self.lado3]
        
    def encontrarValorMaximo(self):
        ç = max(self.lista)
        print(ç)        

    def esEquilatero(self,):
        if(self.lado1 == self.lado2 and self.lado2 == self.lado3):
            print("Es un triangulo equilatero")
        else:
            print("No es un triangulo equilatero")

tr=triangulo()
tr.encontrarValorMaximo()
tr.esEquilatero()
