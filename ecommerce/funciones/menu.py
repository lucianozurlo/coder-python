# Importamos todas las funciones generales
from ecommerce.funciones.check import *

# Importamos la base de datos y sus funciones para manejarla
from ecommerce.funciones.db_json import *

# Importamos la clase Cliente del módulo cliente.py en el paquete ecommerce 
from ecommerce.clases.cliente import Cliente


### Funciones del Menú Principal

## 1. Ingresar un nuevo cliente
# Función para cargar datos de un nuevo cliente (hace la validación de la variable y, de existir, elimina espacios al inicio y fin). Después, retorna con el constructor de la clase Cliente
def cargar_cliente():
    nombre = check_nombre(input('  · Nombre (*): ').strip())
    apellido = check_nombre(input('  · Apellido (*): ').strip())
    edad = check_edad(input('  · Edad (*): ').strip())
    direccion = input('  · Dirección: ').strip()
    email = check_email(input('  · E-mail (*): ').strip())
    telefono = input('  · Teléfono: ').strip()
    return Cliente(nombre, apellido, edad, direccion, email, telefono)

## Función para crear un nuevo cliente y sumarlo la lista clientes
def crear_cliente():
    print('\n\n> Ingresá los datos del nuevo cliente:\n  (*) campos obligatorios\n')
    nuevo_cliente = cargar_cliente()
    if nuevo_cliente:
        clientes.append(nuevo_cliente)
        print(f'\n  >> El cliente :: {nuevo_cliente} :: se creó con éxito.\n')

## 2. Mostrar información de un cliente
# Función para mostrar los datos los cliente enumerando los clientes (hace las veces de ID) que luego permite Seleccionár y mostrar los detalles
def mostrar_cliente():
    if not clientes:
        print('\n  >> No hay clientes registrados.\n')
    else:
        print('\n\nClientes registrados:\n')
        for i, cliente in enumerate(clientes):
            print(f'{i + 1}. {cliente}')
        while True:
            try:
                cliente_index = int(input('\n> Seleccioná un cliente: ')) - 1
                if 0 <= cliente_index < len(clientes):
                    cliente_Seleccionádo = clientes[cliente_index]
                    # ejecuta un método de la clase Cliente
                    cliente_Seleccionádo.mostrar_info_cliente()
                    print('')
                    break
                else:
                    print(f'\n  <!> Error: El ID de cliente {cliente_index + 1} no existe.\n')
            except ValueError:
                print('\n  <!> Error: Tenés que ingresar un ID de cliente válido.\n')

## 3. Relizar una compra
# Función para simular una compra realizada por un cliente
def comprar():
    if not clientes:
        print('No hay clientes registrados.\n')
    else:
        print('\n\nSeleccioná que cliente va a hacer la compra:\n')
        for i, cliente in enumerate(clientes):
            print(f'{i + 1}. {cliente}')
        while True:
            try:
                cliente_index = int(input('\n> Seleccioná un cliente: ')) - 1
                if 0 <= cliente_index < len(clientes):
                    cliente_Seleccionádo = clientes[cliente_index]
                    producto = input('\n  · Ingresá el producto que va a comprar: ')
                    # ejecuta el otro método de la clase Cliente
                    cliente_Seleccionádo.realizar_compra(producto)
                    print('')
                    break
                else:
                    print(f'\n  <!> Error: El ID de cliente {cliente_index + 1} no existe.\n')
            except ValueError:
                print('\n  <!> Error: Tenés que ingresar un ID de cliente válido.\n')

## 4. Guardar base de datos de clientes
# Función para generar un diccionario conla base de datos de clientes y guardarlo en un archivo JSON
def guardar_db_clientes():
    datos_clientes = {}
    for i, cliente in enumerate(clientes):
        datos_clientes[i + 1] = {
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'edad': cliente.edad,
            'direccion': cliente.direccion,
            'email': cliente.email,
            'telefono': cliente.telefono
        }
    with open('db_clientes.json', 'w') as f_json:
        json.dump(datos_clientes, f_json)
    print('\n  >> Los datos de clientes SE GUARDARON con éxito en "db_clientes.json".\n')

## 5. Borrar base de datos de clientes
# Función para vaciar la base de datos activa y la que está guardada en el archivo JSON)
def vaciar_db_clientes():
    while True:
        clear = input('\n\n> ¿Querés borrar la base de datos de clientes?:\n  IMPORTANTE: También se va a eliminar la base de datos guardada (S/N): ')
        if clear.lower().strip() == "s":
            global clientes
            clientes = []
            borrar_db_clientes()
            print('\n  >> La base de datos de clientes SE BORRÓ con éxito.\n')
            break
        elif clear.lower() == 'n':
            print('\n  >> La base de datos de clientes NO SE BORRÓ.\n')
            break
        else:
            print('\n  <!> Error: Tenés que ingresar una opción válida.')

## 6. Salir
# Función para salir y tener la opción de guardar la base de datos de clientes antes de cerrar el programa
def guardar_y_salir():
    while True:
        confirmacion = input('\n\n> ¿Querés guardar los datos de clientes? (S/N): ')
        if confirmacion.lower() == 's':
            with open('db_clientes.json', 'w') as f_json:
                datos_clientes = {}
                for i, cliente in enumerate(clientes):
                    datos_clientes[i + 1] = {
                        'nombre': cliente.nombre,
                        'apellido': cliente.apellido,
                        'edad': cliente.edad,
                        'direccion': cliente.direccion,
                        'email': cliente.email,
                        'telefono': cliente.telefono
                    }
                json.dump(datos_clientes, f_json)
                print('\n  >> Los datos de clientes SE GUARDARON con éxito en "db_clientes.json".\n')
                break
        elif confirmacion.lower() == 'n':
            print('\n  >> Los datos de clientes NO SE GUARDARON.\n')
            break
        else:
            print('\n    <!> Error: Tenés que ingresar una opción válida.\n')
    print('\n¡Chau!\n\n')
