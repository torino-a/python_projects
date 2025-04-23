from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Слишком высоко")
        return turns - 1
    elif user_guess < actual_answer:
        print("Слишком низко")
        return turns - 1
    else:
        print(f"Верно! Ответ: {actual_answer}")


def set_difficulty():
    level = input("Выберите сложность. Например, 'лёгкий' или 'сложный': ")
    if level == "лёгкий":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Добро пожаловать в игру \"Угадай число\"!")
    print("Я загадал число в диапазоне от 1 до 100")
    answer = randint(1, 100)
    print(f"Скрытая проверка, загаданное число: {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"У вас осталось {turns} ходов чтобы угадать число.")
        # Let the user guess a number
        guess = int(input("Ваш ответ: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("К сожалению вы не справились, попробуйте заново!")
            return
        elif guess != answer:
            print("Попробуйте заново!")

game()


