class persona:
    def iniciador(self, nombre):
        self.nombre = nombre
    
    def imprimir(self):
        print("Nombre: ", self.nombre)

p1=persona()
p1.iniciador(input("Ingrese su nombre: "))
p1.imprimir()