from hashlib import sha512
from csv import reader as csv_reader
from config import FILENAME

global login_user
login_user = ''

global pass_hashmap
pass_hashmap = {}

'''
with open('users.csv', 'w+') as file:
    file.write(sha512(b'lol').hexdigest())

with open('users.csv', 'r') as file:
    print(file.readline() == sha512(l.encode('utf-8')).hexdigest())
'''

hash512 = lambda x: sha512(x.encode('utf-8')).hexdigest()

def update(filename = FILENAME):
    with open(filename, 'r') as file:
        reader = csv_reader(file, delimiter=',')
        pass_hashmap = {x[0]:x[1] for x in reader}
    return pass_hashmap

def add(array, filename = FILENAME):
    with open(filename, 'a+') as file: file.write(f"{','.join(array)}\n")

def select(start, end):
    while True:
        inp = input('>>')
        if inp.isdigit() and start <= int(inp) <= end:
            return int(inp)
        print('No valido')

def valid_login(username, password):
    global pass_hashmap
    for x in pass_hashmap.keys():
        if x == username:
            return pass_hashmap[x] == hash512(password)
    return False

def valid_register(username):
    global pass_hashmap
    return not(username in pass_hashmap)


def menu():
    global pass_hashmap
    pass_hashmap = update()
    while True:
        print('1) Login\n2) Registrar\n3) Exit')
        inp = select(1,3)
        if inp == 1:
            if login():
                return login_user
        if inp == 2:
            if register():
                update()
        if inp == 3:
            return None

def login():
    global login_user
    while True:
        username = input('Please enter a username (press 0 to exit): ')
        if ( username.isdigit() and 0 == int(username) ):
            return False
        password = input('Please enter a password (press 0 to exit): ')
        if ( password.isdigit() and 0 == int(password) ):
            return False
        if valid_login(username, password):
            global login_user
            login_user = username
            return True
        print('Invalid')
    

def register():
    while True:
        username = input('Please create a username (press 0 to exit): ')
        if ( username.isdigit() and 0 == int(username) ):
            return False
        password = input('Please create a password (press 0 to exit): ')
        if ( password.isdigit() and 0 == int(password) ):
            return False
        if valid_register(username):
            add([username, hash512(password)])
            pass_hashmap[username] = hash512(password)
            return True
        print('Invalid')

if __name__ == '__main__':
    menu()