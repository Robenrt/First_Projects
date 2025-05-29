from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
# write_key()

Authentication = input("What's the master Password? ")

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() + Authentication.encode()
fer = Fernet(key)

def view():
    with open("password.txt") as file:
        for line in file.readlines():
            data = line.strip()
            website,user,passw = data.split(":")
            print(f"web:{website} username:{user} password:{fer.decrypt(passw.encode()).decode()}")


def add():
    website = input("Web Adress: ")
    username = input("Account name: ")
    pwd = input("Password: ")
    with open("password.txt", "a") as file:
        file.write(f"{website} : {username} : {fer.encrypt(pwd.encode()).decode()}\n")


while True:
    mode = input("Would you like to add a new password or view existing ones(a/v)?, press 'q' to quit! ").strip().lower()
    if "q" in mode:
        break

    elif "v" in mode:
        view()
    elif "a" in mode:
        add()
    else:
        print("invalid entry!")

