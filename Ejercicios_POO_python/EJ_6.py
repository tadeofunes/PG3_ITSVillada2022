class familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
        print(self.__str__())
    
    def __str__(self):
        hijos2 = " ".join(self.hijos)
        cadena = self.padre+" "+self.madre+" "+hijos2
        return cadena

hijos = ["Ricardo", "Mamerto", "Samuel"]        
f1 = familia("Los padres de la familia se llaman: Pedro y", "Juanita, Los hijos se llaman:", hijos)