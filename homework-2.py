
# Консольний термінал банкомата

CORRECT_CARD = "4441"
CORRECT_PIN = "7421"

authorized = False

print("=== ВІТАЄМО У БАНКІВСЬКОМУ ТЕРМІНАЛІ ===")

# Етап 1. Авторизація
for attempt in range(1, 4):
    card = input("Введіть останні 4 цифри картки: ")
    pin = input("Введіть PIN-код: ")

    if card == CORRECT_CARD and pin == CORRECT_PIN:
        print("Авторизація успішна!")
        authorized = True
        break
    else:
        attempts_left = 3 - attempt
        print("Неправильна картка або PIN-код.")

        if attempts_left > 0:
            print("Залишилось спроб:", attempts_left)

# Якщо авторизація не пройдена
if not authorized:
    print("Картку заблоковано через підозрілу активність!")

else:
    # Етап 2. Меню банкомата
    balance = 1000

    while True:
        print("\n=== МЕНЮ БАНКОМАТА ===")
        print("1 - Перевірити баланс")
        print("2 - Зняти кошти")
        print("3 - Поповнити рахунок")
        print("4 - Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            print("Ваш баланс:", balance, "грн.")

        elif choice == "2":
            amount = float(input("Введіть суму для зняття: "))

            if amount > 0 and amount <= balance:
                balance = balance - amount
                print("Гроші успішно знято!")
                print("Залишок:", balance, "грн.")
            else:
                print("Помилка! Некоректна сума або недостатньо коштів.")

        elif choice == "3":
            amount = float(input("Введіть суму поповнення: "))

            if amount > 0:
                balance = balance + amount
                print("Рахунок успішно поповнено!")
                print("Новий баланс:", balance, "грн.")
            else:
                print("Помилка! Сума поповнення має бути більшою за 0.")

        elif choice == "4":
            print("Дякуємо за користування банкоматом!")
            break

        else:
            print("Невідома команда! Спробуйте ще раз.")

