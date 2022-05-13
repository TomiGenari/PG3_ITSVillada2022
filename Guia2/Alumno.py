class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def mostrar_estado(self):
        if self.nota>=6:
            print("Regular")
        else:
            print("Libre")


alumno1 = Alumno()
alumno1.inicializar("Yaco", 7)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2 = Alumno()
alumno2.inicializar("Franquito", 2)
alumno2.imprimir()
alumno2.mostrar_estado()

#hola