# Рюкзак мандрівника
# для запуску - "python homework3.py" cd python-course
backpack = [
    {"item": "зілля лікування", "type": "спорядження", "quantity": 3},
    {"item": "залізний меч", "type": "зброя", "quantity": 1},
    {"item": "смолоскип", "type": "спорядження", "quantity": 2},
]

print("Твій рюкзак:")

for item in backpack:
    print(f"• {item['item']} ({item['type']}) — {item['quantity']} шт.")

print()

print("Додаємо новий предмет до рюкзака.")

new_item = input("Назва предмета: ").strip()
new_type = input("Тип предмета (зброя/спорядження): ").strip()
new_quantity = int(input("Кількість: "))

found = False

for item in backpack:
    if item["item"].lower().strip() == new_item.lower().strip():
        item["quantity"] = item["quantity"] + new_quantity
        found = True
        break

if not found:
    new_item_data = {
        "item": new_item,
        "type": new_type,
        "quantity": new_quantity,
    }

    backpack.append(new_item_data)

print()

print("Оновлений рюкзак:")

for item in backpack:
    print(f"• {item['item']} ({item['type']}) — {item['quantity']} шт.")

total_quantity = 0

for item in backpack:
    total_quantity = total_quantity + item["quantity"]

print()

print(f"Загальна кількість предметів у рюкзаку: {total_quantity} шт.")

print()

search_item = input("Введи назву предмета для пошуку: ").lower().strip()

found = False

for item in backpack:
    if item["item"].lower().strip() == search_item:
        print(
            f"Знайдено: {item['item']} "
            f"({item['type']}) — {item['quantity']} шт."
        )
        found = True
        break

if not found:
    print(f"Предмета «{search_item}» немає в рюкзаку.")

print()

# Порахувати і вивести, скільки всього предметів типу спорядження є в рюкзаку

equipment_quantity = 0

for item in backpack:
    if item["type"].lower().strip() == "спорядження":
        equipment_quantity = equipment_quantity + item["quantity"]

print(f"Усього предметів типу «спорядження»: {equipment_quantity} шт.")

# Цикл перевіряє кожен предмет і додає його кількість,
# якщо його тип — спорядження.