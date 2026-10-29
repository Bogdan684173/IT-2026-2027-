import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    password = ""

    for i in range(10):
        password += random.choice(characters)

    print("Згенерований пароль:", password)
    return password

def check_password_strength(password):
    has_digit = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
    if len(password) >= 8 and has_digit and has_upper:
        return "надійний"
    elif len(password) >= 6:
        return "середній"
    else:
        return "слабкий"

def set_master_password():
    while True:
        password = input("Введіть пароль: ")
        check_password_strength(password)=="слабкий":
            choice = input(" Хочете змінити пароль бо він слабкий? (так/ні): "
            if choice == "так":
                password = generate_password(12)
                return password
        else:
            return password
def login_gate(master_password):
    password = input("Введіть пароль: ")
    if password == master_password:
        return True
    else:
        return False

#    if input("Ваш вибір: ") == "1":
def show_menu():
    while True:
        print("1) Додати завдання \n2) Переглянути завдання \n3) видалити завдання \n4) вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        else:
            break




