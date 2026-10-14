#python homework4_pro.py

# Гільдія найманців: Термінал контрактів


def get_bounded_int(prompt, min_val, max_val):
    while True:
        try:
            number = int(input(prompt))

            if min_val <= number <= max_val:
                return number
            else:
                print(
                    f"Введи число від {min_val} до {max_val}."
                )

        except ValueError:
            print("Помилка! Потрібно ввести ціле число.")


def print_contracts(contracts):
    print("\n=== СПИСОК КОНТРАКТІВ ===")

    if len(contracts) == 0:
        print("Контрактів поки немає.")
        return

    for contract in contracts:
        if contract["status"] == "виконано":
            mark = "[x]"
        else:
            mark = "[ ]"

        print(
            f"{mark} ID: {contract['id']} | "
            f"{contract['title']} | "
            f"Нагорода: {contract['reward']} монет | "
            f"Статус: {contract['status']}"
        )


def add_contract(contracts):
    print("\n=== ДОДАВАННЯ КОНТРАКТУ ===")

    title = input("Назва контракту: ").strip()

    if title == "":
        print("Назва контракту не може бути порожньою.")
        return

    # Перевіряємо, чи існує така назва
    for contract in contracts:
        if contract["title"].lower().strip() == title.lower().strip():
            print("Контракт із такою назвою вже існує.")
            return

    reward = get_bounded_int(
        "Нагорода в монетах (0–1000000): ",
        0,
        1000000
    )

    # Визначаємо новий ID
    if len(contracts) == 0:
        new_id = 1
    else:
        new_id = max(
            contract["id"] for contract in contracts
        ) + 1

    new_contract = {
        "id": new_id,
        "title": title,
        "reward": reward,
        "status": "активний"
    }

    contracts.append(new_contract)

    print(f"Контракт успішно додано! Його ID: {new_id}")


def complete_contract(contracts):
    print("\n=== ЗАВЕРШЕННЯ КОНТРАКТУ ===")

    if len(contracts) == 0:
        print("Немає контрактів для завершення.")
        return

    contract_id = get_bounded_int(
        "Введи ID контракту: ",
        1,
        max(contract["id"] for contract in contracts)
    )

    for contract in contracts:
        if contract["id"] == contract_id:
            if contract["status"] == "виконано":
                print("Цей контракт уже виконано.")
                return

            contract["status"] = "виконано"
            print("Контракт успішно виконано!")
            return

    print("Контракт із таким ID не знайдено.")


def guild_statistics(contracts):
    if len(contracts) == 0:
        return 0, 0, 0

    completed_count = 0
    active_rewards = 0
    active_count = 0

    most_expensive = contracts[0]

    for contract in contracts:
        if contract["status"] == "виконано":
            completed_count += 1
        else:
            active_rewards += contract["reward"]
            active_count += 1

        if contract["reward"] > most_expensive["reward"]:
            most_expensive = contract

    completed_percent = (
        completed_count / len(contracts)
    ) * 100

    if active_count > 0:
        average_reward = active_rewards / active_count
    else:
        average_reward = 0

    most_expensive_title = most_expensive["title"]

    return (
        completed_percent,
        average_reward,
        most_expensive_title
    )


def show_statistics(contracts):
    print("\n=== СТАТИСТИКА ГІЛЬДІЇ ===")

    completed_percent, average_reward, most_expensive_title = (
        guild_statistics(contracts)
    )

    print(
        f"Виконано контрактів: "
        f"{completed_percent:.1f}%"
    )

    print(
        f"Середня нагорода активних контрактів: "
        f"{average_reward:.1f} монет"
    )

    if most_expensive_title == 0:
        print("Найдорожчий контракт: немає контрактів.")
    else:
        print(
            f"Найдорожчий контракт: "
            f"{most_expensive_title}"
        )


def main():
    # Список контрактів створюється всередині main()
    contracts = [
        {
            "id": 1,
            "title": "Перемогти гоблінів",
            "reward": 150,
            "status": "активний"
        },
        {
            "id": 2,
            "title": "Знайти загублений меч",
            "reward": 300,
            "status": "виконано"
        },
        {
            "id": 3,
            "title": "Захистити караван",
            "reward": 500,
            "status": "активний"
        }
    ]

    while True:
        print("\n==============================")
        print(" ГІЛЬДІЯ НАЙМАНЦІВ")
        print("==============================")
        print("1. Показати всі контракти")
        print("2. Додати контракт")
        print("3. Завершити контракт")
        print("4. Статистика гільдії")
        print("0. Вийти")

        choice = input("Обери пункт меню: ").strip()

        if choice == "1":
            print_contracts(contracts)

        elif choice == "2":
            add_contract(contracts)

        elif choice == "3":
            complete_contract(contracts)

        elif choice == "4":
            show_statistics(contracts)

        elif choice == "0":
            print("Дякуємо за роботу в гільдії!")
            break

        else:
            print("Невідомий пункт меню. Спробуй ще раз.")


if __name__ == "__main__":
    main()