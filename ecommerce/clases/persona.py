# Creamos la clase Persona con atributos y métodos que pueden heredar otras clases
class Persona:
    def __init__(self, nombre, apellido, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion