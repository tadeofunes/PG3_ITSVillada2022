class alumno:
    def iniciador(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

Al1=alumno()
Al1.iniciador(input("Ingrese su nombre: "), input("Ingrese su nota: "))
Al1.imprimir()