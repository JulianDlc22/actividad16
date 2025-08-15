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

        print("\n Desea eliminar por titulo o codigo?")
        print("presione 1.por titulo")
        print("presione 2.por codigo")

        opcion = input("\nEliga la Opcion: ")

        try:
            int(opcion)

            match opcion:
                case 1:
                    print(" ")
                    tituloDelete = input("Ingrese el nombre: ")
                    for nom in self.biblioteca:
                        if nom.titulo.lower() == tituloDelete.lower():
                            self.biblioteca.remove(nom)
                            print("Libro Eliminado Exitosamente...")
                        else:
                            print("Libro no encontrado...")

                case 2:
                    print(" ")
                    codigoDelete = input("Ingrese el codigo: ")
                    for cod in self.biblioteca:
                        if cod.codig == codigoDelete:
                            self.biblioteca.remove(cod)
                            print("Libro Eliminado Exitosamente...")
                        else:
                            print("Libro no encontrado...")


        except ValueError:
            print("Error- tiene que elegir un opcion entre 1 y 2")

gestion = GestionBiblioteca()

while True:
    print("--MENU BIBLIOTECA--")
    print("1. Agregar Libro")
    print("2. Mostrar Libros Ingresados")
    print("3. Eliminar Libro")
    print("4. Salir ")

    try:
        opcion = int(input("Ingrese la Opcion: "))
        match opcion:
            case 1:
                gestion.agregar()
            case 2:
                gestion.mostrar()
            case 3:
                gestion.eliminar()
            case 4:
                print("Saliendo del Programa...")
                break

    except ValueError:
        print("Error- ingrese un numero entero")









