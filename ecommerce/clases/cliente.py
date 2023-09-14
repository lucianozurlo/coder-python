# Importamos la clase Persona del módulo persona.py en el paquete ecommerce 
from ecommerce.clases.persona import Persona

# Creamos la clase Cliente que hereda la clase Persona
class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, direccion, email, telefono):
        super().__init__(nombre, apellido, edad, direccion)
        self.email = email.lower()
        self.telefono = telefono

    # Método para mostrar información del cliente
    def mostrar_info_cliente(self):
        print(f'\n  · Nombre:    {self.nombre}')
        print(f'  · Apellido:  {self.apellido}')
        print(f'  · Edad:      {self.edad}')
        print(f'  · Dirección: {self.direccion}')
        print(f'  · E-mail:    {self.email}')
        print(f'  · Teléfono:  {self.telefono}')
        
    # Método para simular una compra
    def realizar_compra(self, producto):
        print(f'\n  >> El cliente {self.nombre} {self.apellido} realizó la compra del producto: {producto}.')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
