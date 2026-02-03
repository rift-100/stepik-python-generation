import random

def play_game():
    print("Добро пожаловать в числовую угадайку")
    print("Давай угадаем число от 1 до X")
    max_num = int(input("Введите X: "))

    guess_num = random.randint(1, max_num)
    counter = 0


    def is_valid(n):
        return n // 1 == n and n >= 1 and n <= max_num

    while True:
        print(f"Введите целое число от 1 до {max_num}")
        answer = int(input())
        counter += 1
        if not is_valid(answer):
            print("А может быть все-таки введем целое число от 1 до 100?")
        elif answer < guess_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif answer > guess_num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif answer == guess_num:
            print(f"Вы угадали за {counter} попыток, поздравляем!")
            break

    is_again = input("Спасибо, что играли в числовую угадайку. Сыграем ещё? (да/нет) ")
    if is_again.lower().strip() == "да":
        play_game()

play_game()

print("До встречи!")
