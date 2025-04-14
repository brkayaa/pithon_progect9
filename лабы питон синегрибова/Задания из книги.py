#упр 1

import random


def guessing_game():
    answer = random.randint(0, 100)
    print("Угадайте число от 0 до 100!")

    while True:
        user_input = input("Каковы ваши предположения? ")


        if not user_input.isdigit():
            print("Ошибка: пожалуйста, вводите только целые числа.")
            continue

        user_guess = int(user_input)


        if user_guess < 0 or user_guess > 100:
            print("Ошибка: число должно быть от 0 до 100 включительно!")
            continue

        if user_guess == answer:
            print(f'Правильно! Ответ: {user_guess}')
            break
        elif user_guess < answer:
            print(f'Ваше число {user_guess} слишком маленькое!')
        else:
            print(f'Ваше число {user_guess} слишком большое!')



guessing_game()