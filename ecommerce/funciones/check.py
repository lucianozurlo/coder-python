# Función para validar el nombre y apellido Ingresádos por el usuario (se pueden ingresar solo letras y espacios)
def check_nombre(valor):
    while not (all(c.isalpha() or c.isspace() for c in valor) and valor.strip()):
        print('\n    <!> Error (campo obligatorio): El nombre y apellido pueden contener solo letras y/o espacios.\n')
        valor = input('    Ingresalo nuevamente: ')
        print('')
    return valor

# Función para validar la edad Ingresáda por el usuario (se pueden ingresar solo números)
def check_edad(valor):
    while not valor.isdigit() or int(valor) <= 0:
        print('\n    <!> Error (campo obligatorio): Tenés que ingresar una edad válida.\n')
        valor = input('    Ingresala nuevamente: ')
        print('')
    return valor

# Función para validar el e-mail Ingresádo por el usuario (se tienen que ingresar al menos un "@" y un ".")
def check_email(valor):
    while '@' not in valor or '.' not in valor:
        print('\n    <!> Error (campo obligatorio): Tenés que ingresar una dirección de e-mail válida.\n')
        valor = input('    Ingresala nuevamente: ')
        print('')
    return valor
