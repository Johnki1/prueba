
from crud import (
    crear_base_de_datos,
    crear_coleccion,
    insertar_documento,
    ver_documentos,
    actualizar_documento,
    eliminar_documento,
    eliminar_coleccion
)
from menu import mostrar_menu

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_base_de_datos()
        elif opcion == "2":
            crear_coleccion()
        elif opcion == "3":
            insertar_documento()
        elif opcion == "4":
            ver_documentos()
        elif opcion == "5":
            actualizar_documento()
        elif opcion == "6":
            eliminar_documento()
        elif opcion == "7":
            eliminar_coleccion()
        elif opcion == "8":
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
