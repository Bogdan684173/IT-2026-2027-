# Гра "Числовий детектив"
import random

play_again = True

print("=== ВІТАЄМО У ГРІ «ЧИСЛОВИЙ ДЕТЕКТИВ» ===")

while play_again:
    secret_number = random.randint(1, 100)
    max_attempts = 6
    guessed = False #dbdtlt jcm wt Новий раунд: комп'ютер загадав число від 1 до 100 

    print("\n--- Новий раунд: комп'ютер загадав число від 1 до 100 ---")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Спроба {attempt}/{max_attempts}. Твій варіант: "))

        if guess < 1 or guess > 100:
            print("Число поза діапазоном (1–100)! Спроба зарахована як помилка.")
            continue

        difference = abs(secret_number - guess)

        if guess == secret_number:
            print(f"Вітаємо! Ти розгадав число за {attempt} спроб(и)!")
            guessed = True
            break
        elif difference <= 5:
            if guess < secret_number:
                print("Гаряче! Моє число трохи більше.")
            else:
                print("Гаряче! Моє число трохи менше.")
        elif guess < secret_number:
            print("Холодно! Моє число більше.")
        else:
            print("Холодно! Моє число менше.")

    if not guessed:
        print(f"\nНа жаль, спроби вичерпано. Було загадано число {secret_number}.")

    # Запит на повтор гри
    answer = input("\nБажаєш зіграти ще раз? (так / ні): ").strip().lower()
    if answer != "так" and answer != "yes":
        play_again = False
        print("\nДякуємо за гру! До нових розслідувань.")