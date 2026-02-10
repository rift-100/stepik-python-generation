import random

word_list = ["ноутбук", "часы", "деньги", "бизнес", "музыка", "выгода", "разработчик"]


def get_word(list):
    return random.choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print("Давайте играть в угадайку слов!")
    while not guessed:
        print(display_hangman(tries))
        print(word_completion)
        user_input = input("Введите букву загаданного слова или слово целиком: ").strip().upper()

        while not user_input.isalpha() or user_input in guessed_letters or user_input in guessed_words or user_input in word_completion:
            if user_input in word_completion:
                user_input = input("Вы уже отгадали эту букву, введите другую или слово целиком: ").strip().upper()
            elif not user_input.isalpha():
                user_input = input("Вы ввели некоректное значение, введите букву или слово целиком: ").strip().upper()
            else:
                user_input = input("Вы уже вводили эту букву или слово, введите другую букву или слово целиком: ").strip().upper()

        if user_input == word:
            print("Поздравляем, вы угадали слово! Вы победили!")
            print(word.upper())
            guessed = True
        else:
            if len(user_input) > 1:
                guessed_words.append(user_input)
                tries -= 1
            else:
                if user_input in word:
                    word_completion_update = ""
                    for i in range(len(word)):
                        if word_completion[i].isalpha():
                            word_completion_update += word_completion[i]
                        elif word[i] == user_input:
                            word_completion_update += word[i]
                        else:
                            word_completion_update += "_"
                    word_completion = word_completion_update
                    if word_completion == word:
                        guessed = True
                        print("Поздравляем, вы угадали слово! Вы победили!")
                        print(word.upper())
                else:
                    guessed_letters.append(user_input)
                    tries -= 1

            if tries == 0:
                print("Вы проиграли, у вас кончились попытки. Загаданое слово: ", word.upper())
                break

while True:
    play(get_word(word_list))
    is_play_again = input("Сыграем ещё? (да/нет) ")
    if is_play_again.strip().lower() != "да":
        print("До встречи. Заходи ещё")
        break
