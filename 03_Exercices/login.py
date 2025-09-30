class WrongLoginException(Exception):
    pass

class WrongPasswordException(Exception):
    pass

def input_login():
    try:
        login = input("Saisir votre login :")
        if not login.isalpha() or not login.islower():
            raise WrongLoginException("Login invalide")
    except WrongLoginException as wl:
        print(wl)
        return ""
    else:
        print("Login valide !")
        return login
    
def input_password():
    try:
        password = input("Saisir votre Password :")
        if not password.isdigit():
            raise WrongPasswordException("Password invalide")
    except WrongPasswordException as wp:
        print(wp)
        return ""
    else:
        print("Password valide !")
        return password
    

if __name__ == '__main__':
    login = ""
    password = ""
    while login == "" or password == "":
        login = input_login()
        password = input_password()