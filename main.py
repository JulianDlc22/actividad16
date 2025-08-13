class Biblioteca:
    def __init__(self, codigo, titulo, autor, yearPublicacion):
        self.titulo = titulo
        self.autor = autor
        self.yearPublicacion = yearPublicacion
        self.codigo = codigo

    def mostrar_info(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Publicacion: {self.yearPublicacion} - Codigo: {self.codigo}"

class GestionBiblioteca:
    def __init__(self):
        self.biblioteca = []

    def agregar(self):
        try:
            codigoUnico = int(input("Codigo: "))
            if codigoUnico in self.biblioteca:
                print("El codigo ya existe")
                return

            titulo = input("Titulo: ")
            autor = input("Autor: ")
            publicacion = int(input("Publicacion: "))

            self.biblioteca.append(Biblioteca(codigoUnico, titulo, autor, publicacion))
            print("Agregado exitosamente...")

        except ValueError:
            print("El año debe ser un número entero...")

    def mostrar(self):

        if not self.biblioteca:
            print("Aun no hay datos Ingresados...")
        else:
            print("--Libros Ingresados--")

            for i, verInfo in enumerate(self.biblioteca, start=1):
                print(f"{i}. {verInfo.mostrar_info()}")

    def eliminar(self):

        print("--Eliminar Libros--")

        print("\n Desea eliminar por nombre o codigo?")
        print("\n presione 1.por nombre")
        print("\n presione 2.por codigo")

        opcion = input("Eliga la Opcion: ")

        try:
            int(opcion)

        except ValueError:
            print("Error- tiene que elegir un opcion entre 1 y 2")



        try:
           buscarCodigo = int(input("Ingrese el codigo del libro que desea eliminar: "))

           if buscarCodigo in self.biblioteca:
               self.biblioteca.remove(buscarCodigo)
               print("Eliminado Exitosamente...")

        except ValueError:
            print("Error- esta ingresando un codigo invalido")






