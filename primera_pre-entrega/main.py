# Cargar y guardar base de datos en archivo JSON
# *(si no encuentra el archivo JSON, va a crear uno nuevo a partir de un diccionario vacío)*

import json

def load_db_users():
    try:
        with open("db_users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_db_users():
    with open('db_users.json', 'w') as f:
        json.dump(db_users, f)
        

### Funciones:
def register_user(user, passw):
    if user not in db_users:
        db_users[user] = passw
        save_db_users()
        print('\n>> ¡Usuario registrado con éxito! <<\n')
    else:
        print('\n>> El nombre de usuario ya existe. Por favor, ingresá un nombre diferente. <<')
        enter_user()

def enter_user():
    print('\n> Registrá tus datos: ')
    user = input('\nUsuario: ')
    passw = input('Contraseña: ')
    register_user(user, passw)

def show_users():
    if len(db_users) == 0:
        print('\n>> No hay usuarios registrados <<\n')
    else:
        print('\n> Usuarios registrados:')
        for user in db_users:
            print(f'· {user}')
        print('')

def login_check(user, passw):
    if user in db_users and db_users[user] == passw:
        print(f'\n>> ¡Bienvenid@ {user}! <<\n')
    else:
        print('\n>> Nombre de usuario o contraseña incorrectos. <<\n')

def login():
    print('\n> Ingresá tus datos: ')
    user = input('\nUsuario: ')
    passw = input('Contraseña: ')
    login_check(user, passw)

def reset_db_users():
    clear = input('\n>> ¿Querés borrar la base de usuarios? (s/n) ')
    if clear.lower().strip() == "s":
        global db_users
        db_users = {}
        save_db_users()
        print('\n>> La base de datos SE HA BORRADO con éxito. <<\n')
    else:
      print('\n>> La base de datos NO SE HA BORRADO. <<\n')


### **Menú principal**
db_users = load_db_users()

print('-------------------------------------')
print('1. Registrar un nuevo usuario')
print('2. Mostrar usuarios registrados')
print('3. Iniciar sesión')
print('4. Borrar base de datos de usuarios')
print('5. Salir')

while True:
    option = input('-------------------------------------\n\nSeleccioná una opción del menú: ')
    if option == '1':
        enter_user()
    elif option == '2':
        show_users()
    elif option == '3':
        login()
    elif option == '4':
        reset_db_users()
    elif option == '5':
        save_db_users()
        print('\n>> ¡Chau! <<\n')
        break
    else:
        print('\n>> Esa opción no existe. Volvé a intentarlo: \n')
