# Менеджер команди пригодників

team = [
    {"name": "Аріа",    "class": "лучниця",   "level": 5, "hp": 42},
    {"name": "Богдан",  "class": "воїн",       "level": 7, "hp": 68},
    {"name": "Соломія", "class": "чарівниця",  "level": 4, "hp": 30},
]

print("Твоя команда пригодників:")
for hero in team:
    print(hero["name"], "-", hero["class"], "- рівень", hero["level"], "- HP", hero["hp"])

print()
print("Додаємо нового героя до команди.")
new_name  = input("Ім'я нового героя: ")
new_class = input("Клас героя (воїн/лучниця/чарівниця): ")
new_level = input("Рівень героя: ")
new_hp    = input("Кількість HP: ")

new_hero = {
    "name":  new_name,
    "class": new_class,
    "level": int(new_level),
    "hp":    int(new_hp),
}
team.append(new_hero)

print()
print("Оновлена команда:")
for hero in team:
    print(hero["name"], "-", hero["class"], "- рівень", hero["level"], "- HP", hero["hp"])

total_hp    = 0
total_level = 0
for hero in team:
    total_hp    = total_hp    + hero["hp"]
    total_level = total_level + hero["level"]

average_level = total_level / len(team)

print()
print("Загальний HP команди:", total_hp)
print("Середній рівень команди:", average_level)

print()
search_name = input("Введи ім'я героя для пошуку: ")
found = False

for hero in team:
    if hero["name"].lower() == search_name.lower():
        print("Знайдено:", hero["name"], "-", hero["class"], "- рівень", hero["level"])
        found = True
        break

if not found:
    print("Героя з таким ім'ям немає в команді.")
