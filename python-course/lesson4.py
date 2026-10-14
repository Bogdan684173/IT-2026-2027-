# Менеджер команди пригодників з функціями та обробкою помилок

team = [
    {"name": "Аріа",    "class": "лучниця",   "level": 5, "hp": 42},
    {"name": "Богдан",  "class": "воїн",       "level": 7, "hp": 68},
    {"name": "Соломія", "class": "чарівниця",  "level": 4, "hp": 30},
]
# для запуску - "python lesson4.py" cd python-course

def print_team(team): #створення функції команди
    print("Твоя команда пригодників:")
    for hero in team:
        print(hero["name"], "-", hero["class"], "- рівень", hero["level"], "- HP", hero["hp"])


def team_stats(team):
    total_hp    = 0
    total_level = 0
    for hero in team:
        total_hp    = total_hp    + hero["hp"]
        total_level = total_level + hero["level"]
    average_level = total_level / len(team)
    return total_hp, average_level


def get_int_input(prompt):#безпечне введення числа
    while True:
        value = input(prompt)#введення числа
        try:
            return int(value)#переводимо в ціле число
        except ValueError:#перевірка на число
            print("Це не схоже на ціле число. Спробуй ще раз.")


def add_hero(team):#додавання нового героя до команди
    print()
    print("Додаємо нового героя до команди.")
    new_name  = input("Ім'я нового героя: ")
    new_class = input("Клас героя (воїн/лучниця/чарівниця): ")
    new_level = get_int_input("Рівень героя: ")
    new_hp    = get_int_input("Кількість HP: ")
    new_hero  = {
        "name":  new_name,
        "class": new_class,
        "level": new_level,
        "hp":    new_hp,
    }
    team.append(new_hero)
    print(new_name, "приєднався(лася) до команди!")


def find_hero(team, name):#функція пошуку героя в команді
    for hero in team:
        if hero["name"].lower() == name.lower():
            return hero# повертаємо героя якщо він знайдений
    return None

#функція для зміни класу героя 
def change_hero_class(team, name, new_class):
    hero = find_hero(team, name)
    if hero is not None:
        hero["class"] = new_class
        print(hero["name"], "тепер", hero["class"])
    else:
        print("Героя з таким ім'ям немає в команді.")

def main():
    print_team(team)

    add_hero(team)
    print()
    print_team(team)
    change_hero_class(team, "Аріа", "чарівниця")
    total_hp, average_level = team_stats(team)
    print()
    print("Загальний HP команди:", total_hp)
    print("Середній рівень команди:", average_level)

    print()
    search_name = input("Введи ім'я героя для пошуку: ")
    found_hero  = find_hero(team, search_name)

    if found_hero is not None:
        print("Знайдено:", found_hero["name"], "-", found_hero["class"], "- рівень", found_hero["level"])
    else:
        print("Героя з таким ім'ям немає в команді.")


main()