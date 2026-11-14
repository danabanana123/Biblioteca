# IMPORTACIÓN DE CLASES

from modelos import Libro, LibroDigital, Biblioteca


# 1. INSTANCIACIÓN DE OBJETOS
# ==================================================

mi_biblioteca = Biblioteca("Biblioteca Central")

# Objetos de la clase base

libro1 = Libro(
    "Orgullo y prejuicio", "Jane Austen", 1813, True, None
)

libro2 = Libro(
    "La divina comedia", "Dante Alighieri", 1320, True, None
)

# Objetos de la subclase

libro3 = LibroDigital(
    "Las ventajas de ser invisible",
    "Stephen Chbosky", 1999, True, None, "PDF", 5.2
)

libro4 = LibroDigital(
    "Las intermitencias de la muerte",
    "José Saramago", 2005, True, None, "EPUB", 3.8
)


# 2. COMPOSICIÓN
# ==================================================

print("\n=== PRUEBA DE COMPOSICIÓN ===")

mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)
mi_biblioteca.agregar_libro(libro3)
mi_biblioteca.agregar_libro(libro4)

mi_biblioteca.mostrar_catalogo()


# 3. ENCAPSULAMIENTO
# ==================================================

print("\n=== PRUEBA DE ENCAPSULAMIENTO ===")

print(f"Título actual: {libro1.titulo}")

libro1.titulo = "Orgullo y prejuicio - Edición especial"

print(f"Título actualizado: {libro1.titulo}")

try:
    libro1.titulo = " "
except ValueError as error:
    print(f"Validación correcta: {error}")


# 4. HERENCIA Y POLIMORFISMO
# ==================================================

print("\n=== PRUEBA DE HERENCIA Y POLIMORFISMO ===")

for libro in mi_biblioteca.libros:
    libro.mostrar_informacion()


# 5. OPERACIONES
# ==================================================

print("\n=== OPERACIONES ===")

mi_biblioteca.prestar_libro(
    "Orgullo y prejuicio - Edición especial",
    "Rajesh Koothrappali"
)

libro1.renovar()

mi_biblioteca.devolver_libro(
    "Orgullo y prejuicio - Edición especial"
)

mi_biblioteca.prestar_libro(
    "Las ventajas de ser invisible",
    "Amy Farrah Fowler"
)

libro3.renovar()
libro3.descargar()

mi_biblioteca.consultar_libro(
    "Las intermitencias de la muerte"
)


# 6. INDEPENDENCIA ENTRE OBJETOS
# ==================================================

print("\n=== INDEPENDENCIA DE LOS OBJETOS ===")

print(f"Estado de libro1: {libro1.disponible}")
print(f"Estado de libro3: {libro3.disponible}")

mi_biblioteca.devolver_libro(
    "Las ventajas de ser invisible"
)

print(
    f"Estado de libro3 después de devolverlo: "
    f"{libro3.disponible}"
)

print(f"Estado de libro4: {libro4.disponible}")
