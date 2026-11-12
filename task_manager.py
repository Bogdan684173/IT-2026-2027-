
import random
import json

TASKS_FILE = "tasks.json"
STATS_FILE = "stats.json"


# Позначення завдання як виконаного
def mark_task_done(tasks):
    if not tasks:
        print("Список завдань порожній.")
        return

    view_tasks(tasks)

    number = input("Введи номер виконаного завдання: ").strip()

    if not number.isdigit():
        print("Потрібно ввести ціле число.")
        return

    number = int(number)

    if number < 1 or number > len(tasks):
        print("Немає завдання з таким номером.")
        return

    tasks[number - 1]["done"] = True
    print("Завдання позначено виконаним:", tasks[number - 1]["text"])
    save_tasks(tasks)


# Генерація пароля
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Згенерований пароль:", password)
    return password


# Перевірка надійності пароля
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


# Створення майстер-пароля
def set_master_password():
    while True:
        password = input("Введіть пароль: ")

        if check_password_strength(password) == "слабкий":
            choice = input(
                "Хочете змінити пароль, бо він слабкий? (так/ні): "
            )

            if choice.lower() == "так":
                password = generate_password(12)
                return password
        else:
            return password


# Перевірка пароля
def login_gate(master_password):
    password = input("Введіть пароль для входу: ")

    if password == master_password:
        return True
    else:
        return False


# Головне меню
def show_menu(tasks):
    while True:
        print("\n===== МЕНЕДЖЕР ЗАДАЧ =====")
        print("1) Додати завдання")
        print("2) Переглянути завдання")
        print("3) Видалити завдання")
        print("4) Позначити завдання виконаним")
        print("5) Вийти")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            mark_task_done(tasks)

        elif choice == "5":
            print("Робота завершена!")
            break

        else:
            print("Неправильний вибір! Введіть число від 1 до 5.")


# Додавання завдання
def add_task(tasks):
    choice = input("Введи назву завдання: ").strip()

    if not choice:
        print("Назва завдання не може бути порожньою.")
        return

    tasks.append({"text": choice, "done": False})
    save_tasks(tasks)
    print("Завдання успішно додано!")


# Збереження завдань
def save_tasks(tasks, filename=TASKS_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


# Завантаження завдань із захистом від пошкодженого JSON
def load_tasks(filename=TASKS_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Попередження: файл даних пошкоджено. Створюємо новий список.")
        return []


# Перегляд завдань
def view_tasks(tasks):
    if not tasks:
        print("Немає завдань.")
        return

    print("\n===== СПИСОК ЗАВДАНЬ =====")

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['text']} - {status}")


# Видалення завдання
def delete_task(tasks):
    if not tasks:
        print("Список завдань порожній.")
        return

    view_tasks(tasks)

    choice = input("Введіть номер завдання для видалення: ").strip()

    if not choice.isdigit():
        print("Потрібно ввести ціле число.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(tasks):
        print("Немає завдання з таким номером.")
        return

    removed_task = tasks.pop(choice - 1)
    save_tasks(tasks)

    print("Завдання видалено:", removed_task["text"])


# Завантаження статистики запусків
def load_stats():
    try:
        with open(STATS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return {"runs": 0}

    except json.JSONDecodeError:
        print("Попередження: файл статистики пошкоджено.")
        return {"runs": 0}


# Збереження статистики запусків
def save_stats(stats):
    with open(STATS_FILE, "w", encoding="utf-8") as file:
        json.dump(stats, file, ensure_ascii=False, indent=2)


# Головна функція програми
def main():
    tasks = load_tasks()

    master_password = set_master_password()

    if not login_gate(master_password):
        print("В доступі відмовлено.")
        print("Робота закінчена.")
        return

    # Оновлення статистики після успішного входу
    stats = load_stats()
    stats["runs"] += 1
    save_stats(stats)

    print(f"\nВітаємо! Це ваш {stats['runs']}-й сеанс роботи з Менеджером задач!")

    show_menu(tasks)


# Перевірка запуску програми
if __name__ == "__main__":
    main()
