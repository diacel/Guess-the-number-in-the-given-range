import random

def guess_number():
    min_num = int(input("Введите минимальное значение диапазона: "))
    max_num = int(input("Введите максимальное значение диапазона: "))
    max_attempts = int(input("Введите количество попыток: "))

    # Загадываем число
    secret_number = random.randint(min_num, max_num)

    # Пользователь пытается отгадать число
    for attempt in range(max_attempts):
        guess = int(input("Введите ваше предположение: "))

        if guess == secret_number:
            print("Поздравляю! Вы отгадали число.")
            return

        elif guess < secret_number:
            print("Загаданное число больше вашего предположения.")

        else:
            print("Загаданное число меньше вашего предположения.")

    # Если все попытки использованы и число так и не отгадано
    print("К сожалению, вы использовали все попытки. Загаданное число было:", secret_number)

guess_number()