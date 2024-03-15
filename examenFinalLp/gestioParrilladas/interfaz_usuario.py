import sys

def mostrar_menu():
    print("1. Comprar ticket")
    print("2. Mostrar ventas")
    print("3. Salir")

def pedir_opcion():
    opcion = input("Ingrese una opción: ")
    return int(opcion)

def main():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        if opcion == 1:
            # Implementar la compra de tickets
            pass
        elif opcion == 2:
            # Implementar la visualización de ventas
            pass
        elif opcion == 3:
            sys.exit(0)
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()