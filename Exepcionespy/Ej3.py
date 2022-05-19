class EncontrarMesesDelAño:
    def __init__(self):
        while True:
            try:
                self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
                len(self.meses)
                self.Mes = (int(input("Ingrese el mes: ")))
                print (self.meses[self.Mes-1])
            except IndexError:
                print("Error, ingrese un numero del 1 al 12")

e=EncontrarMesesDelAño()