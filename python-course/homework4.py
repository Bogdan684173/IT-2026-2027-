# Журнал квестів мандрівника
#python homework4.py

def print_quests(quests):
    print("Журнал квестів:")

    for quest in quests:
        if quest["status"] == "виконано":
            print(
                f"[x] {quest['title']} — "
                f"нагорода: {quest['reward']} монет"
            )
        else:
            print(
                f"[ ] {quest['title']} — "
                f"нагорода: {quest['reward']} монет"
            )


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Будь ласка, введи число.")


def add_quest(quests):
    print()
    print("Додаємо новий квест.")

    title = input("Назва квесту: ").strip()
    reward = get_int_input("Нагорода в монетах: ")

    new_quest = {
        "title": title,
        "reward": reward,
        "status": "в процесі",
    }

    quests.append(new_quest)


def complete_quest(quests, title):
    for quest in quests:
        if quest["title"].lower().strip() == title.lower().strip():
            quest["status"] = "виконано"
            return True

    return False


def calculate_total_reward(quests):
    total_reward = 0

    for quest in quests:
        if quest["status"] == "виконано":
            total_reward = total_reward + quest["reward"]

    return total_reward


def main():
    quests = [
        {
            "title": "Знайти загублений меч",
            "reward": 100,
            "status": "в процесі",
        },
        {
            "title": "Перемогти гобліна",
            "reward": 150,
            "status": "виконано",
        },
        {
            "title": "Знайти стародавній артефакт",
            "reward": 300,
            "status": "в процесі",
        },
    ]

    print_quests(quests)

    add_quest(quests)

    print()

    completed_title = input(
        "Введи назву квесту, який ти щойно завершив: "
    ).strip()

    if complete_quest(quests, completed_title):
        print("Квест успішно позначено як виконаний!")
    else:
        print("Квест з такою назвою не знайдено.")

    print()
    print("Оновлений журнал квестів:")

    print_quests(quests)

    total_reward = calculate_total_reward(quests)

    print()
    print(f"Загальна сума заробленого золота: {total_reward} монет")


if __name__ == "__main__":
    main()