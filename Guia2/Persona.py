class Persona:
    def setNombre(self,name):
        self.nombre=name

    def imprimir(self):
        print("Nombre: ",self.nombre)



persona=Persona()
persona.setNombre("Nari")
persona.imprimir()