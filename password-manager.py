# here user can create a passowrd and store in a way to password.txt file while encoding it and can acces it by decoding it
from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", 'wb') as key_file:
#         key_file.write(key)



def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split('|')
            print(f"user : {user}, password : {str(fer.decrypt(pwd.encode()).decode())}")
            

def add():
    name = input('Account Name : ')
    password = input('enter you password : ')

    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(password.encode()).decode() + '\n')

while True:
    mode = input(f"would you like to add new password or view the existing one (view/ add ) press q to quit: ").lower()
    
    if mode== 'view':
        view()
    elif mode == 'add':
        add()

    elif mode == 'q':
        break
    else:
        print('invalid option ')
        continue