# Importamos todas las funciones del menú
from ecommerce.funciones.menu import crear_cliente, mostrar_cliente,comprar, guardar_db_clientes, vaciar_db_clientes, guardar_y_salir

# Mensaje de bienvenida
print('\n\n¡Hola!')

# Función para mostrar el menú principal
def mostrar_menu():
    print('\n-------------------------------------')
    print('1. Ingresar un nuevo cliente')
    print('2. Mostrar información de un cliente')
    print('3. Realizar una compra')
    print('4. Guardar base de datos de clientes')
    print('5. Borrar base de datos de clientes')
    print('6. Salir')

while True:
    mostrar_menu()
    opcion = input('-------------------------------------\n\nSeleccioná una opción del menú: ')

    if opcion == '1':
        crear_cliente()

    elif opcion == '2':
        mostrar_cliente()

    elif opcion == '3':
        comprar()

    elif opcion == '4':
        guardar_db_clientes()

    elif opcion == '5':
        vaciar_db_clientes()

    elif opcion == '6':
        guardar_y_salir()
        break

    else:
        print('\n\nOpción no válida. Por favor, intentalo nuevamente.')
