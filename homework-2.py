
import random


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    password = ""

    for i in range(length):
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

        if check_password_strength(password) == "слабкий":
            choice = input("Хочете змінити слабкий пароль? (так/ні): ")

            if choice.lower() == "так":
                password = generate_password(12)
                return password
        else:
            return password


# Авторизація з трьома спробами
def login_gate(master_password):
    for attempt in range(1, 4):
        password = input("Введіть пароль: ")

        if password == master_password:
            print("Авторизація успішна! Вітаємо!")
            return True
        else:
            attempts_left = 3 - attempt

            print(f"Невірний пароль! Спроба {attempt} з 3.")
            print(f"Залишилося спроб: {attempts_left}")

    print("Доступ заблоковано через підозрілу активність!")
    return False


def show_menu(tasks):
    while True:
        print("\n=== МЕНЕДЖЕР ЗАВДАНЬ ===")
        print("1) Додати завдання")
        print("2) Переглянути завдання")
        print("3) Видалити завдання")
        print("4) Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Вихід із менеджера завдань!")
            break
        else:
            print("Невідома команда! Спробуйте ще раз.")


def add_task(tasks):
    choice = input("Введи назву завдання: ")
    tasks.append({"text": choice, "done": False})
    print("Завдання успішно додано!")


def view_tasks(tasks):
    if not tasks:
        print("Немає завдань!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. {task['text']} - {status}")


def delete_task(tasks):
    if not tasks:
        print("Немає завдань для видалення!")
        return

    view_tasks(tasks)

    choice = int(input("Введіть номер завдання для видалення: "))

    if 1 <= choice <= len(tasks):
        tasks.pop(choice - 1)
        print("Завдання успішно видалено!")
    else:
        print("Завдання з таким номером не існує!")


# Головна функція з блокуванням меню
def main():
    tasks = []
    master_password = set_master_password()

    access_granted = login_gate(master_password)

    if not access_granted:
        print("В доступі відмовлено")
        print("Робота закінчена")
        return

    show_menu(tasks)

    print("Робота закінчена")


main()
