import json

# Importamos la clase Cliente del módulo cliente.py en el paquete ecommerce 
from ecommerce.clases.cliente import Cliente

# Cargar y guardar base de datos en archivo JSON
# Verificar si el archivo JSON existe, y si no, crearlo

# Función para limpiar la base de datos de clientes
def borrar_db_clientes():
    global db_clientes
    db_clientes = {}
    with open('db_clientes.json', 'w') as f:
        json.dump({}, f)

# Función para cargar la base de datos de clientes desde un archivo JSON
def cargar_db_clientes():
    try:
        with open('db_clientes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        borrar_db_clientes()

# Función para cargar clientes desde el archivo JSON al iniciar el programa
def load_clientes_from_json():
    try:
        with open('db_clientes.json', 'r') as f_json:
            datos_clientes = json.load(f_json)
            return [Cliente(
                cliente_data['nombre'],
                cliente_data['apellido'],
                cliente_data['edad'],
                cliente_data['direccion'],
                cliente_data['email'],
                cliente_data['telefono']
            ) for _, cliente_data in datos_clientes.items()]
    except:
        return []

# Inicialización de la lista de clientes con los datos cargados desde el archivo JSON
clientes = load_clientes_from_json()