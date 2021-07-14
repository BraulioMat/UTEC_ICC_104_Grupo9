from hashlib import sha224

'''
with open('users.csv', 'w+') as file:
    file.write(sha224(b'lol').hexdigest())

with open('users.csv', 'r') as file:
    print(file.readline() == sha224(l.encode('utf-8')).hexdigest())
'''

global filename
filename = 'users.csv'
global username
username = ''

def add(array, filename = filename):
    with open(filename, 'a+') as file:
        file.write(f"{','.join(array)}\n")

def select(start, end):
    while True:
        inp = input('>>')
        if inp.isdigit() and start <= int(inp) <= end:
            return int(inp)
        print('No valido')

def valid(username, password, filename= filename):
    with open(filename, 'r') as file:
        for x in file:
            temp = x.split(',')
            if temp[0] == username:
                print(sha224(password.encode('utf-8')).hexdigest())
                return temp[1].strip('\n') == sha224(password.encode('utf-8')).hexdigest()


def menu():
    while True:
        print('1) Login\n2) Registrar\n3) Exit')
        inp = select(1,3)
        if inp == 1:
            if login():
                return True
        if inp == 2:
            register()
        if inp == 3:
            return False

def login():
    while True:
        user = input('Please enter a username (press 0 to exit): ')
        pas = input('Please enter a password (press 0 to exit): ')
        if user.isdigit() and 0 <= int(user) <= 0:
            return False
        if pas.isdigit() and 0 <= int(pas) <= 0:
            return False
        if valid(user, pas):
            username = user
            return True
        print('Invalid')
    

def register():
    user = input('Please create a username: ')
    pas = input('Please create a password: ')
    add([user, sha224(pas.encode('utf-8')).hexdigest()])

if __name__ == '__main__':
    menu()