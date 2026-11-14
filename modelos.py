# 1. CLASE BASE: LIBRO
# ==================================================

class Libro:

    def __init__(self, titulo, autor, año, disponible, prestado_a):
        self.__titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible
        self.prestado_a = prestado_a

    # ENCAPSULAMIENT0

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo.strip():
            self.__titulo = nuevo_titulo
        else:
            raise ValueError("El título no puede estar vacío.")

    # PRESTAR UN LIBRO

    def prestar(self, persona):
        if self.disponible:
            self.disponible = False
            self.prestado_a = persona
            print(f"El libro '{self.titulo}' ha sido prestado a {persona}.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    # DEVOLVER UN LIBRO

    def devolver(self):
        if not self.disponible:
            print(f"El libro '{self.titulo}' ha sido devuelto.")
            self.disponible = True
            self.prestado_a = None
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    # RENOVAR EL PRÉSTAMO

    def renovar(self):
        if not self.disponible:
            print(
                f"El préstamo de '{self.titulo}' "
                f"ha sido renovado para {self.prestado_a}."
            )
        else:
            print(f"El libro '{self.titulo}' no está prestado.")

    # MOSTRAR INFORMACIÓN

    def mostrar_informacion(self):
        estado = (
            "Disponible"
            if self.disponible
            else f"Prestado a {self.prestado_a}"
        )

        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año}")
        print(f"Estado: {estado}")
        print("-" * 30)

    # CONSULTAR ESTADO

    def consultar_estado(self):
        if self.disponible:
            print(f"El libro '{self.titulo}' está disponible.")
        else:
            print(
                f"El libro '{self.titulo}' "
                f"está prestado a {self.prestado_a}."
            )



# 2. CLASE DERIVADA: LIBRO DIGITAL
# ==================================================

class LibroDigital(Libro):

    def __init__(
        self, titulo, autor, año, disponible, prestado_a,
        formato, tamaño_mb
    ):
        super().__init__(
            titulo, autor, año, disponible, prestado_a
        )

        self.formato = formato
        self.tamaño_mb = tamaño_mb

    # DESCARGAR LIBRO DIGITAL

    def descargar(self):
        print(
            f"El libro digital '{self.titulo}' "
            f"está listo para descargarse en formato {self.formato}."
        )

    # POLIMORFISMO: SOBRESCRITURA DE MÉTODO

    def mostrar_informacion(self):
        super().mostrar_informacion()

        print("Tipo: Libro digital")
        print(f"Formato: {self.formato}")
        print(f"Tamaño: {self.tamaño_mb} MB")
        print("-" * 30)


# 3. CLASE AUXILIAR: BIBLIOTECA
# ==================================================

class Biblioteca:

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    # AGREGAR LIBROS

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
            print(f"'{libro.titulo}' se agregó a la biblioteca.")
        else:
            print("El objeto ingresado no es un libro válido.")

    # MOSTRAR CATÁLOGO

    def mostrar_catalogo(self):
        print(f"\n=== CATÁLOGO DE {self.nombre.upper()} ===")

        if not self.libros:
            print("La biblioteca no tiene libros registrados.")
        else:
            for libro in self.libros:
                libro.mostrar_informacion()

    # BUSCAR LIBRO

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro

        return None

    # PRESTAR LIBRO

    def prestar_libro(self, titulo, persona):
        libro = self.buscar_libro(titulo)

        if libro:
            libro.prestar(persona)
        else:
            print(f"No se encontró el libro '{titulo}'.")

    # DEVOLVER LIBRO

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)

        if libro:
            libro.devolver()
        else:
            print(f"No se encontró el libro '{titulo}'.")

    # CONSULTAR LIBRO

    def consultar_libro(self, titulo):
        libro = self.buscar_libro(titulo)

        if libro:
            libro.consultar_estado()
        else:
            print(f"No se encontró el libro '{titulo}'.")
