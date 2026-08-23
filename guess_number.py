import random
secret_number = random.randint(1, 4)

for attempts in range(3):
    number = int(input("Введите загаданное число: "))
    if number == secret_number:
        print("Поздравляем вы выиграли!")
        break
    elif number > secret_number:
        print("Загаданное число меньше!")
    else:
        print("Загаданное число больше!")
