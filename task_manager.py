import random

import json

TASKS_FILE = "tasks.json"

def mark_task_done(tasks):

    if len(tasks) == 0:
        print("Список завдань порожній.")
        return
    view_tasks(tasks)
    number = input("Введи номер виконаного завдання: ")
    if not number.isdigit():
        print("Потрібно ввести число.")
        return
    number = int(number)
    if number < 1 or number > len(tasks):
        print("Немає завдання з таким номером.")
        return
    tasks[number - 1]["done"] = True
    print("Завдання позначено виконаним:", tasks[number - 1]["text"])


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
        if check_password_strength(password)=="слабкий":
            choice = input(" Хочете змінити пароль бо він слабкий? (так/ні): ")
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
        print("1) Додати завдання \n2) Переглянути завдання \n3) видалити завдання \n4) позначити завдання виконаним \n5) вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_done(tasks)
        else:
            break

def add_task(tasks):
        choice = input("Введи назву завдання: ")
        tasks.append({"text":choice, "done":False})


def save_tasks(tasks, filename=TASKS_FILE):
with open(filename, "w", encoding="utf-8") as file:
     json.dump(tasks, file, ensure_ascii=False, indent=2)

def load_tasks(filename=TASKS_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
except FileNotFoundError:
    return []

def view_tasks(tasks):
    if not tasks:
        print("Немає завдань")
    else:
        for i, task in enumerate(tasks, start=1):

            print(f"{i}. {task['text']} - {'✓' if task['done'] else '✗'}")

def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Введіть номер завдання для видалення: "))
    tasks.pop(choice - 1)

def main():
    tasks = load_tasks()
    master_password = set_master_password()
    if login_gate(master_password)== True:
        show_menu(tasks)
    else:
        print("В доступі відмовлено")
    print("Робота закінчена")

main()





